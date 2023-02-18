'''
import importlib
test = importlib.import_module('expac_selection').chooseExpansion.main()
#print (test)
print (f'expansion name is {test[0]} and expansion list will be {test[1]}')

'''


import os
print (f"current working directory is {os.getcwd()}")
import random
requiredRole = ['melee']

def getClass(requiredRole):
    import random
    classesOut = []
    tank =         [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]
    healer =       [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0]
    melee =        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
    ranged =       [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
    allRoles =     ['tank', 'healer', 'melee', 'ranged']
    allClasses =   ['mage', 'druid', 'warrior', 'paladin', 'priest', 'shaman', 'rogue', 'hunter', 'warlock', 'death_knight', 'monk', 'demon_hunter']

    for x in range(len(allRoles)):
        if allRoles[x] in requiredRole:
            roleValidClasses = eval(allRoles[x])
            for y in range(len(roleValidClasses)):
                if roleValidClasses[y] == 1:
                    classesOut.append(allClasses[y])
                else:
                    pass
        else:
            pass
    randClass = random.choices(classesOut)
    return randClass[0]


#foo = ['getClass']
#fooRun = [f"{foo[0]}(requiredRole)"]
#print(fooRun[0])
#print(eval(fooRun[0]))
print(f"{getClass(requiredRole)}(requiredRole)")
# ------ clearer naming scheme needed for this to work
#print(random.choices(eval(fooRun[0])))


#print(f'\ninput was {requiredRole} and classes are {getClass(requiredRole)}')