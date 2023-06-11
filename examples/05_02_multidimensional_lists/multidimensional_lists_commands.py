""" A 3-Dimensional Valet Service """

# 2D list of lists - index cars by row, spot
lot_2d = [['Toyota', 'Audi', 'BMW'],  # 0th row
          ['Lexus', 'Jeep'],         # 1st row
          ['Honda', 'Kia', 'Mazda']]  # 2nd row

# 3D list of lists of lists - index cars by floor, row, spot
lot_3d = [[['Telsa', 'Fiat', 'BMW'],  # 0th floor
           ['Honda', 'Jeep'],
           ['Saab', 'Kia', 'Ford']],
          [['Subaru', 'Nissan'],     # 1st floor
           ['Volvo']],
          [['Mazda', 'Chevy'],       # 2nd floor
           [],
           ['Volkswagen']]]

""" Demo Commands (with  print() functions to show output when run as main script) """
if __name__ == '__main__':

    # indexing 2D lists
    print(lot_2d)        # 2D list of parking lot
    print(lot_2d[2])     # 1D list of cars in row 2
    print(lot_2d[2][1])  # car parking in row 2, spot 1

    # indexing 3D lists
    print(lot_3d)           # 3D list of multi-story garage
    print(lot_3d[0])        # 2D list of cars on floor 0
    print(lot_3d[0][2])     # 1D list of cars on floor 0, row 2
    print(lot_3d[0][2][1])  # car parked on floor 0, row 2, spot 1

    # accessing all cars in the multi-story garage
    for floor in lot_3d:     # cycle through each floor in the multi-story garage
        for row in floor:    # cycle through each row in the floor
            for car in row:  # cycle through each car in the row
                print(car)
