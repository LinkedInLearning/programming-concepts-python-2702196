""" A Brief Study in Handling Life Events """

import asyncio

def alarm():  # handler for when the alarm goes off
    print('Wake Up!')
    print('Calling the Pizza Company.\n')
    loop.call_later(1, alarm)  # schedule another alarm

def doorbell():  # handler for when the doorbell rings
    print('Ding! Dong!')
    print('Opening the door... "Thanks for bringing the pizza!"\n')

def phonecall():  # handler for when the phone rings
    print('Ring Ring!')
    print('Answering the phone... "Hello! Who is this?"\n')

loop = asyncio.get_event_loop()
loop.call_later(1, alarm)      # schedule initial alarm event
loop.call_later(4, doorbell)   # schedule doorbell event
loop.call_later(5, phonecall)  # schedule phone call event

print('Starting the event loop...\n')
loop.run_forever()  # run until stop() is called

print('The event loop stopped; closing it down.')
loop.close()
