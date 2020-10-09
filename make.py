from re import sub
import fori
import initialise
f = open("text/docker.txt", "r")
file1 = open('output/out.txt', "w")
a = f.readline()
b = f.readline()
c = f.readline()
d = f.readline()
if a.find("=")!=-1:
    make = initialise.main(a)
    file1.write(make)
if b.find("for")!=-1:
    makea = fori.main(b)
    file1.write(makea)
if c.find("for")!=-1:
    makea = fori.main(c)
    file1.write(makea)
if d.find("=")!=-1:
    make = initialise.main(d)
    file1.write(make)

