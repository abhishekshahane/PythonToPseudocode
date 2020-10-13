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
    if x.find("=")!=-1 and x.find("+=")==-1 and x.find("-=")==-1 and x.find("==")==-1 and x.find(">=")==-1 and x.find("<=")==-1 and x.find("!=")==-1:
        make = initialise.main(x)
        file1.write(make)
    elif x.find("+=")!=-1:
        makea = increment.main(x)
        file1.write(makea)
    elif x.find("for")!=-1:
        makeb = fori.main(x)
        a = f"{makeb[0]} {makeb[1]}{makeb[2]} {makeb[3]} {makeb[4]} {makeb[5]}\n"
        file1.write(a)
    elif x.find("print")!=-1:
        makec = out.output(x)
        file1.write(makec)
    elif "," in x and "print" in x:
        maked = harder.main(x)
        file1.write(maked)
    elif x.find("-=")!=-1:
        makee = increment.decrement(x)
        file1.write(makee)
    elif x.find("while")!=-1:
        makef = fori.whileloop(x)
        a = f"{makef[0]} {makef[1]}=={makef[2]} {makef[3]}\n"
        file1.write(a)
        
file1.close()
        

        


        

