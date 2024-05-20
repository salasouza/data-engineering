#!/bin/bash

# Verifica se o argumento --path foi fornecido
if [ "$1" != "--path" ]; then
    echo "Uso: ./execute.sh --path arquivo.py"
    exit 1
fi

# Obtém o caminho do arquivo Python do próximo argumento
arquivo_python="$2"

# Verifica se o arquivo Python existe
if [ ! -f "$arquivo_python" ]; then
    echo "Arquivo Python não encontrado: $arquivo_python"
    exit 1
fi

# Executa o arquivo Python
python "$arquivo_python"
