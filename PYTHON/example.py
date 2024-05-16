from datetime import datetime

now = datetime.now()
print(now)

from datetime import date

today = date.today()
print("CURRENT DATE : ", today)
print(dir(datetime))

import datetime

datetime_obj = datetime.datetime.now()
print("Datetime: ", datetime_obj)

import json

x = {
   'first_name': 'John',
   'last_name': 'Doe',
   'age': 30
}
my_json = json.dumps(x, indent = 18)

print(my_json)

import re
regex = "hello"
txt = "hello world"

res = re.search(regex, txt)
print("Index of the start and end position: ", res.span())
print("Index of the start position: ", res.start())
print("Index of the end position: ", res.end())

import re
regex = "Python"
txt = "I love Python, because Python is fun to learn!"

matches = re.sub(regex, "javascript", txt)
print(matches)

import re

regex = "^mango"
txt = "mango is sweet"

x = re.findall(regex, txt)
if x:
   print("The string starts with 'mango'")
else:
   print("The string does not start with 'mango'")
   
import re

x = re.findall("[pyt]", "python")
print(x)

import re

x = re.findall("\D", "John is 30 years old, while Jane is 29.")
print(x)

o = open("/storage/emulated/0/python/BAMBI_NET.css", "a")
o.write("I love html")
o.close()

o = open("BAMBI_NET.css", "r")

q = o.read()
print(q)


import os

filepath = "htmlhello.css"

if os.path.exists(filepath):
    os.remove(filepath)
else:
    print("FILEPATH NON-EXISTENCE")