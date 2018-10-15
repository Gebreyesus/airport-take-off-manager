#  importing the class Request to be used as a node on a linked list maintaining priority queue


"""
Beteab Gebru
Compilers I - Project 2 : Take-off-Scheduler using python
10/14/2018
This class will define a queue ADT - for the takeoff requests submitted by planes
This class defines the data structure used to implement a priority queue.
The implementation will use linked list implementation where insertion will factor in priority.
The priority will be, the time, a request is made for a time slot.
earlier requests will get the slot and others will get pushed to later open slots
"""


class Node:
    def __init__(self, payload):
        self.reqData = payload  # request object is stored as a payload
        self.next = None


class priorityQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def Enqueue(self, newReq):
        current = self.first
        newRequest = newReq
        #  temp = Node(newRequest)
        # add first node with request newRequest if queue is empty
        if current is None | self.length == 0:
            n = Node(newRequest)
            self.first = n
            self.last = n
            self.length = self.length + 1
            return
        else:
            #  otherwise: check if the new request should come first
            if prioritise(current, newRequest) & (self.length == 1):
                n = Node(newRequest)
                n.next = current
                self.first = n
                self.length = self.length + 1
            return
        self.length = self.length + 1

        #  current = current.next # moving the pointer to next node(request)
        while current.next is not None | current.next != last:
            if prioritise(current.next, newRequest):
                n = Node(newRequest)
                n.next = current
                self.first = n
                self.length = self.length + 1
            current = current.next
        # if nothing else attach it to the tail of the
        n = Node(newRequest)
        n.newRequest = newRequest
        n.next = current.next
        current.next = n
        self.last = n
        return


"""This function will simply call a printer method in the class Request to show us take-off data as time moves along"""


def Dequeue(self):
    temp = self.head
    while temp is not None:
        temp.showFlightInfo()
        temp = temp.next


""" 
@:param current : object representing the current object in the queue being checked for insertion
@:param newRequest : new request being enqueues according to priority
@returns boolean value : true if new-request holds priority over request being inspected 
"""


def prioritise(current, newReq):
        #  check for first priority : reqStart will indicate earlier takeoff requests
        if current.get_reqStart() < newReq.get_reqStart():
            return False
        else:
            if current.get_reqStart() == newReq.get_reqStart():  # if request time is occupied
                #  if requested slot is already taken check for priority#2 ->get_submissionTime
                if current.get_submissionTime < newReq.get_submissionTime:
                    return False  # return false of the current one is higher on a second priority qualifier
                else:
                    return True
            else:
                return True
