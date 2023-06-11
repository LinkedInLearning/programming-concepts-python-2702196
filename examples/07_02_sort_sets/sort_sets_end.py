""" Sorting Friends into Sets """

# set of all friends
friends = set(['Mark', 'Rae', 'Verne', 'Richard',
               'Aaron', 'David', 'Bruce', 'Garry',
               'Bill', 'Connie', 'Larry', 'Jim',
               'Landon', 'Dillon', 'Frank', 'Tom',
               'Kyle', 'Katy', 'Olivia', 'Brandon'])

# set of people who live in my zip code
zipcode = set(['Jerry', 'Elaine', 'Cindy', 'Verne',
               'Rudolph', 'Bill', 'Olivia', 'Jim',
               'Lindsay', 'Rae', 'Mark', 'Kramer',
               'Landon', 'Newman', 'George'])

# set of people who play Munchkin
munchkins = set(['Steve', 'Jackson', 'Frank', 'Bill',
                 'Mark', 'Landon', 'Rae'])

# set of Olivia's friends
olivia = set(['Jim', 'Amanda', 'Verne', 'Nestor'])

# Demo Commands (with  print() functions to show output when run as main script)
if __name__ == '__main__':

    # choose just the friends who live nearby
    local = friends.intersection(zipcode)
    print(f'I have {len(local)} local friends named:\n{local}\n')

    # remove the Munchkin players
    invite = local.difference(munchkins)
    print(f'I have {len(invite)} friends to invite named:\n{invite}\n')

    # revise the friends to invite set
    invite = invite.symmetric_difference(olivia)
    print(f'My revised set has {len(invite)} friends named:\n{invite}\n')
