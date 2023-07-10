""" I'll Have the Special! """

def order_special(day):
    match day:
        case 'Sunday':
            return 'spinach pizza'
        case 'Monday':
            return 'mushroom pizza'
        case 'Tuesday':
            return 'pepperoni pizza'
        case 'Wednesday':
            return 'veggie pizza'
        case 'Thursday':
            return 'bbq chicken pizza'
        case 'Friday':
            return 'sausage pizza'
        case 'Saturday':
            return 'Hawaiian pizza'

today = 'Tuesday'
special = order_special(today)
print(f'\nToday is {today}, and the special is {special}.\n')
