# Name: Kevin Nakashima
# Class: CPSC 223P
# Date: 02/07/2017
# File: Text2Binary.py
# converts a string to binary
#Imports=======================================================================

#T2B===========================================================================
def T2B(text):
    binary = []
    for letter in text:
        binary.append(bin(ord(letter))[2:].zfill(8))

    print(*binary, sep=" ")
#MAIN==========================================================================
def main():
    text = input("Please enter a string: ")
    T2B(text)
              
main()
#==============================================================================

