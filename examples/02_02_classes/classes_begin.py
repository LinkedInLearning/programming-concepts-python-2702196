""" The Blueprint for Jeans """

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
