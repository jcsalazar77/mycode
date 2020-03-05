#!/usr/bin/python3

import urllib.request
import re

print("Where should we search?")
url = input()

print("Great! So we'll try to open this url " +str(url) + " to search for the phrase:")

searchFor = input()
searchMe = urllib.request.urlopen(url).read().decode("utf-8")
while re.search(searchFor, searchMe):
    print("Found a match!")
    keep_going = input("\nWould you like to try another search? Enter to continue, or enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break
    else:
        print("No match")

