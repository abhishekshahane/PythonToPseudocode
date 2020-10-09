from re import sub
def output(a):
    b=a.split("(")
    b[1] = b[1].replace(")", "")
    b[0] = sub(b[0], "OUTPUT", b[0])
    final = " ".join(b)
    return final
