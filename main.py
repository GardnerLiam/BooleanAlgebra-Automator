from table import PrintTable
from AST import *



tests = ["!(A+B)+(A*B)","!a + !b"]

raw = tests[1]

v = list(variables(raw))
o = Onion(raw)
print(o)
print)
PrintTable(o,v)
