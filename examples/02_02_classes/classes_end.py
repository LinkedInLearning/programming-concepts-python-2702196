""" The Blueprints for Jeans """

class Jeans:
    def __init__(self, waist, length, color):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False

    def put_on(self):
        print(f'Putting on {self.waist}x{self.length} {self.color} jeans')
        self.wearing = True

    def take_off(self):
        print(f'Taking off {self.waist}x{self.length} {self.color} jeans')
        self.wearing = False

# Demo Commands(with print() functions to show output when run as main script)
if __name__ == '__main__':

    # create and examine a pair of jeans
    my_jeans = Jeans(31, 32, 'blue')
    print(type(my_jeans))
    print(dir(my_jeans))

    # don and remove the jeans
    my_jeans.put_on()
    print(my_jeans.wearing)

    my_jeans.take_off()
    print(my_jeans.wearing)
