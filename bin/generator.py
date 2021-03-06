import random
import string
import pickle
import math
import sys
import time

##Use Mode
# python3 generator.py ..\example\output.txt 10 3 ola 2


def generator(path, size, nSymbols, sequence, alpha):
    x = []
    path = open(path, "rb")
    tabela = pickle.load(path)
    path.close()
    # print(tabela)

    x.extend(sequence)
    nextSymbol = ""
    for adicoes in range(nSymbols):
        combination = "".join(x[len(x)-size:])
        if combination in tabela:
            nextSymbol = random.choices(
                list(tabela[combination].keys()), weights=tabela[combination].values(), k=1)[0]
        else:
            nextSymbol = ''.join([random.choice(
                string.ascii_letters + string.digits + string.punctuation) for n in range(1)])
        sequence += nextSymbol
        x.append(nextSymbol)
        print(sequence)

    # print(tabela)
    summation = 0
    summationTotal = 0
    nPossibleSymbols = 0
    h = 0
    hFinal = 0
    for i in tabela:
        for j in tabela[i]:
            summationTotal += tabela[i][j]
            nPossibleSymbols += 1

    for i in tabela:
        for j in tabela[i]:
            summation += tabela[i][j]

        # print(summation)
        for j in tabela[i]:
            # if tabela[i][j] != 0:
            tabela[i][j] = ((tabela[i][j] + alpha) /
                            (summation + (alpha * nPossibleSymbols)))
            h += -tabela[i][j] * math.log(tabela[i][j], 2)

        hFinal += h * (summation / summationTotal)
        summation = 0
        nPossibleSymbols = 0
        h = 0

    # print("----------------------------------------------------------------")
    # print("Tabela:")
    # print(tabela)
    print("----------------------------------------------------------------")
    print("Sumatório total:"+str(summationTotal))
    print("----------------------------------------------------------------")
    print("hFinal:" + str(hFinal))
    print("----------------------------------------------------------------")


def usage():
    print("Usage: python3 generator.py \n\t<path_file: string> \n\t<number of symbols:int>\n\t-k <key:int>\n\t<Words sequence:string>\n\t <alpha: float>" )


if __name__ == "__main__":
    arguments = sys.argv

    if len(arguments) != 6:
        usage()
        sys.exit(2)


    path  = str(arguments[1])
    nSymbols = int(arguments[2])
    size = int(arguments[3])
    sequence = str(arguments[4])
    alpha = float(arguments[5])

    t0 = time.time()
    generator(path, size,nSymbols, sequence, alpha)
    t1 = time.time()
    print("Tempo que demora a gerar o texto: "+ str(t1-t0))