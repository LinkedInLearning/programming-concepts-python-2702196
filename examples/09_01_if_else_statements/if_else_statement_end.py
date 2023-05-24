""" Ordering A Pizza That Verne Can Eat """

# things that Verne does not eat
diet_restrictions = set(['meat', 'cheese'])

# decide which pizza to order
if 'meat' and 'cheese' in diet_restrictions:
    print('Get a vegan pizza.')

elif 'meat' in diet_restrictions:
    print('Get a cheese pizza.')

else:
    print('Get something else.')
