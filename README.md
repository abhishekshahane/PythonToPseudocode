# PythonToPseudocode
I got bored of converting Python to Pseudocode, so I made this.
<h3>Some notes to be made</h3>
<ol>
  <li>This program can and will make mistakes, it is not meant to be a complete substitute for writing your pseudocode, but to make the process easier.</li>
  <li>docker.txt and out.txt are tests</li>
  <li>Unfortunately, doesn't yet add NEXT or ENDIF</li>
</ol>

<b>How to use.</b>

1. Put your python code in docker.txt(Remember this only works for increments, print statements, for loops, if statements(AKA conditionals), while loops and initialising variables at the moment.)

2. Next, luckily for you, we've made a CLI to make this process easier. Simply run `cli.py --help` to see a help message or to run, type `cli.py --run [FILE]`, where [FILE] is your file(incase you wanted to migrate from make.py), and if those two commands don't work, simply run `python [FILE].py` and everything should work perfectly. Also, in case you were wondering, I used argparse to build that. Anyways, signing off on the project for now. Abhishek - 20/10/2020.
<br></br>

<h3>Exceptions</h3>
<ol>
   <li>Your python code has to run perfectly, otherwise the program will start glitching.</li>
</ol>
<h2>Enjoy!</h2>
