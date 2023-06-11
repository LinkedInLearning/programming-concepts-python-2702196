""" A Stack of Bills to Pay """

# Demo Commands (with  print() functions to show output when run as main script)

# create a list to use as the stack
stack = list()

# add some bills to the stack
stack.append('bill1')
stack.append('bill2')

# remove the top bill to pay it
print(stack.pop())

# add two more bills to the stack
stack.append('bill3')
stack.append('bill4')

# remove bills from top to bottom
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.pop()  # causes Indexerror exception
