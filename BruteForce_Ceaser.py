#!/usr/bin/python3.10
import sys

text = sys.argv[1]
#s = int (sys.argv[2])
if text.isupper():
   text = text.lower()
def decrypt(text,s):
    result = ""

    #traverse the plain text

    for i in range(len(text)):
        char = text[i]

        #Encrypt lowercase characters in plain text
        # Checking for white spaces
        if ord(char)==32:
           result = result + " "
        else:
           result += chr((ord(char) - s - 97) % 26 + 97)

    print ("Key[",s,"]:",result)
    return result

#check the above function
print ("Cipher text: " + text)
for s in range(1,27):
  a=decrypt(text,s)
  s=s+1
#print ("Shift pattern: "+ str(s))
#print ("Plain text: " + decrypt(text,s).upper())
