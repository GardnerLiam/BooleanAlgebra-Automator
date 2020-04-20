import os

#example: sample = r"Q=\overline{a}\cdot\overline{b} + \overline{\overline{a}+b}"

def Render(sample):

    tex = ""
    with open('template.tex', 'r') as f:
        tex = f.read().replace("EQUATION",sample)

    with open("writer/main.tex", "w") as f:
        f.write(tex)

    os.chdir("writer")
    os.system("pdflatex --shell-escape main.tex 2>&1 > /dev/null")
    os.system("pdftoppm main.pdf expression -png")
    os.system("mv expression-1.png ../Q.png")
    #os.system("rm -rf main.*")
