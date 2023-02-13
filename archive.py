
'''
#from expac_selection import 
check = int(input("?"))
if check == 1:
    #checkval = 1
    import importone as f
elif check == 2:
    #checkval = 2
    import importtwo as f


#f.callx()
#print(x)
newx = f.num.callx()
newx2 = f.num.callx2()
print (newx, newx2)
'''

'''
#from expac_selection import 
import importlib
check = int(input("?"))
if check == 1:
    x = 'importone'
    print(x)
    f = importlib.import_module(x)
elif check == 2:
    x = 'importtwo'
    print(x)
    f = importlib.import_module(x)
#f.callx()
#print(x)
outx = f.num.callx()
outx2 = f.num.callx2()
#print (newx, newx2)
print (outx, outx2)
'''

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

'''
check = ['hello', 'hi', 'no']
test = 'no'
for x in range(len(check)):
    if test in check[x]:
        print ('yes')
    else:
        print('no')

'''

'''
requiredRoles = ['tank', 'melee']

def getClasses(requiredRoles):
        classInclude = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        tank =         [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]
        healer =       [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1]
        melee =        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
        ranged =       [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
        allRoles =     ['tank', 'healer', 'melee', 'ranged']

        for foo in range(len(requiredRoles)):
            currentRole = eval(requiredRoles[foo])
            for x in range(len(classInclude)):
                    if classInclude[x] < currentRole[x]:
                        classInclude[x] = 1
                    else:
                        pass
        return classInclude

print(getClasses(requiredRoles))

'''

'''
a = [2, 4, 6, 0]
#print(a)
b = [2, 4, 6, 0]
c = [0, 0, 0, 0]
d = [0, 0, 0, 0]

for x in range(len(a)):
    c[x] = a[x] + b[x]
    if  c[x]>=1:
        d[x] = 1
    else:
        d[x] = 0

for x in range(len(a)):
    if a[x]+b[x] > 0:
        c[x] = 1
    else:
        c[x] = 0
print (c)
print (d)
herelist = ['a', 'b', 'c', 'd']
print (eval(herelist[2]))
'''

'''

--------------------------------deprecated---------------------------------------

class chooseExpansion:
    def main():
        import os, importlib
        home = os.getcwd()
        userin = input("Choose Expansion: ")
        #print (home) #diag

        contents = (os.listdir(home))
        target = []
        for n in contents:
            if 'spec' in n:
                target.append(n)
        #print (target) #diag
        removeExt = []
        for n in target:
            removeExt.append(os.path.splitext(n)[0])
        #print (removeExt) #diag

        expacMatchList = []
        for n in removeExt:
            expacMatchList.append(importlib.import_module(n).getExpac.expacMatch())
            #print (importlib.import_module(n).getExpac.expacMatch()) #diag
            #print (expacMatchList) #diag

        #chosen = []
        for n in range(len(expacMatchList)):
            if userin.lower() in expacMatchList[n]:
                expacOut = (expacMatchList[n][0], removeExt[n])
                #print (expacOut) #diag
                #print (expacOut[0]) #diag
                #print (expacOut[1]) #diag
                return expacOut
            else:
                pass

'''
