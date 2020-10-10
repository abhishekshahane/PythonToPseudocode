from re import sub, findall
import fori
import initialise
import out
import increment
import harder
f = open("text/docker.txt", "r")
file1 = open('output/out.txt', "w")
for x in f:
    # Assuming there aren't a for loop in a if statement and so on
    # Edge case
    if x.find("=")!=-1 and x.find("+=")==-1:
        make = initialise.main(x)
        file1.write(make)
    elif x.find("+=")!=-1:
        makea = increment.main(x)
        file1.write(makea)
    elif x.find("for")!=-1:
        makeb = fori.main(x)
        file1.write(makeb)
    elif x.find("print")!=-1:
        makec = out.output(x)
        file1.write(makec)
    elif "," in x and "print" in x:
        maked = harder.main(x)
        file1.write(maked)

        
