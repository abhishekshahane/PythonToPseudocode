from re import sub
def main(a):
    b = a.split(" ")
    b[1] = sub("=", "<-", b[1])
    makefinala = "".join(b)
    return makefinala
