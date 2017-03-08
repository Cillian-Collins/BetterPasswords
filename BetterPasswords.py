#Python Password Generator Version 1.01

#Imports
from random import randint
import subprocess as sp

#Copyrights
print("+=====================================================================================================================+")
print("|                                                                                                                     |")
print("|                                                  BETTER PASSWORDS                                                   |")
print("|                                                 by Cillian Collins                                                  |")
print("|                                                                                                                     |")
print("+=====================================================================================================================+")

#Input
word = str(raw_input('Enter your password here: '))

#Alpha only and less than 6 character long loop
while len(word) < 6 or not word.replace(' ', '').isalpha():
    #Check if less than 6 characters
    if len(word) < 6:
        #If less than 6 characters, print the error
        print("Please enter a word larger than 6 characters long!")
    else:
        #If more than 5 characters it must not be letters only, so print the error
        print("Please enter letters only!")
    #If it threw an error, prompt the user to fix the input error
    word = raw_input('Enter your password here: ')

#Formula for the password generator saved as variable
password = '#' + word + str(randint(1000,9999))
#Prints the variable
print (password)
#Saves a passwords.txt file
with open('passwords.txt', 'wb') as file:
    #Writes the 'password' variable to the file
    file.write(password)

#Sets variable for notepad.exe
programName = "notepad.exe"
#Sets variable for passwords.txt
fileName = "passwords.txt"
#Opens passwords.txt in notepad.exe
sp.Popen([programName, fileName])
    
