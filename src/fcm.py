from math import e, log2
from pathlib import Path
import pickle
import sys
import math

# python3 fcm.py ..\example\example.txt ..\example\output.txt 3


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

    #descobrir a quantidade de carateres unicos
    cardinality = len(''.join(set(x)))

    fcm_size = ( math.pow(cardinality, key) )* cardinality * 16 / 8 / 1024 / 1024 
    print(str(fcm_size))
    if fcm_size > 250:
        createHashMapTable(key, x, table, filePathToSave)
    else:
        createTable(key, x, table, filePathToSave)


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