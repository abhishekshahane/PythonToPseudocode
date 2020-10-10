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
    return f"{b[0]} {b[1]} {b[2]} {b[3]} {b[4]}"
    
