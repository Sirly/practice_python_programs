# Name: Kevin Nakashima
# Class: CPSC 223P
# Date: 02/07/2017
# File: Binary2Text.py
# converts a binary set to a string
#Imports=======================================================================

#T2B===========================================================================
def Bin2Text(binary):
    text = []
    for set in binary:
        text.append(chr(int(set, 2)))

    print(*text, sep = '')
#MAIN==========================================================================
def main():
    binary = input("Please enter binary: ")
    binaryList = binary.split(' ')
    Bin2Text(binaryList)
              
main()
#==============================================================================
