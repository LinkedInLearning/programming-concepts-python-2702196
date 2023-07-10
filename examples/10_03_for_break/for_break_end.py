""" Putting Away Clean Dishes """

import random

# 20 clean dishes in dishwasher
dishwasher = ['plate', 'bowl', 'cup', 'knife', 'fork',
              'spoon', 'plate', 'spoon', 'bowl', 'cup',
              'knife', 'cup', 'cup', 'fork', 'bowl',
              'fork', 'plate', 'cup', 'spoon', 'knife']

for dish in list(dishwasher):
    # check space left in cabinet
    if not random.randint(0, 19):
        print('Out of space!')
        break
    else:
        print(f'Putting {dish} in the cabinet')
        dishwasher.remove(dish)
