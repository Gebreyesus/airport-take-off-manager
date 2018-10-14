# This program will call the classes and functions needed
# to drive the program and we will call necessary classes and methods from here
# the main will read from a file named Scheduling.txt all the attributes of request

import sys  # this import will allow us to compile from cmd prompt with input file
import Takeoff_Request  # importing our class file

if __name__ == "__main__":
    rp = Takeoff_Request.Req_Process(sys.argv[1])
    rp.run()