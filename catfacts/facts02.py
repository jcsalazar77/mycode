#!/usr/bin/python3

import requests

def main():
    """Runtime code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # the .json() method will dump a JSON string into pythonic data structures
    # this is much easier than using the urllib.request library
    print(r.json())
    print("\n\n\n")

    # if we request the 'all' key, we can strip off the outside {}
    #This seems minor, but is CRITICAL if we want to parse our data
    print(r.json().get("all"))

main()
