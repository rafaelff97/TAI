from math import e, log2
from pathlib import Path
import pickle
import sys

# python3 fcm.py example.txt output.txt 3


def createHashMapTable(key, x, table, filePathToSave):
    for counter in range(key, len(x)+1):
        #print("contador " + str(contador))
        combination = "".join(x[counter-key:counter])
        #print("combination " + combination)
        if combination not in table:
            table[combination] = {}

        nextLetter = "".join(x[counter:counter+1])

        if nextLetter in table[combination]:
            table[combination][nextLetter] += 1
        else:
            table[combination][nextLetter] = 1

    try:
        file = open(filePathToSave, 'wb')
    except FileNotFoundError:
        file = open(filePathToSave, 'wb')

    # arquivo.write(str(table))
    pickle.dump(table, file)
    file.close()
    # print(str(table))


def createTable(key, x, table, filePathToSave):
    for counter in range(key, len(x)+1):
        #print("contador " + str(contador))
        combination = "".join(x[counter-key:counter])
        #print("combinacao " + combinacao)
        if combination not in table:
            table[combination] = {}
            for i in range(33, 127):
                table[combination][chr(i)] = 0

        nextLetter = "".join(x[counter:counter+1])

        if nextLetter in table[combination]:
            table[combination][nextLetter] += 1

    try:
        file = open(filePathToSave, 'wb')
    except FileNotFoundError:
        file = open(filePathToSave, 'wb')

    # arquivo.write(str(table))
    pickle.dump(table, file)
    file.close()
    # print(str(table))


def readText(path, key, filePathToSave):
    f = open(path)
    text = f.readlines()
    x = []
    for line in text:
        x.extend(line)
    f.close()
    # print(x)
    # iterar

    # key = int(input("Key size?\n"))  # key
    table = {}

    # tamanho do texto
    textSize = Path(path).stat().st_size

    if textSize > 250:
        createHashMapTable(key, x, table, filePathToSave)
    else:
        createTable(key, x, table, filePathToSave)

    # C:\\Users\\rFael\\OneDrive\\Ambiente de Trabalho\\Mestrado EI\\2021-2022\\TAI\\Projeto_01\\example.txt


def usage():
    print("Usage: python3 fcm.py \n\t<input path file: string> \n\t<output path file: string> \n\t<key:int>\n")


if __name__ == "__main__":
    arguments = sys.argv

    if len(arguments) != 4:
        usage()
        sys.exit(2)

    path = str(arguments[1])
    filePathToSave = str(arguments[2])
    key = int(arguments[3])
    readText(path, key, filePathToSave)
