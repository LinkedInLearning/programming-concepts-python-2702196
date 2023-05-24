""" Loading the Dishwasher """

# dirty dishes in the sink
sink = ['bowl', 'plate', 'cup']

for dish in list(sink):
    print('Putting {} in the dishwasher'.format(dish))
    sink.remove(dish)

# check that the sink is empty
print(sink)
