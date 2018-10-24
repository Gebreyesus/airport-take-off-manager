"""
Beteab Gebru
Compilers I - Project 2 : Take-off-Scheduler using python
10/14/2018

This class will define all the functions and operations needed for take-off scheduling
    1. will read a file and build objects of request data type
    2. will insert each request into a Pr_Queue class
    3. The Pr_Queue will keep the requests in order of priority
    4. It will simulate a days operations using a the time counter
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

    def process_input(self):
        """
            In this function we will take assumptions listed below.
                1. the file format selected is in .txt format
                2. each line of text contains the flight request data in the following order
                    { flightID, submissionTime, reqStart, reqDuration}
                When program simulates a run there will be new values for actual takeoff times
                    { flightID, submissionTime, reqStart, reqDuration, actualStart, actualEnd }
            The scanner will read the file a line at a time. separated by a comma, at a time.
            It'll instantiate a request object with relevant data read from a line of text.
            It'll simply populate the list with Request objects
            """
        request_data = ["name", 0, 0, 0]
        req_data_counter = 0
        with open(self.__file_name) as input_file:
            whole_file = input_file.read().splitlines()
            for i in range(len(whole_file)):
                whole_file[i] = whole_file[i].split(',')  # use comma as a delimiter
                for j in range(len(whole_file[i])):
                    whole_file[i][j] = whole_file[i][j].strip()
                    #  print("Data outer-loop: " + whole_file[i][j])   # Debugging line
                    if req_data_counter < 4:  # we will break the data into units
                        # print("Data inner-loop: " + whole_file[i][j])   # Debugging line
                        request_data[req_data_counter] = whole_file[i][j]
                        req_data_counter = req_data_counter + 1

                    if req_data_counter > 3:
                        # create object, having read all values for a single req
                        new_request_object = Request.Request(request_data[0], request_data[1], request_data[2],
                                                             request_data[3])
                        self.input_list.append(new_request_object)
                        assert isinstance(new_request_object, object)  # asserting if item added is object request
                        # print(new_request_object.showFlightInfo())   # Debugging line
                        req_data_counter = 0  # resetting index counter to start reading new request data

            # Testing if we have read the requests properly
            print("the number of items in list are :" + str(len(self.input_list)))
            for req in range(len(self.input_list)):
                print(str(req) + self.input_list[req].showFlightInfo())

    @staticmethod
    def set_takeoff_time(input_list):
        """
        This method will be called with a list parameter, that has been sorted with order of priority in mind.
        It will parse through the list and set the actual start and ened of take off times
        # we shall start on the first index in the list, set its actual start time
        # we set the actual start time by looking at previous takeoff duration and
        # push takeoff time if prev take-off is still on
           else:  # else let plane takeoff at its current set time
        # set end times by looking takeoff durations
        ->Having made the adjustments it'll return the a list with full set of values
        @:return input_list : copy of orginal
        """
        print("***Entered time setter function")  # Debugging line
        if len(input_list) > 0:
            input_list[0].set_actualStart(max(int(input_list[0].get_actualStart()), int(input_list[0].get_reqStart())))
            for i in range(1, len(input_list)):
                print("int the for loop")
                wait_period = input_list[i - 1].get_actualStart() + (int(input_list[i - 1].get_reqDuration()))
                if (int(input_list[i].get_reqStart())) < wait_period:
                    newstart = wait_period + input_list[i].get_reqStart()
                    print("cant start while others are taxiing -> adjust takeoff start -> new start is " + newstart)
                    input_list[i].set_actualStart(wait_period)
                else:
                    input_list[i].set_actualStart(input_list[i].get_actualStart())

                # print("Observing changes " + input_list[i].showFlightInfo() + str())
            for i in range(len(input_list)):
                input_list[i].set_actualEnd(int(input_list[i].get_reqDuration()+input_list[i].get_actualStart()))

        # Testing if we have adjusted actual takeoff start and end times for each flight
        print("the number of items in list are :" + str(len(input_list)))
        for req in range(len(input_list)):
            print(str(req) + input_list[req].showFlightInfo())

        return input_list

    @staticmethod
    def __sort_by_priority(input_list):
        """
        This method will be called with a requests list that have been read from file
        The requested start time is used as the first priority and the
        submission time is the second priority,
        - we achieve this by sorting on pr 2 first followed by sort on pr #1 (taking advantage of stable sorting)
        @ return : a list sorted according to priorities
        """
        # temp = input_list.sort(key=operator.attrgetter('__submission_time'))
        # input_list.sort(key=operator.attrgetter('__req_start'))
        return input_list
