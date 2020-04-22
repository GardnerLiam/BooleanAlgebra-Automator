from system import *

illegals = [" ","\n"]
operators = ["+","*"]
others = ["(",")","!"]

def remover(raw,illegals):
    cp = raw[:]
    for i in illegals:
        cp = cp.replace(i,"")
    return cp

def variables(raw):
    global illegals
    global operators
    global others

    return set(remover(raw,illegals+operators+others))

def chunkEndFinder(data):
    '''
    data starts after (
    returns ) index
    '''
    counter = 1
    for i in range(len(data)):
        if data[i] == "(":
            counter+=1
        if data[i] == ")":
            counter-=1
            if counter == 0:
                return i
def chunk(data,var):
    '''
    data starts after (
    returns parsed chunk and new index
    '''
    eod = chunkEndFinder(data)
    #print("CHUNK: {}".format(data))
    #print("CHUNK EOD INDEX: {}".format(eod))
    #print("CHUNK EOD VALUE: {}".format(data[eod]))
    toChunk = data[:eod]
    #print("CHUNKING: {}".format(toChunk))
    result = Onion(toChunk,var)
    #print("FINISHED CHUNKING")
    return result,eod+1


def Onion(raw,v=None):
    global illegals
    global operators
    var = variables(raw) if v is None else v
    parsed = remover(raw,illegals)
    function = []
    i = 0
    while i < len(parsed):
        if (parsed[i] in var) or (parsed[i] in operators):
            function.append(parsed[i])
            i += 1
        elif parsed[i] == "(":
            inter,inc = chunk(parsed[i+1:],var)
            function.append(inter)
            i += inc+i+1
            #print("NEXT CHAR: {}".format(parsed[i]))
        elif parsed[i] == "!":
            if parsed[i+1] in var:
                function.append([parsed[i],parsed[i+1]])
                i += 2
            elif parsed[i+1] == "(":
                inter,inc = chunk(parsed[i+2:],var)
                function.append([parsed[i],inter])
                i += inc+i+2
        else:
            warntext = "WARNING: Unknown character {} around ".format(parsed[i])
            if i+2 > len(parsed):
                warntext += parsed[i-2:]
            else:
                warntext += parsed[i-2:i+2]
            warning(warntext)
            i+=1
    return function

