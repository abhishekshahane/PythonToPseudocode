from re import sub, findall
import os
import fori
import initialise
import out
import time
import increment
import harder
#Starting time
start_time = time.time()
#Line number
line = 1
f = open("text/docker.txt", "r")
file1 = open('output/out.txt', "w")
filesize = os.path.getsize("text/docker.txt")
if filesize==0:
    raise Exception(f"Filesize: {filesize}. Hmm, looks like your file is empty to us...")
for x in f:
    if "    " in x:
        raise Exception(f"Hmm, looks like you've indented your code on line {line}, please unindent it.")
    # Assuming there aren't a for loop in a if statement and so on
    # Edge case
    if x.find("=")!=-1 and x.find("+=")==-1 and x.find("-=")==-1 and x.find("==")==-1 and x.find(">=")==-1 and x.find("<=")==-1 and x.find("!=")==-1:
        make = initialise.main(x)
        file1.write(make)
    # For adding something to variables
    elif x.find("+=")!=-1:
        makea = increment.main(x)
        file1.write(makea)
    #For loop making
    elif x.find("for")!=-1:
        makeb = fori.main(x)
        a = f"{makeb[0]} {makeb[1]}{makeb[2]} {makeb[3]} {makeb[4]} {makeb[5]}\n"
        file1.write(a) #Writing
    #Printing 
    elif x.find("print")!=-1:
        makec = out.output(x)
        file1.write(makec)
    #Printing with vars
    elif "," in x and "print" in x:
        maked = harder.main(x)
        file1.write(maked)
    elif x.find("-=")!=-1:
        makee = increment.decrement(x)
        file1.write(makee)
    elif x.find("while")!=-1:
        makef = fori.whileloop(x)
        file1.write(makef)
    elif x.find("if")!=-1 and x.find("elif")==-1:
        makeg = increment.ifstatement(x) + "\nTHEN\n"
        file1.write(makeg)
    elif x.find("elif")!=-1:
        makeh = increment.elseif(x) + "\nTHEN\n"
        file1.write(makeh)

    
    else:
        raise Exception(f"Hmm, we didn't recongnize this line ({x}) on line {line}. We recommend you read README.md to make sure everything is correct!")
    line+=1
print("........................")
print("Executed sucessfully in: ", time.time()-start_time, " seconds.")
print("........................")
file1.close()
