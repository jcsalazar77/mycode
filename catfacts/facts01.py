#!/usr/bin/python3

import requests

def main():
    """Runtime code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # the .json() method will dump a JSON string into pythonic data structures
    # this is much easier than using the urllib.request library
    print(r.json())
main()
