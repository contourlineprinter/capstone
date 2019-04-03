# !/usr/bin/env python3
# creating a simple python script that creates a text file
# this will be used to test if our server is able to call this on file upload
file = open("test.txt","w")
file.write("test \n")
file.write("1 , 2, 3")


file.close()

