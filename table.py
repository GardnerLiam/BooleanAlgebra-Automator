from itertools import product
from parser import Peel, Evaluate
from AST import *

def toDicts(variables):
    hashmaps = []
    prd = product([True,False],repeat=len(variables))
    for i in prd:
        d = {}
        for v in range(len(variables)):
            d[variables[v]] = i[v]
        hashmaps.append(d)
    return hashmaps

def PrintTable(onionized,variables):
    dictionaries = toDicts(variables)
    for i in variables:
        print("{}".format(i),end="\t")
    print("Q")
    for d in dictionaries:
        peeled = Peel(onionized,variables,d)
        answer = Evaluate(peeled,variables,d)
        for v in variables:
            print("{}".format(int(d[v])),end="\t")
        print(int(answer))
    print()
