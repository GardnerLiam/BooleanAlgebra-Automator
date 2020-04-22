from AST import *

from itertools import product
import types

def Peel(onion,variables,dictionary):
    c = onion[:]
    for i in range(len(onion)):
        if isinstance(onion[i],list):
            c[i] = Evaluate(Peel(onion[i],variables,dictionary),variables,dictionary)
    return c

def Evaluate(layer,v,d):
    c = []
    for i in range(len(layer)):
        if isinstance(layer[i],bool):
            c.append(str(layer[i]))
        elif layer[i] in v:
            c.append(str(d[layer[i]]))
        elif layer[i] == "!":
            c.append("not ")
        elif layer[i] == "+":
            c.append("|")
        elif layer[i] == "*":
            c.append("&")
    return eval(''.join(c))

