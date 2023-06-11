""" You Can Change an Outfit, But You Can't Change Your Words """

# Demo Commands(with print() functions to show output when run as main script)

# create a closet full of clothes
closet = ['shirt', 'hat', 'pants', 'jacket', 'socks']
print(closet)
print(id(closet))

# remove a hat
closet.remove('hat')
print(closet)
print(id(closet))

# create a poor choice of words
words = "You're wearing that"
print(words)
print(id(words))

# add more to the phrase
words = words + ' because you look great!'
print(words)
print(id(words))
