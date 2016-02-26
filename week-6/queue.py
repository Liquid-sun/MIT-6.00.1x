#!/usr/bin/env python

"""
For this exercise, you will be coding your very first class, a Queue class.
Queues are a fundamental computer science data structure. A queue is basically
like a line at Disneyland - you can add elements to a queue, and they maintain
a specific order.
When you want to get something off the end of a queue, you get the item that 
has been in there the longest (this is known as 'first-in-first-out', or FIFO). 
You can read up on queues at Wikipedia if you'd like to learn more.

In your Queue class, you will need three methods:

__init__:
initialize your Queue (think: how will you store the queue's elements?
You'll need to initialize an appropriate object attribute in this method)

insert:
inserts one element in your Queue

remove:
removes (or 'pops') one element from your Queue and returns it.
If the queue is empty, raises a ValueError.

"""


class Queue(object):
    def __init__(self):
        self.qu = []

    def __len__(self):
        return len(self.qu)

    def __repr__(self):
        q = ','.join([str(i) for i in self.qu])
        return "Queue({})".format(q)

    def __str__(self):
        q = ','.join([str(i) for i in self.qu])
        return "[{}]".format(q)

    def insert(self, item):
        self.qu.append(item)

    def remove(self):
        if not self.qu:
            raise ValueError("Queue is empty")
        else:
            fst = self.qu[0]
            self.qu = self.qu[1:]
            return fst

        
if __name__=="__main__":
    q = Queue()
    for i in range(10):
        q.insert(i)
    print repr(q)


    for i in range(20):
        elem = q.remove()
        print("Removing: {}".format(elem))

    print repr(q)



