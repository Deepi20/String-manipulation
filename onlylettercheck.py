import re

name_check = re.compile(r"[^A-Za-zs.]")

name = raw_input ("Please, enter your name: ")

while name_check.search(name):
    print "Please enter your name correctly!"
    name = raw_input ("Please, enter your name: ")
