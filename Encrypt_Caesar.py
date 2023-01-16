#!/usr/bin/python3.10
import sys

text = sys.argv[1]
s = int (sys.argv[2])
def encrypt(text,s):
    result = ""

    #traverse the plain text

    for i in range(len(text)):
        char = text[i]

        #Encrypt lowercase characters in plain text
        # Checking for white spaces
        if ord(char)==32:
           result = result + " "
        else:
           result += chr((ord(char) + s - 97) % 26 + 97)

    return result

#check the above function
print ("Plain text: " + text)
print ("Shift pattern: "+ str(s))
print ("Cipher: " + encrypt(text,s).upper())
