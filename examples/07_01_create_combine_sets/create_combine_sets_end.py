""" Creating and Combining Sets of Friends """

college = set(['Bill', 'Katy', 'Verne', 'Dillon',
               'Bruce', 'Olivia', 'Richard', 'Jim'])

coworker = set(['Aaron', 'Bill', 'Brandon', 'David',
                'Frank', 'Connie', 'Kyle', 'Olivia'])

family = set(['Garry', 'Landon', 'Larry', 'Mark',
              'Olivia', 'Katy', 'Rae', 'Tom'])

# Demo Commands (with  print() functions to show output when run as main script)
if __name__ == '__main__':

    # display all of the items in the college set
    print(college)

    # check the number of items in each set
    print(len(college))
    print(len(coworker))
    print(len(family))

    # combine all friends into a single set
    friends = college.union(coworker, family)

    # print out friends in each set
    print(f'I have {len(college)} college buddies named:\n{college}\n')
    print(f'I have {len(coworker)} coworkers named:\n{coworker}\n')
    print(f'I have {len(family)} family friends named:\n{family}\n')
    print(f'I have {len(friends)} total friends named:\n{friends}\n')
