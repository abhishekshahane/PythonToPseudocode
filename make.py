from re import sub
import fori
import initialise
import out
import increment
f = open("text/docker.txt", "r")
file1 = open('output/out.txt', "w")
for x in f:
    # Assuming there aren't a for loop in a if statement and so on
    # Edge case
    if x.find("=")!=-1 and x.find("+=")==-1:
        make = initialise.main(x)
        file1.write(make)
    #New route for each different scenario
    elif x.find("+=")!=-1:
        makea = increment.main(x)
        file1.write(makea)
    elif x.find("for")!=-1:
        makeb = fori.main(x)
        file1.write(makeb)
    elif x.find("print")!=-1:
        makec = out.output(x)
        file1.write(makec)

        

