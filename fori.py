from re import sub
# I was gonna use lambda functions but honestly who cares
# BTW docker.txt and out.txt are tests
# This whole project is still in development, so don't use it yet!!
def main(a):
    b = a.split(" ")
    b[0] = sub(b[0], "FOR", b[0])
    b[3] =  b[3].replace("range(", "")
    b[3] = b[3].replace(")", "")
    b[3] = b[3].replace(",", " TO ")
    b[3] = b[3].replace(":", "")
    b[2] = sub(b[2], "<-", b[2])
    b[4] = b[4].replace(")", "")
    b[4] = b[4].replace(":", "")
    return f"{b[0]} {b[1]} {b[2]} {b[3]}{b[4]}"
def whileloop(a):
    if a.count("==")==1:
        c = a.replace(":", "")
        c = c.replace("==", " ")
        c = c.split(" ")
        c[0] = sub(c[0], "WHILE", c[0])
        d = c + ["DO"]
        t = list(map(lambda s: s.strip(), d))
        return t


    
