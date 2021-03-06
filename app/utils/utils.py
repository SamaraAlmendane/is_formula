import re

def isNegacao(c):
    return c == '~'

def isConectivo(c):
    return c == '~' or c == '^' or c == 'v' or c == '-' or c == '='


def isSimbolo(c):
    return c == 'T' or c == 'F' or c == 'A' or c == 'B' or c == 'C' or c == 'D' or c == 'E' or c == 'G' or c == 'H' or c == 'I' or c == 'J' or c == 'K'
    #P Q R S P1 R1 ...

def isCaractereValido(c):
    return re.search("[PQRS]", c) or re.search("[0-9]", c) or c == '^' or c == 'v' or c == '<' or c == '-' or c == '>' or c == '~' or c == '(' or c == ')' or c == 'T' or c == 'F'

def validaCaracteresFormula(formula):
    tamFormula = len(formula)
    pos = 0
    while pos < tamFormula:
        if not isCaractereValido(formula[pos]):
            return {"resultado": False, "error": "caractere invalido: {c}".format(c=formula[pos])}
        pos += 1
    return {"resultado": True, "error": ""}

def contSimbolos(formula):
    arrayMatchs = re.findall("[SPRQ][0-9]*[0-9]*", formula)
    return len(arrayMatchs)
