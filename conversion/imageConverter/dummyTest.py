#!/usr/bin/env python3
# simple python script that createes a text file
file = open("dummy.txt","w")
file.write("test\n")
file.write("1, 2, 3")

file.close()
