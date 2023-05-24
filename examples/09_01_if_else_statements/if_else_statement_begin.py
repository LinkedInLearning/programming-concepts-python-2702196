""" Ordering A Pizza That Verne Can Eat """

# things that Verne does not eat
diet_restrictions = set(['meat', 'cheese'])

# decide which pizza to order
if 'meat' in diet_restrictions:
    print('Get a cheese pizza.')

elif 'meat' and 'cheese' in diet_restrictions:
    print('Get a vegan pizza.')

else:
    print('Get something else.')
