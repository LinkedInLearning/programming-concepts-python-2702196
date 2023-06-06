""" Polling for Pizza Because I'm Hungry! """

import time

hungry = True  # I need a pizza!

while hungry:
    print('Opening the front door')
    front_door = open('front_door.txt', 'r', encoding='utf-8')

    if 'Delivery Person' in front_door:
        print('The pizza is here!!!!!!!!!!')
        hungry = False
    else:
        print('Not yet...')

    print('Closing the front door.\n')
    front_door.close()

    time.sleep(1)  # rest for 1 second
