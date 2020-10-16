from re import sub, findall
from extrafuncs import check
def main(a):
    b = a.split("+=")
    return f"{b[0]}<- {b[0]} + {b[1]}"
def decrement(a):
    b = a.split("-=")
    return f"{b[0]}<- {b[0]} - {b[1]}"
#If statements here idk why
def ifstatement(a):
    if a.count("==")==1:
        c = a.replace(":", "")
        c = c.replace("==", " ")
        c = c.split(" ")
        c[0] = sub(c[0], "IF", c[0])
        t = list(map(lambda s: s.strip(), c))
        j = check(t)
        f = "=="
        return "{} {} {} {}".format(j[0], j[1], f, j[2])
    elif a.count(">=")==1:
        c = a.replace(":", "")
        c = c.replace(">=", " ")
        c = c.split(" ")
        c[0] = sub(c[0], "IF", c[0])
        t = list(map(lambda s: s.strip(), c))
        j = check(t)
        f = ">="
        return "{} {} {} {}".format(j[0], j[1], f, j[2])
    elif a.count("<=")==1:
        c = a.replace(":", "")
        c = c.replace("<=", " ")
        c = c.split(" ")
        c[0] = sub(c[0], "IF", c[0])
        t = list(map(lambda s: s.strip(), c))
        j = check(t)
        f = "<="
        return "{} {} {} {}".format(j[0], j[1], f, j[2])
    elif a.count("!=")==1:
        c = a.replace(":", "")
        c = c.replace("!=", " ")
        c = c.split(" ")
        c[0] = sub(c[0], "IF", c[0])
        t = list(map(lambda s: s.strip(), c))
        j = check(t)
        f = "!="
        return "{} {} {} {}".format(j[0], j[1], f, j[2])
