from random import randint
import subprocess as sp

print("+=====================================================================================================================+")
print("|                                                                                                                     |")
print("|                                                  BETTER PASSWORDS                                                   |")
print("|                                                 by Cillian Collins                                                  |")
print("|                                                                                                                     |")
print("+=====================================================================================================================+")

word = str(raw_input('Enter your password here: '))

while len(word) < 6 or not word.replace(' ', '').isalpha():
    if len(word) < 6:
        print("Please enter a word larger than 6 characters long!")
    else:
        print("Please enter letters only!")

    word = raw_input('Enter your password here: ')

print '#' + word + str(randint(1000,9999))
with open('passwords.txt', 'wb') as file:
    file.write('#' + word + str(randint(1000,9999)))

programName = "notepad.exe"
fileName = "passwords.txt"
sp.Popen([programName, fileName])
    
