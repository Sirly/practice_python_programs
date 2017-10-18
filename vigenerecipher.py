#   File: vigenerechipher.py
#   Kevin Nakashima
#   2/14/2017
#   Takes a file name and code word/phrase.
#       Program will encode contents of file.
#       contents will output to another textfile.
#==============================================================================
#   IMPORTS
import string
import re

def main():
    #declare and initialize arrays
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    #convert array to list for negative indexing
    upper = list(upper)
    lower = list(lower)
    #get file name
    fName = input("Enter the file name to encrypt: ")
    #get key
    key = input("Enter a key: ")
    #make key lowercase
    key = key.lower()
    #strip of all whitespace
    key = key.replace(' ', '')
    #strip of all non alphabetical characters
    regex = re.compile('[^a-zA-Z]')
    key = regex.sub('', key)
    keyLen = len(key)
    #open file to read
    inFile = open(fName, 'r')
    #truncate fName after '.' for outFile name
    fName = fName.split('.')
    fName = fName[0]
    #open file to write
    outFile = open(fName + "-cipher.txt", 'w')
    #string processing
    while True:
        data = []
        data = inFile.readline()
        if data == '':
            inFile.close()
            break
        index = 0
        newData = []
        for i in range(len(data)):
            if 65 <= ord(data[i]) and ord(data[i]) <= 90:
                newData.append(upper[(ord(data[i]) - 65) - (ord(key[index])-97)])
                index += 1
                index %= keyLen
            elif 97 <= ord(data[i]) and ord(data[i]) <= 122:
                newData.append(lower[(ord(data[i]) - 97) - (ord(key[index])-97)])
                index += 1
                index %= keyLen
            else:
                newData.append(data[i])
        outFile.write(''.join(newData))

    #open file to write encrypted data
    outFile.close()
    
    print("Encrypted file was saved to " + fName + "-cipher.txt")

main()
