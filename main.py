from parser import *
from renderer import Render
from gentable import createTable

testFile = "expression.txt"
raw = ""
with open(testFile,'r') as f:
    raw = f.read()

var,expr = ParseForTable(raw[:])

image = ParseForLaTex(raw[:])
Render(image)

createTable(var,expr)

