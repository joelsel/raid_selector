
"""
class experiment:
    def __init__(self, day, month):
        self.day = day
        self.month = month

    def output(self):
        prompt = ("today is {} the {}".format(self.day,self.month))
        print (prompt)
z = experiment("monday", "23")
z.output()
"""

"""
#constructing expansion data as list
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
print(type(c))
print(c)  
print(c[1])

"""


"""
class foo:
    def __init__(self, time, day, month):
        self.time = time
        self.day = day
        self.month = month


    def testing(self):
        #f"time is {self.time}, day is {self.day}, month is {self.month}"
        prompt = ("prompt time is {}, prompt day is {}, prompt month is {}".format(self.time, self.day, self.month))
        name = input ("name = ")
        print (prompt)
        print (f"name was {name}")

    def thing(self):
        self.time = input("time is: ")
        self.day = input("day is: ")
        self.month = input("month is: ")
        print (f"\ninput time was {self.time},\ninput day was {self.day},\ninput month was {self.month}\n")

bar = foo("testtime", "testday", "testmonth")
#bar.testing()
bar.testing()
#working on implementing classes
"""
"""

from importtest import odd
from importtest import even

class number:
    def __init__(self, first, second, third):
            self.first = first
            self.second = second
            self.third = third
    
    def readout(self):
            f"\n first value = {self.first}\n second value = {self.second}\n third value = {self.third}"

filepick = input("odd or even: ")
choice = []
if "odd" in filepick:
    for i in odd:
        choice.append(i)
elif "even" in filepick:
    for i in even:
        choice.append(i)
else:
    print ("test failed")
w = number(choice)
w.readout()
"""

# need to instatiate a class before you can use it, what does that mean?
# try running the test without the class or def or init first


"""
#appending elements to another list, test(failed)
a = ['1', '2', '3']
b = []

for i in a:
    b.append(i)
    print(i)
#c = list(f"{b}")
c = f"{b}"
print(c)
print(f"c type is {type(c)}")

print(f"a type is {type(a)}")
print(len(c))
"""

"""
#testing import function
from importtest import *
class expac:
    def __init__ (self, classList, roleList):
        self.classList = classList
        self.roleList = roleList

    def readout(self):
       print (f"class list includes {self.classList}, role list includes {self.roleList}")

"""

"""
#passthrough input to secondary file
expacSelect = input("wrath or legion: ")
r = []
if "wrath" in expacSelect:
    r = Wrath()
elif "legion" in expacSelect:
    r = Legion()
else:
    print("selection error")
print (r)
print (r[1])
w = expac(r[0], r[1])
w.readout()
"""

#debugging

#print(xpick())
#print (expacData)
#print (r[1])
#w = expac(r[0], r[1])
#w.readout()


#implement read method from reference file, map output to local variable, read nested list element from local variable
from importtest import *

class expacTest:
    def __init__ (self, expacData):
        self.expacData = expacData
    
    def readData(self):
        r = (f"reading class data: {self.expacData[0]}, reading role data: {self.expacData[1]}")
        r1 = (f"read element 2 of class: {self.expacData[0][1]}, read element 3 of role: {self.expacData[1][2]}")
        print (r)
        print (r1)

w = expacTest(xpick())
w.readData()




