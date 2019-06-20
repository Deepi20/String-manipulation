import re

phone_check = re.compile(r"[^0-9s-()]")

phone = raw_input ("Please, enter your phone: ")

while phone_check.search(phone):
    print "Please enter your phone correctly!"
    phone = raw_input ("Please, enter your phone: ")
