""" A Queue of Groceries to Put Away """

# Demo Commands (with  print() functions to show output when run as main script)

# create a new queue object
import queue
q = queue.Queue()
print(q.empty())

# put bags into the queue
q.put('bag1')
print(q.empty())
q.put('bag2')
q.put('bag3')

# get bags from the queue in FIFO order
print(q.get())
print(q.get())
print(q.get())
# q.get() # causes an error; use CTRL+C to

# create a new queue to hold two items
q2 = queue.Queue(maxsize=2)
print(q2.empty())

# put two bags into the two-item queue
q2.put('bag1')
print(q2.full())
q2.put('bag2')
print(q2.full())

# try to put an extra bag into the queue
q2.put_nowait('bag3')  # causes an error
