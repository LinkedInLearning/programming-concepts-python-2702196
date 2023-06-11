""" A Garage Full of Classy Vehicles """

# Base Vehicle class
class Vehicle:
    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.gas = 4  # a full tank of gas

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print(f'The {self.color} {self.manufacturer} goes VROOOM!!!')
        else:
            print(f'The {self.color} {self.manufacturer} sputters out of gas...')

# Car inherits the Vehicle class
class Car(Vehicle):
    def radio(self):  # turn on the radio
        print("Rockin' Tunes!")

    def window(self):  # open the window
        print('Ahhh... fresh air!')

# Motorcycle inherits the Vehicle class
class Motorcycle(Vehicle):
    def helmet(self):  # put on a helmet
        print('Helmet on - nice and safe!')
