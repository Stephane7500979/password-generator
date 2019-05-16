#importing needed objects
import os
import re
#affecting the folder dir to foldername
#foldername = "python patern essai"

#reads in the text file
foldername = open('functionModify.txt','r' )

for line in foldername:
    oldPassword = (line.split(':')[1])
    #print(oldPassword)
    newline = line.replace(oldPassword, " new")
    print(newline)
