Trabalho 1\n
O objetivo do programa é criar um modelo com a finalidade de coletar informações estatísticas sobre textos, utilizando modelos de contexto finito.
Um modelo de contexto finito (Markov), de ordem k, produz a distribuição de probabilidade do próximo símbolo em uma sequência de símbolos, considerando a história recente até a profundidade k.

Elementos do grupo:
Rafael da Fonseca Fernandes - 95319
Gonçalo Junqueira - 95314
João Pedro Pereira - 106346


Trabalho de laboratório 1
Para executar o programa, é necessário ter requisitos minimos.
Requisitos: Python 3

De seguida é necessário correr os comandos abaixo no diretório src:

# Generator
python3 generator.py path_file number_of_symbols key words_sequence alpha" )
Exemplo: python3 generator.py ..\example\output.txt 10 3 ola 2

# FCM
python3 fcm.py input_path_file output_path_file key
Exemplo: python3 fcm.py ..\example\example.txt ..\example\output.txt 3

Parâmetros:
path_file : caminho do arquivo que resultou do fcm
number_of_symbols: número de simbolos para gerar
key: ordem do modelo (k> 0)
words_sequence: sequência inicial
alpha: parâmetro de suavização (0> = a <= 1)
input_path_file: caminho do arquivo onde está o texto
output_path_file: caminho para guardar o resultado do fcm nesse arquivo

Resultados esperados para o exemplo descritos:
Sumatório total:4351184
Entropy:2.080465836173141
Text generation time: 0.057631731033325195 seconds
