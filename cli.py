import argparse
from os import system
import make
from sys import argv
parser = argparse.ArgumentParser(description='CLI for PythonToPseudocode by Abhishek Shahane.')
parser.add_argument('--run', metavar='file', type=str,  help='runs the program')
args = parser.parse_args()
#The file is just for convenience, incase you want to change your filename from make.py to something else.
if "--run" in args:
    system(f'python {args[2]}')

