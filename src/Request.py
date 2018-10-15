"""
Beteab Gebru
Compilers I - Project 2 : Take-off-Scheduler using python
10/14/2018

This ADT defines a Request, which is a request made by planes to reserve the runway for takeoff
"""


class Request_Node:

    def __init__(self, name, subtime, reqstart, reqduration):
        self.flightID = str(name)                 # name of requesting plane/flight
        self.reqDuration = int(reqduration)       # How long will the plane be on the runway
        self.actualStart = 0                      # Actual time-slot provided by scheduler
        self.actualEnd = 0                        # Exit timestamp for the tak-off
        self.submissionTime = int(subtime)        # Time stamp when request is submitted
        self.reqStart = int(reqstart)             # When does the plane want to takeoff

    """
    @:return an arbitrary string containing the request data 
    """
    def showFlightInfo(self):
        return " :||-- " + self.flightID + " -- " + str(self.submissionTime) + " -- " + str(self.reqStart) + " -- "\
               + str(self.reqDuration) + " -- " + str(self.actualStart) + \
               " -- " + str(self.actualEnd) + " --||"

    """
     @:return __sub_time -the time stamp when request comes in(used to prioritise request)
    """
    def get_sub_time(self):
        return self.submissionTime

    """
    @:return reqStart - the new start time allotted by scheduler
    """
    def get_req_start(self):
        return self.reqStart

    """
    @:return actualStart - time plane starts to use resource
    """
    def get_actual_start(self):
        return self.actualStart

    """
    @:return __flightID - flight identifier is returned 
    """
    def get_id(self):
        return self.flightID

    """
    @returns the actual end time 
    """
    def get_actual_end(self):
        return self.actualEnd

    """
    Returns the amount of time resource is requested for
    """
    def get_req_duration(self):
        return self.reqDuration

    """
    @:param start - sets the actual start data attribute (changed by scheduler)
    """
    def set_actual_start(self, start):
        self.actualStart = start

    """
    @:param end - used to set the data attribute(changed by scheduler)
    """
    def set_actual_end(self, end):
        self.actualEnd = end
