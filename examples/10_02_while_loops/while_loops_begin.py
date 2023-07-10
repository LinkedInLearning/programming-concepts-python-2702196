""" Scrubbing A Stuborn Pan """

import random

dirty = True  # state of the pan
scrub_count = 0  # number of scrubs

while dirty:
    scrub_count += 1
    print(f'Scrubbed the pan {scrub_count} times.')

    print('Rinsing to check if the pan is clean...\n')

    if not random.randint(0, 9):
        print('All clean!')
        dirty = False
    else:
        print('Still dirty...')
