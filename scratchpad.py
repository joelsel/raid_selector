
import importlib
import random

#raidSize = int(input("number: "))
raidSize = 2
expansionName = importlib.import_module("expac_selection").chooseExpansion.main()
allRoles = ['tank', 'healer', 'melee', 'ranged']
validRoles = [1, 1, 1, 1]
requiredRole = random.choices(allRoles, weights = validRoles)
print(requiredRole)

class utility:
    def makeReadable(getTerm):
        hold = []
        readableOut = []

        tempWords = (getTerm.replace('_', ' ')).split()
        for x in range(len(tempWords)):
            hold.append(tempWords[x].capitalize())
            readableOut = " ".join(hold)
        return readableOut


def main(count, expansionName, requiredRole):

    currentExpansion = expansionName[1]
    #requiredRole = ["ranged"]


    print(f'\ncurrent required role = {requiredRole}')
    returnClassCommand = (f"importlib.import_module('{currentExpansion}').classes.getRandClass({requiredRole})")
    print(f"return class command is {returnClassCommand}")
    viableClass = (eval(returnClassCommand))
    returnViableSpec = (f"importlib.import_module('{currentExpansion}').getSpec.{viableClass}({requiredRole})")
    print (f'return viable spec command is = {returnViableSpec}')
    viableSpec = (eval(returnViableSpec))

    #returnSpecInit = f"importlib.import_module('{currentExpansion}').getSpec.__init__()"
    #specInit = eval(returnSpecInit)

    requiredRoleReadable = utility.makeReadable(requiredRole[0])
    viableSpecReadable = utility.makeReadable(viableSpec)
    viableClassReadable = utility.makeReadable(viableClass)
   
    lineOut = (f'\n{(count+1):<4}{requiredRoleReadable:_<10}{viableSpecReadable:-^15}{viableClassReadable:_>10}')
    print(requiredRoleReadable)
    print(viableClassReadable)
    print(viableSpecReadable)

    #print(f"{requiredRoleReadable:<15}{viableSpecReadable:^10}{viableClassReadable:^15}{'end':>1}")
    return lineOut


main(raidSize, expansionName, requiredRole)


def wtf(lineOut):    
    with open ('trial.txt', 'a') as f:
        #f.write(f"\n\n")
            f.write(lineOut)

wtf("\n\n")
wtf(f"chosen expansion: {expansionName}")
#print(importlib.import_module("expac_selection").chooseExpansion.main())
#wtf(f"\n expansion: {}")
for count in range(raidSize):
    wtf(main(count, expansionName, requiredRole))
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