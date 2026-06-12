import os
import sys
import subprocess
import argparse

def extrair_nome_saida(caminho_entrada):
    """Gera o nome de saída adicionando '_reduzido' antes da extensão."""
    diretorio, arquivo = os.path.split(caminho_entrada)
    nome_base, extensao = os.path.splitext(arquivo)

    # Se o arquivo for 'documento.pdf', vira 'documento_reduzido.pdf'
    nome_saida = f"{nome_base}_reduzido{extensao}"

    # Mantém no mesmo diretório que o arquivo de entrada foi mapeado
    return os.path.join(diretorio, nome_saida)

def comprimir_pdf(caminho_entrada, qualidade):
    if not os.path.exists(caminho_entrada):
        print(f"Erro: O arquivo '{caminho_entrada}' não foi encontrado.")
        sys.exit(1)

    caminho_saida = extrair_nome_saida(caminho_entrada)

    tamanho_original = os.path.getsize(caminho_entrada) / (1024 * 1024)
    print(f"Processando: {os.path.basename(caminho_entrada)} ({tamanho_original:.2f} MB)")
    print(f"Qualidade selecionada: {qualidade}")

    comando = [
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS=/{qualidade}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={caminho_saida}",
        caminho_entrada
    ]

    try:
        subprocess.run(comando, check=True)
        tamanho_novo = os.path.getsize(caminho_saida) / (1024 * 1024)

        print("\n Redução concluída com sucesso!")
        print(f"Arquivo gerado: {os.path.basename(caminho_saida)}")
        print(f"Tamanho reduzido: {tamanho_novo:.2f} MB")
        print(f"Taxa de compressão: {((1 - (tamanho_novo / tamanho_original)) * 100):.1f}% menor.")

    except subprocess.CalledProcessError as e:
        print(f"Erro na execução do Ghostscript: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Comprime PDFs usando Ghostscript dentro do Docker.")
    parser.add_argument("arquivo", help="Nome ou caminho do arquivo PDF de entrada (dentro da pasta mapeada).")
    parser.add_argument(
        "--qualidade",
        default="ebook",
        choices=["screen", "ebook", "printer", "prepress"],
        help="Nível de qualidade/compressão (padrão: ebook)"
    )

    args = parser.parse_args()
    comprimir_pdf(args.arquivo, args.qualidade)
