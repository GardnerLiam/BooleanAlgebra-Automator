from itertools import product

def evaluate(expr,value,variables):
    c = expr[:]
    for i in range(len(variables)):
        c = c.replace(variables[i]," "+str(value[i]))
    return int(eval(c))

def createTable(variables,expr):
    values = [p for p in product([1,0],repeat=len(variables))]
    table = [evaluate(expr[:],values[i],list(variables)) for i in range(len(values))]
    v = list(variables) + ["Q"]
    for i in range(len(v)):
        print("{}".format(v[i]),end="\t")
    print()
    for i in range(len(table)):
        for r in values[i]:
            print("{}".format(int(r)),end="\t")
        print(table[i])
    print()
