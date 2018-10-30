"""
Beteab Gebru
Compilers I - Project 2 : Take-off-Scheduler using python
10/14/2018
This ADT defines a Request, which is a request made by planes to reserve the runway for takeoff
"""


class Request:
    def __init__(self, name, subtime, reqstart, reqduration):
        """
        his ADT defines a Request, which is a request made by planes to reserve the runway for takeoff
        """
        self.__flight_ID = name  # name of requesting plane/flight
        self.__req_duration = reqduration  # How long will the plane be on the runway
        self.__actual_start = 0  # Actual time-slot provided by scheduler
        self.__actual_end = 0  # Exit timestamp for the tak-off
        self.__submission_time = subtime  # Time stamp when request is submitted
        self.__req_start = reqstart  # When does the plane want to takeoff
        self.next = None  # Stores value of the next flight
        self.prev = None                    # stores the index of the prev flight
        # print('Done With __init function -->Request class')  # Debug line *******************************

    def showFlightInfo(self):
        """
        This function will return well formatted info on a particular takeoff
        @:return String : Format{ flightID, submissionTime, reqStart, reqDuration, actualStart, actualEnd }
        """
        return (" :{" + self.__flight_ID + "} -  {" + str(self.__submission_time) + "} - {" + str(self.__req_start) +
                "} - {" + str(self.__req_duration) + "} - {" + str(self.__actual_start) +
                "} - {" + str(self.__actual_end) + "}")

    def __repr__(self):
        return '{} : {} : {}: {} : {}: {} '.format(self.__flight_ID, self.__submission_time, self.__req_start,
                                                   self.__req_duration, self.__actual_start, self.__actual_end)

    #  ------------------------------------------------------getter functions
    def get_submissionTime(self):
        """
        @:return submissionTime -the time stamp when request comes in(used to prioritise request)
        """
        return self.__submission_time

    def get_reqStart(self):
        """
        @:return reqStart - the new start time allotted by scheduler
        """
        return self.__req_start

    def get_actualStart(self):
        """
        @:return actualStart - time plane starts to use resource
        """
        return self.__actual_start

    def get_flightID(self):
        """
        @:return flightID - flight identifier is returned
        """
        return self.__flight_ID

    def get_actualEnd(self):
        """
        @returns the actual end time
        """
        return self.__actual_end

    def get_reqDuration(self):
        """
        Returns the amount of time resource is requested for
        """
        return self.__req_duration

    #  ------------------------------------------------------setter functions

    def set_actualStart(self, start):
        """
        @:param start - sets the actual start data attribute (changed by scheduler)
        """
        self.__actual_start = start

    def set_actualEnd(self, end):
        """
        @:param end - used to set the data attribute(changed by scheduler)
        """
        self.__actual_end = end

    """
    def set_nextFlight(self, Nxt):
        
        @:param Nxt - used to set the data attribute(changed by scheduler)
       
        self.next = Nxt
        """

    """    
    def set_prevFlight(self, Prv):
        @:param Prv - used to set the data attribute(changed by scheduler)
        self.__prev = Prv
        """
