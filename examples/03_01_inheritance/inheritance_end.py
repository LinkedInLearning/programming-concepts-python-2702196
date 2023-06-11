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


# Demo Commands(with print() functions to show output when run as main script)
if __name__ == '__main__':
    
    # create car & motorcycle objects
    my_car = Car('red', 'Mercedes')
    my_mc = Motorcycle('silver', 'Harley')

    # take them out for a test drive
    my_car.drive()
    my_mc.drive()
    my_mc.drive()
    my_mc.drive()
    my_mc.drive()
    my_mc.drive()  # out of gas
    my_car.drive()

    # play around with accessories
    my_car.radio()
    my_car.window()
    my_mc.helmet()
    # my_mc.window() # windows do not exist on motorcycles - throws and error
