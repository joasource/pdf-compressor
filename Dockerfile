FROM python:3.11-slim

# Evita que o Python escreva arquivos .pyc e força o output direto no terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala o Ghostscript e limpa o cache do apt para reduzir o tamanho da imagem
RUN apt-get update && apt-get install -y --no-install-recommends \
    ghostscript \
    && rm -rf /var/lib/apt/lists/*

# Cria o diretório de trabalho dentro do container
WORKDIR /app

# Copia o script para dentro do container
COPY comprimir.py .

# Define o diretório /dados como o local onde vamos mapear nossos arquivos locais
WORKDIR /dados

# Define o comando padrão que será executado ao rodar o container
ENTRYPOINT ["python", "/app/comprimir.py"]
