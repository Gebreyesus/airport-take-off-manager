"""
Beteab Gebru
Compilers I - Project 2 : Take-off-Scheduler using python
10/14/2018

This class defines a priority queue data structure, using heapq from python library
"""
import Request
import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    """
    method takes a new item and uses 1st and 2nd priority attributes to insert it

    The heappush method from heapq is called with the list that stores the queue and then a tuple with the primary and
    secondary priorities, the index and the item to be pushed. The heappush method uses the primary priority first, the
    secondary priority next and finally the index to order the items. No two items will ever have the same index so this
    value is the tie breaker in the case that the primary and secondary priorities are the same for two or more items
    added to the queue. The item with the lowest priority is at the top of the queue (will be popped first). After the
    item is added to the queue, the index is incremented.
    """

    def enqueue(self, item, req_start, submission_time):
        heapq.heappush(self.__q, (req_start, submission_time, self.index, item))
        self.index += 1

    """
    Uses the heapq heappop method to return the smallest item in the queue (with the lowest priority).

    This function returns the last item in the tuple that is returned by heappop because heappop doesn't necessarily
    know how many priorities you have defined. The last item in this tuple is always the item added to the queue.
    """

    def dequeue(self):
        return heapq.heappop(self.queue)[-1]

    """
        checks if queue length is zero
        returns true if queue is empty, false otherwise

    """

    def empty(self):
        return len(self.queue) == 0
