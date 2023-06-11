""" The Hierarchy of Packages """

# Demo Commands(with print() functions to show output when run as main script)

import urllib.request

# retrieve google.com home page
print(urllib.request.urlopen('http://www.google.com'))

# get the path to urllib package
print(urllib.__path__)
