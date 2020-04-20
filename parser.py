def ParseForTable(raw):
    legals = ['!', '+', '*', '(', ')'," ","\n"]

    stripped = raw[:]
    for i in legals:
        stripped = stripped.replace(i, "")
    variables = set(stripped)

    text = raw.replace("!","not ").replace("+","|").replace("*","&")

    return variables,text

def ParseForLaTex(raw):
    before = [r"!", r"*"]
    after =  [r"\overline",r"\cdot"]
    brackets = ["(",")"]
    text = [i for i in raw[:]]

    replaceNextBracket = False
    for i in range(len(text)):
        if i+1 < len(text):
            if (text[i] in before):
                if(text[i+1] == "(" and text[i]==before[0]):
                    replaceNextBracket = True
                    text[i+1] = '{'
                text[i] = after[before.index(text[i])]
        if replaceNextBracket:
            if (text[i] == ")"):
                text[i] = "}"
                replaceNextBracket = False

    return ("Q=" + ''.join(text))[:-1]
