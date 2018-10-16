
"""
Beteab Gebru
Compilers I - Project 2 : Take-off-Scheduler using python
10/14/2018
This class will define a queue ADT - for the takeoff requests submitted by planes
This class defines the data structure used to implement a priority queue.
The implementation will use list implementation where insertion will factor in priority.
The priority will be, the time, a request is made for a time slot.
earlier requests will get the slot and others will get pushed to next in line
"""

import Request as Request


class priorityQueue:
    def __init__(self):
        self.scheduleList[1000]  # list able to store max take-offs in a day
        self.first = None
        self.last = None
        self.length = 0          # number of requests loaded today

    def sizeOfQueue(self):
        return self.length
    def getfirst(self):
        return self.first
    def getlast(self):
        return self.last

    """ 
    @:param current : object representing the current object in the queue being checked for insertion
    @:param newRequest : new request being enqueues according to priority
    @returns boolean value : true if new-request holds priority over request being inspected 
    """
    def Enqueue(self, newReq):
        current = self.first
        if current is None | self.length == 0:  # enqueue first request with request newRequest if queue is empty
            self.first = newReq
            self.last = newReq
            self.length = self.length + 1
            return
        if self.length > 0 :
            if :  # if new item is higher priority than current
                self.first = n
                self.length = self.length + 1
            return
        else:
        self.length = self.length + 1

        #  current = current.next # moving the pointer to next node(request)
        if self.comparePriority(self, current.next, newReq):
            n = Node(newReq)
            n.next = current
            self.first = n
            self.length = self.length + 1
            current = current.next
        # if nothing else attach it to the tail of the
        n = Node(newReq)
        n.newRequest = newReq
        n.next = current.next
        current.next = n
        self.last = n
        return

    """
    This method/function will compare the new request with a node from the linked-list queue
    :param current: represents the current node being examined
    :param newReq:  represents the node being inserted/enqueued
    :returns boolean True if the new item is of higher priority hence needing insertion
    """
    @staticmethod
    def comparePriority(current, newReq):
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
    """This function will simply call a printer method in the class Request to show us take-off data against time"""

    def Dequeue(self, indx):  # will traverse the linked list in its current state from first to last
        if indx is not None:
            return self.