
#debugging

#print(xpick())
#print (expacData)
#print (r[1])
#w = expac(r[0], r[1])
#w.readout()

'''
#implement read method from reference file, map output to local variable, read nested list element from local variable
from expansionList import *

class expacSelect:
    def __init__ (self, expacData):
        self.expacData = expacData
    
    def readData(self):
        #r = (f"\nreading class data: {self.expacData[0]}, reading role data: {self.expacData[1]}")
        #r1 = (f"\nread element 2 of class: {self.expacData[0][1]}, read element 3 of role: {self.expacData[1][2]}")
        #print (r)
        #print (r1)
        place
    
    def castExpacData(self):
        classList =   self.expacData[0]
        roleList =    self.expacData[1]
        class_wt =    self.expacData[2]
        tank_only =   self.expacData[3]
        healer_only = self.expacData[4]
        melee_only =  self.expacData[5]
        ranged_only = self.expacData[6]
        expacName =   self.expacData[7]

        print(f'classList = {classList}\n')
        print(f'roleList = {roleList}\n')
        print(f'class_wt = {class_wt}\n')
        print(f'tank only = {tank_only}\n')
        print(f'healer only = {healer_only}\n')
        print(f'melee only = {melee_only}\n') 
        print(f'expansion name = {expacName}\n')

    def testdata(self):
        #r = (f"\n\n whole expac data is: {self.expacData}")
        r = (f'\n \
            current classList =   {self.expacData[0]} \n\n \
            current roleList =    {self.expacData[1]} \n \
            current class_wt =    {self.expacData[2]} \n \
            current tank_only =   {self.expacData[3]} \n \
            current healer_only = {self.expacData[4]} \n \
            current melee_only =  {self.expacData[5]} \n \
            current ranged_only = {self.expacData[6]} \n \
            ')
        print (r)

w = expacSelect(xpick())
#w.readData()
#w.testdata()
w.castExpacData()
'''

'''
#testing return spec providing role
import random
import samplexpac as sl
specOptions = ['Tank', 'Healer', 'Melee', 'Ranged']
role_sample = random.choices(specOptions)
spec_out = sl.sample_expansion.druid_spec(role_sample)
print (spec_out)
'''
'''
# testing return expacData from expansionList
import expansionList as el
w = el.xpick()
#print (w[0])
classList =   w[0]
roleList =    w[1]
class_wt =    w[2]
tank_only =   w[3]
healer_only = w[4]
melee_only =  w[5]
ranged_only = w[6]
expacName =   w[7]
print(f'classList = {classList}\n')
print(f'roleList = {roleList}\n')
print(f'class_wt = {class_wt}\n')
print(f'tank only = {tank_only}\n')
print(f'healer only = {healer_only}\n')
print(f'melee only = {melee_only}\n') 
print(f'expansion name = {expacName}\n')


import random
import importlib
#samplexpac contains TBC classes

x = ('specList' + expacName[0])

#import specList as sl workaround
print ('importspeclist string test: ', x) #diag
'''
'''
sl = importlib.import_module(x)

#primitive import init
prej = 'sl.pullSpec.__init__()'


#import samplexpac as sl
specOptions = ['Tank', 'Healer', 'Melee', 'Ranged']
g = (random.choices(classList))

#lowercase input to match function names
h = (g[0]).lower()

#replace space with underscore
h = h.replace(" ","_")

role_sample = random.choices(specOptions)
i = ('sl.pullSpec.' + h + '(role_sample)')
print ("role sample input : ", i) #diag
j = eval(i)

print (role_sample) #diagnostic

eval(prej) #import 'import' method before running function
print (j)
#spec_out = sl.pullSpec.druid(role_sample)
#print (spec_out)
'''

import importlib
#raidSize = int(input("number: "))
raidSize = 2
expansionName = importlib.import_module("expac_selection").chooseExpansion.main()

class utility:
    def capAll(input):
        temp = (input.replace("_", " ")).split()
        readable = []
        readableOut = []
        for x in range(len(temp)):
            readable.append(temp[x].capitalize())
            readableOut = " ".join(readable)
        return readableOut


def main(count, expansionName):

    currentExpansion = expansionName[1]
    requiredRole = ["ranged"]


    print(f'\ncurrent required role = {requiredRole}')
    returnClassCommand = (f"importlib.import_module('{currentExpansion}').classes.getClasses({requiredRole})")
    print(f"return class command is {returnClassCommand}")
    viableClass = (eval(returnClassCommand))
    returnViableSpec = (f"importlib.import_module('{currentExpansion}').getSpec({requiredRole}).{viableClass}()")
    print (f'return viable spec command is = {returnViableSpec}')
    viableSpec = (eval(returnViableSpec))

    requiredRoleReadable = utility.capAll(requiredRole[0])
    viableSpecReadable = utility.capAll(viableSpec)
    viableClassReadable = utility.capAll(viableClass)
   
    lineOut = (f'\n{(count+1):<4}{requiredRoleReadable:_<10}{viableSpecReadable:-^15}{viableClassReadable:_>10}')
    print(requiredRoleReadable)
    print(viableClassReadable)
    print(viableSpecReadable)

    #print(f"{requiredRoleReadable:<15}{viableSpecReadable:^10}{viableClassReadable:^15}{'end':>1}")
    return lineOut


main(raidSize,expansionName)


def wtf(lineOut):    
    with open ('trial.txt', 'a') as f:
        #f.write(f"\n\n")
            f.write(lineOut)

wtf("\n\n")
#print(importlib.import_module("expac_selection").chooseExpansion.main())
#wtf(f"\n expansion: {}")
for x in range(raidSize):
    wtf(main(x))
'''
def capAll(input):
    temp = (input.replace("_", " ")).split()
    readable = []
    for x in range(len(temp)):
        readable.append(temp[x].capitalize())
    return readable


#b = 'this'

#print(capAll(b))
'''