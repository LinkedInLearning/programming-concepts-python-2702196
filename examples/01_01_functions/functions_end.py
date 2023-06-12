""" A Functional Breakfast """

def make_omelette():
    print('Mixing the ingredients')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side\n')
    omelette = 'a tasty omelette'
    return omelette

# make breakfast for two
barron_breakfast = make_omelette()
olivia_breakfast = make_omelette()
print(f'Barron is having {barron_breakfast}\n')
print(f'Olivia is having {olivia_breakfast}\n')
