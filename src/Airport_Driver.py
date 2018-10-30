"""
Beteab Gebru
Compilers I - Project 2 : Take-off-Scheduler using python
10/14/2018
"""

# import sys as sys
import Priority_Queue as Priority_Queue
import Request as Request
# import operator


class Airport_Driver:
    def __init__(self, file_name):
        """
        This class will define all the functions and operations needed for take-off scheduling
        1. will read a file and build objects of request data type
        2. will insert each request into a Pr_Queue class
        3. The Pr_Queue will keep the requests in order of priority
        4. It will simulate a days operations using a counter as a time-keeper
        """
        self.ScheduleList = []  # will store all request data temporarily
        self.input_list = []  # A list of request objects from the input file
        self.__file_name = file_name  # Name of input file as string (i.e. "input.txt")
        self.current_queue = Priority_Queue.Priority_Queue()
        self.input_list = []

    def Simulator(self):
        """
        This method is going to run a timer to simulate a days activity
        The process of enqueueing incoming requests and dequeueing requests
        that are due to taxi.
        """
        print("======================== Start OF  the Simulator()*")
        source_list = self.input_list
        # takeoff_report = []
        # clock = 0

        # call method process_input() to read requests from file
        self.process_input()
        # CALLING  method __sort_by_priority() to sort requests by in order
        self.__sort_by_priority(source_list)
        # CALLING  method set_takeoff_time() to set take-off times
        source_list = self.set_takeoff_time(source_list)

        print("========================End of Simulation()*")

    def __sort_by_priority(self, input_list):
        """
        This method will be called with a requests list that have been read from file
        The requested start time is used as the first priority and the
        submission time is the second priority,
        - we achieve this by sorting on pr 2 first followed by sort on pr #1 (taking advantage of stable sorting)
        @ return : a list sorted according to priorities
        """
        print("========================Start of __sort_by_priority() Method *")
        # temp1 = input_list.sort(key=operator.attrgetter("submission_time"))
        # temp1 = temp1.sort(key=operator.attrgetter(str("__req_start")))

        # sending one item from list at a time to be enqueued ensuring sorted-nes
        for j in range(len(input_list)):
            self.current_queue.enqueue(input_list[j])
            # print("Enqueued the FF item from Input list :" + input_list[j].showFlightInfo())
            # print("*De-queued the FF item from Queue :" + self.current_queue.dequeue(j).showFlightInfo())
        """
           if input_list[i].get_reqStart <= self.current_queue.first.get_reqStart:
               if input_list[i].get_submissionTime <= self.current_queue.first.get_submissionTime:
                   temp = self.current_queue.first
               self.current_queue.first = input_list[i]
               self.current_queue.first.next = temp"""
        print("========================End of __sort_by_priority() Method *")


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
        @:return input_list : copy of original
        """
        print("========================Start of set_takeoff_time() Method *")
        if len(input_list) > 0:  # if list is not empty
            input_list[0].set_actualStart(max(int(input_list[0].get_actualStart()), int(input_list[0].get_reqStart())))

            for i in range(1, len(input_list)):  # from 2nd item onwards
                wait_period = input_list[i - 1].get_actualStart() + (int(input_list[i - 1].get_reqDuration()))
                input_list[i].set_actualStart(wait_period)
                
                for j in range(len(input_list)):
                    input_list[j].set_actualEnd(
                        (int(input_list[j].get_reqDuration())+int(input_list[j].get_actualStart())))
                    
        print("========================finished calc take-off times *")
        # Testing if we have adjusted actual takeoff start and end times for each flight
        Airport_Driver.display_contents(input_list)
        print("========================End of set_takeoff_time() Method *")
        return input_list

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
        print("========================Start of Process_Input() Method*")
        request_data = ["name", 0, 0, 0]  # initialing th object variables
        req_data_counter = 0  # refers to an index in a list

        with open(self.__file_name) as input_file:
            whole_file = input_file.read().splitlines()
            for i in range(len(whole_file)):
                whole_file[i] = whole_file[i].split(',')  # use comma as a delimiter
                for j in range(len(whole_file[i])):
                    whole_file[i][j] = whole_file[i][j].strip()
                    if req_data_counter < 4:  # we will break the data into units
                        request_data[req_data_counter] = whole_file[i][j]
                        req_data_counter = req_data_counter + 1
                    if req_data_counter > 3:
                        # create object, having read all values for a single req
                        new_request_object = Request.Request(request_data[0], request_data[1], request_data[2],
                                                             request_data[3])
                        self.input_list.append(new_request_object)
                        assert isinstance(new_request_object, object)  # asserting if item added is object request
                        req_data_counter = 0  # resetting index counter to start reading new request data
        print("========================file reading finished*")
        self.display_contents(self.input_list)
        print("========================End of Process_Input() Method *")

    @staticmethod
    def display_contents(CurrentList):
        """
        wE WILL CALL THIS FUNCTION TO PRINT THE LIST/QUEUE TO OBSERVE VALUES
        :param CurrentList: iT TAKES A LIST OF ITEMS AND DISPLAYS CONTENTS OF IT
        :return: nO VALUE IS RETURNED.
        """

        print("========================Start of display_contents() Method*")
        print("The number of items in list are :" + str(len(CurrentList)))
        print("----- Fl.ID--- ||sub_T|| reqStart||Dur ||Start||End")
        # Flight ID||sub_Time||reqStart||reqDuration||actualStart||actualEnd")
        for j in range(len(CurrentList)):
            print(str(j) + ": " + CurrentList[j].showFlightInfo())
        print("========================END of display_contents() Method *")