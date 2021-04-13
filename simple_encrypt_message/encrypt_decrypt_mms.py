# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:50:10 2020

@author: Quoc Thinh Vo
@simple encryption

"""

import numpy as np

def encrypt(x_string):
    y_list=[]
    z_list=[]
    for x in x_string:
        y= 2**(ord(x)) % 11
        z= 2**(ord(x)) / 11
        y_list.append(y) 
        z_list.append(z)

    return y_list,z_list 

def decrypt(y_list,z_list ):
    new_x_list=[]
    for y,z in zip(y_list,z_list):
        x = z*11 + y
        x =chr(int(np.log(x)/np.log(2)))
        new_x_list.append(x)
    return new_x_list


x_string = str(input("Enter your message: \n"))

y_list,z_list= encrypt(x_string)

x_list = decrypt(y_list,z_list)

string_mms= ''.join(x_list)

ask_user = str(input("You want to see your encrypted message? (Y/N): \n"))


if ask_user == 'Y':
    for i in range(len(y_list)):
        print(y_list[i],end='')
    print()
    ask_user2 = str(input("You want to see your decrypted message? (Y/N): \n"))
    
    if ask_user2 == 'Y':
        print(string_mms)
    else:
        print("Ok, thank you bye!")    
else:
    print("Ok, thank you bye!")

    