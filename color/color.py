#!/usr/bin/python3

import crayons

def main():
    """Runtime code. Always indent a function"""
    #print red string in red
    print(crayons.red('red string'))

    # red, white, and blue text
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))
    

    crayons.disable() #disables the crayon package
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.DISABLE_COLOR = False #enable the crayons package

    # This line will print in color because color is enabled
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

##We must call our main functionor our code will not run
main()

