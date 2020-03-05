#!/usr/bin/python3

import requests

def main():
    """Runtime code"""
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    #display the methods available to our new object
    print( dir(r) )
main()
