""" Trying to Download Things That Don't Exist """

import urllib.request

webpage = urllib.request.urlopen('http://www.google.com')

for line in webpage:
    print(line)
