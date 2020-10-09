from re import sub
import fori
import initialise
f = open("text/docker.txt", "r")
file1 = open('output/out.txt', "w")
for x in f:
    # Assuming there aren't a for loop in a if statement and so on
    if x.find("=")!=-1:
        make = initialise.main(x)
        file1.write(make)
    elif x.find("for")!=-1:
        makea = fori.main(x)
        file1.write(makea)
