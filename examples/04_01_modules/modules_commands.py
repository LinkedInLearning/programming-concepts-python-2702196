""" The Right Tools for the Job """

# Demo Commands(with print() functions to show output when run as main script)

# import the entire random module
import random
print(random.randint(1,20))
# randint(1,20) # causes an error

# import just the randint function
from random import randint
print(randint(1,20))
print(random.random())

# import just the random function
from random import random
print(random())
# random.randint(1,20) # causes an error

# import the entire random module as "random"
import random as rand
print(rand.randint(1,20))
print(random())
