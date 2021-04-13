"""
Author: Quoc Thinh Vo
Date: 02/20/2021
"""
import bcrypt
from timeit import default_timer as timer # https://stackoverflow.com/a/25823885
import numpy as np
# assumes hashed password file is named 'table.csv'
# and stored in same directory as report
hashed_password_file = "table.csv"
with open(hashed_password_file) as f:
    hashed_passwords = [p.strip() for p in f.readlines()]

# print the first 10 hashed passwords, just for inspection:
for i, hashed_password in enumerate(hashed_passwords):
    print(hashed_password)
    if i + 1 >= 10:
        break
		
# sample code for using bcrypt
# see here for more sample code:
# https://pypi.org/project/bcrypt/#usage

# the following salt was generated using bcrypt.gensalt()
# the "b" prefix turns the string into binary
# this is necessary because the bcrypt.hashpw function
# requires that the password and salt are binary numbers, not strings
salt = b'$2b$12$qGA7Ps7wsWagoMz8nQQDYu' 

my_password = "abc"
# we can call the "encode" method on a string to turn it into a binary number
# we can also call "decode" to turn binary back into a string
my_hashed_password = bcrypt.hashpw(my_password.encode(), salt)
# the hashed password will look nothing like the original plaintext password
print(my_password, salt, my_hashed_password)
# the first 29 characters of the hashed password will be the original salt used
print(my_hashed_password[:29] == salt)

# the same password hashed with a different salt
# will look completely different, even if we ignore the salt portion of the hash:
print(my_hashed_password[29:])
print(bcrypt.hashpw(my_password.encode(), b'$2b$12$1Irnpr/K.bTnfzr6PVaAqO')[29:])

#Timing the abc password
salt = b'$2b$12$qGA7Ps7wsWagoMz8nQQDYu' 
my_password = "abc"

def duration_in_milliseconds(my_password, salt):
    start = timer()
    bcrypt.hashpw(my_password.encode(), salt)
    end = timer()
    duration = (end - start) * 1000 # time in milliseconds
    return duration

def average_duration_in_milliseconds(my_password, salt, sample_size=10):
    durations = []
    for i in range(sample_size):
        duration = duration_in_milliseconds(my_password, salt)
        durations.append(duration)
    return np.mean(durations)

print( average_duration_in_milliseconds(my_password, salt))

# Cracking a list of passwords
a=ord('a')
alpha_list=[chr(i) for i in range(a,a+26)]
combo_words = [first + last for last in alpha_list for first in alpha_list]

salt = b'$2b$12$5bdOr7S8eJFjYx9byyKMOO'
password_list = []
hashed_password_file = "table.csv"

with open(hashed_password_file) as f:
    hashed_passwords = [p.strip() for p in f.readlines()]

for hashed_password in (hashed_passwords):
    password_list.append(hashed_password[29:])

# To maintain password order and reduce possible duplicated:
dict_pass = { i : "None" for i in password_list } 

for word in combo_words:
    if bcrypt.hashpw(word.encode(),salt).decode("utf-8")[29:] in password_list:
        dict_pass[bcrypt.hashpw(word.encode(),salt).decode("utf-8")[29:]] = (word)
        
print("Done")

# Print out the list of cracked passwords
for key,value in dict_pass.items():
    print ("hashed password: ",key,"-----","cracked: ",value)
