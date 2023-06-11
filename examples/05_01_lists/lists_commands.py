""" Parking Cars in a List """

# Demo Commands(with print() functions to show output when run as main script)

# create the initial list of cars
row = ['Ford', 'Audi', 'BMW', 'Lexus']

# park a Mercedes at the end of the row
row.append('Mercedes')
print(row)
print(row[4])

# swap a BMW at index 2 for a Jeep
row[2] = 'Jeep'
print(row)

# park a Honda at the end of the row
row.append('Honda')
print(row)
print(row[4])

# park a Kia at the front of the row
row.insert(0, 'Kia')
print(row)
print(row[4])

# find the Mercedes and leave the list
print(row.index('Mercedes'))
print(row.pop(5))
print(row)

# find and remove a Lexus
row.remove('Lexus')
print(row)
