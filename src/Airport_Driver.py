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
import sys as sys
import Pr_Queue as Pr_Queue
import Request as Request


class Airport_Driver:
    def __init__(self, file_name):
        self.ScheduleList = []          # will store all request data temporarily
        self.input_list = []            # A list of request objects from the input file
        self.__file_name = file_name    # Name of input file as string (i.e. "input.txt")
        self.__file_name = "Scheduling.txt"

    print('Done With __init function -->Airportdriver')   # Debug line *******************************

    """
    In this function we will take assumptions listed below.
        1. the file format selected is in .txt format 
        2. each line of text contains the flight request data in the following order
            { flightID, submissionTime, reqStart, reqDuration}
        When program simulates a run there will be new values for actual takeoff times
            { flightID, submissionTime, reqStart, reqDuration, actualStart, actualEnd }
    The scanner will read the file a line at a time. 
    It'll instantiate a request object with relevant data read from a line of info.
    It'll enqueue every object by passing it as a parameter to the Pr_Queue class method that inserts new objects        
    """
    def process_input(self):
            request_data = ["name", 0, 0, 0]
            req_data_counter = 0
            with open(self.__file_name) as input_file:
                whole_file = input_file.read().splitlines()
                print('Opened file to read the file********************')  # Debugging line
                # days_takeoff_list = Pr_Queue(len(whole_file))  # creating queue sized number of lines in file
                for i in range(len(whole_file)):
                    whole_file[i] = whole_file[i].split(',')    # use comma as a delimiter
                    for j in range(len(whole_file[i])):
                        whole_file[i][j] = whole_file[i][j].strip()
                        #  print("Data outer-loop: " + whole_file[i][j])   # Debugging line
                        if req_data_counter > 3:
                            # create object, having read all values for a single req
                            new_request_object = Request.Request(request_data[0], request_data[1], request_data[2],
                                                                 request_data[3])
                            print("Requests Data : " + new_request_object.get_flightID() + " : ")
                            print(new_request_object.showFlightInfo())

                            # new_request_object
                            req_data_counter = 0  # resetting index counter to start reading new request data
                        if req_data_counter < 4:    # we will break the data into units
                            #  print("Data inner-loop: " + whole_file[i][j])   # Debugging line
                            request_data[req_data_counter] = whole_file[i][j]
                            req_data_counter = req_data_counter + 1
                    # days_takeoff_list(newreq)
                    # print('Done With process_input function') # Debugging line
