import argparse
from os import system
import make
parser = argparse.ArgumentParser(description='CLI for PythonToPseudocode.')
parser.add_argument('--run', metavar='file', type=str,  help='runs the program')
args = parser.parse_args()
if "--run" in args:
    system(f'python make.py')
