from re import sub, findall
from extrafuncs import check, String
def main(a):
    b = a.split("+=")
    return f"{b[0]}<- {b[0]} + {b[1]}"
def decrement(a):
    b = a.split("-=")
    return f"{b[0]}<- {b[0]} - {b[1]}"
#If statements here idk why
def ifstatement(a):
    a=str(a)
    a = a.replace(":", "")
    c = findall(r"[\w']+", a)
    b = String(a)
    b = b.alphanum()
    c[0] = sub(c[0], "IF", c[0])
    j = list(map(lambda s: s.strip(), c))
    f=b.strip()
    return "{} {} {} {}".format(j[0], j[1], f, j[2])
def elseif(a):
    a=str(a)
    a = a.replace(":", "")
    c = findall(r"[\w']+", a)
    b = String(a)
    b = b.alphanum()
    c[0] = sub(c[0], "ELSE IF", c[0])
    j = list(map(lambda s: s.strip(), c))
    f=b.strip()
    return "{} {} {} {}".format(j[0], j[1], f, j[2])

