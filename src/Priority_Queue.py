"""
Beteab Gebru
Compilers I - Project 2 : Take-off-Scheduler using python
10/14/2018

This class defines a priority queue data structure,
"""


class Priority_Queue:
    def __init__(self):
        self.Queue = []
        self.first = 0  # stores the first item in the current queue
        self.last = 0  # stores the last item in current queue
        self.length = len(self.Queue)  # length of queue
        print(":Created a Queue : length " + str(self.length))  # debugging line

    def enqueue(self, new_item):
        """
        this method will take a new item(request() type.
        it will walk through the list Queue[] and insert it.
        we utilise the 'next' and 'prev' to create a linked list of requests in right order
        :param new_item: a request sent to be enqueued
        :return: no return is made
        """

        # insert it at index 0 if queue is empty
        if self.empty():
            self.first = new_item
            self.last = new_item
            self.Queue.append(new_item)  # append item to queue and proceed to sort
        else:
            for i in range((len(self.Queue)-1)):

                # if new item must be in first position of the queue
                if new_item.get_reqStart() <= self.first.get_reqStart():
                    if new_item.get_submissionTime() < self.first.get_submissionTime():
                        new_item.next = self.first  # set next attrib of new req, to the old first
                        self.first = new_item       # the new item is new first of the queue
                        break
                # if new item needs to be in the last index
                elif new_item.get_reqStart() >= self.last.get_reqStart():
                    if new_item.get_submissionTime() >= self.last.get_submissionTime():
                        # make the new item last and alter the request.next attrib
                        self.last.next = new_item  #
                        self.last = new_item
                        break

    def dequeue(self, item_index):
        """
            this method will be called to remove the first item in queue
        :return: item being removed from the front of the queue. accessed using index
        """
        return self.Queue[item_index]

    def empty(self):
        """
        this method returns true is queue is empty
        :return: bool - true is length is 0
        """
        return self.length == 0
