"""
Beteab Gebru
Compilers I - Project 2 : Take-off-Scheduler using python
10/14/2018

This class will define all the functions and operations needed for take-off scheduling
    1. will read a file and build objects of request data type
    2. will insert each request into a Pr_Queue class
    3. The Pr_Queue will keep the requests in order of priority
    4. It will simulate a days operations using a counter as a time-keeper
"""
import Pr_Queue
import Request as Request


class Airport_Driver:
    def __init__(self, Filename):
        self.inputList = []          # will store all request data temporarily
        self.fileName = Filename     # Name of input file as string (i.e. "input.txt")

        """
        In this function we will take assumptions listed below.
            1. the file format selected is in .txt format 
            2. each line of text contains the flight request data in the following order
                { flightID, submissionTime, reqStart, reqDuration, actualStart, actualEnd }
        The scanner will read the file a line at a time. 
        It'll instantiate a request object with relevant data read from a line of info.
        It'll enqueue every object by passing it as a parameter to the Pr_Queue class method that inserts new objects        
        """
    def __process_input(self):

        with open(self.fileName) as input_file:
            whole_file = input_file.read().splitlines()
            for i in range(len(whole_file)):
                whole_file[i] = whole_file[i].split(',')
                for j in range(len(whole_file[i])):
                    whole_file[i][j] = whole_file[i][j].strip()

        for item in whole_file:
            self.inputList.append((item[0], int(item[1]), int(item[2]), int(item[3])))
            anotherRequest = Request.ConstructRequest(item[0], int(item[1]), int(item[2]), int(item[3]))
            Pr_Queue.priorityQueue.Enqueue(anotherRequest)



