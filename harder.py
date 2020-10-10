from re import sub, findall
def main(a):
    b = findall(r"[\w']+", a)
    b[0] = sub(b[0], "OUTPUT", b[0])
    return f"{b[0]} {b[1]}, {b[2]}"
