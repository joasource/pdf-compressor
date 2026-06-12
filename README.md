# 📄 PDF Compressor

Uma ferramenta em container Docker para comprimir arquivos PDF de forma rápida, isolada e sem sujar o sistema host.

## 🛠️ Instalação

Para começar, clone este repositório para a sua máquina local e construa a imagem Docker:

```bash
# Clone o repositório
git clone https://github.com/joasource/pdf-compressor.git

# Entre no diretório
cd pdf-compressor

# Construa a imagem Docker
docker build -t pdf-compressor .

```

## 🚀 Como Usar

Com a imagem construída, você pode executar o compressor diretamente via Docker. O comando varia um pouco dependendo do seu sistema operacional ou terminal para mapear corretamente o diretório atual.

### 🐧 Linux e 🍏 macOS (Bash/Zsh)

```bash
docker run --rm -v "$(pwd)":/dados pdf-compressor documento.pdf --qualidade ebook

```

### 🪟 Windows (PowerShell)

```powershell
docker run --rm -v "${PWD}":/dados pdf-compressor documento.pdf --qualidade ebook

```

### 🪟 Windows (Prompt de Comando - CMD)

```cmd
docker run --rm -v "%cd%":/dados pdf-compressor documento.pdf --qualidade ebook

```

---

## 🎛️ Opções de Qualidade

Você pode extrair o máximo de desempenho do compressor alterando o argumento do parâmetro `--qualidade`. Escolha o perfil que melhor se adapta à sua necessidade:

| Opção | Resolução / Qualidade | Uso Ideal |
| --- | --- | --- |
| `screen` | Baixa resolução | Leitura em telas (gera o menor tamanho de arquivo possível) |
| `ebook` | Qualidade média | Um bom meio-termo para compartilhamento geral |
| `printer` | Alta qualidade | Preparado para impressão (tamanho de arquivo maior) |
| `prepress` | Qualidade máxima | Preserva quase a totalidade dos detalhes originais do documento |

---

### ⚙️ Parâmetros do Exemplo:

* `--rm`: Remove o container automaticamente após a conclusão do processo.
* `-v`: Espelha a pasta atual do seu terminal para a pasta `/dados` dentro do container (usando a sintaxe nativa de cada ambiente: `$(pwd)`, `${PWD}` ou `%cd%`).
* `meu_relatorio.pdf`: O nome do arquivo original que você deseja otimizar.
* `--qualidade screen`: Define o perfil de compressão (conforme a tabela acima).
