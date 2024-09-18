# Importe o módulo 'os' e utilize a função 'listdir' para listar todos os arquivos e diretórios no diretório atual.
# A função 'listdir' retornará uma lista com os nomes dos arquivos e diretórios presentes no diretório onde o script 
# está sendo executado. Em seguida, exiba o conteúdo dessa lista

import os

# lista arquivods de um diretório atual
diret = os.listdir()

# Exibe o que tem no diretório
for i in diret:
    print(i)