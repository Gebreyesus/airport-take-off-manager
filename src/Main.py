"""
Beteab Gebru
Compilers I - Project 2 : Take-off-Scheduler using python
10/14/2018
    This program will call the classes and functions needed to run the program.
    Our main will simply call the Airport_Driver.py with filename as argument.
"""

import sys  # this import will allow us to compile from cmd prompt with input file
from Airport_Driver import Airport_Driver as Airport_Driver  # importing our class file


if __name__ == "__main__":
    # compiling the main.py file with input .txt file as argument
    Airport_Driver1 = Airport_Driver(sys.argv[1])
    Airport_Driver1.Simulator()
