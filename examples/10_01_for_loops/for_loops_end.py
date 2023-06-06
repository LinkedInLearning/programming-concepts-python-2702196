""" Loading the Dishwasher """

# dirty dishes in the sink
sink = ['bowl', 'plate', 'cup']
print(f'\nThere are {len(sink)} dishes in the sink: {sink}\n')

for dish in list(sink):
    print(f' - Put a {dish} in the dishwasher')
    sink.remove(dish)

# check that the sink is empty
print(f'\nThere are {len(sink)} dishes in the sink: {sink}\n')
