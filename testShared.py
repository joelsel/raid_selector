'''
import importlib
test = importlib.import_module('expac_selection').chooseExpansion.main()
#print (test)
print (f'expansion name is {test[0]} and expansion list will be {test[1]}')

'''


#import os
#print (f"current working directory is {os.getcwd()}")
import random
#requiredRole = ['melee']
class getClasses:
    def __init__(self, requiredRole):
        self.requiredRole = requiredRole
        
    def getRandClass(self):
        import random

        classesOut = []
        tank =       [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]
        healer =     [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0]
        melee =      [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
        ranged =     [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
        allRoles =   ['tank', 'healer', 'melee', 'ranged']
        allClasses = ['mage', 'druid', 'warrior', 'paladin', 'priest', 'shaman', 'rogue', 'hunter', 'warlock', 'death_knight', 'monk', 'demon_hunter']

        for x in range(len(allRoles)):
            if allRoles[x] in self.requiredRole:
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

# ------ clearer naming scheme needed for this to work
#print(random.choices(eval(fooRun[0])))
#print(f'\ninput was {requiredRole} and classes are {getClass(requiredRole)}')

class getSpec:
    def __init__(self, requiredRole):
        import random
        self.requiredRole = requiredRole

    def mage(self):
        if 'ranged' in self.requiredRole:
            possibleSpec = ['Arcane', 'Fire', 'Frost']
            spec = random.choices(possibleSpec)
        else:
            spec = ['Invalid!']
        return spec[0]

    def druid(self):
        if 'melee' in self.requiredRole:
            spec = ['Feral']
        elif 'healer' in self.requiredRole:
            spec = ['Restoration']
        elif 'tank' in self.requiredRole:
            spec = ['Guardian']
        elif 'ranged' in self.requiredRole:
            spec = ['Balance']
        else:
            spec = ['Invalid!']
        return spec[0]

    def warrior(self):
        if 'melee' in self.requiredRole:
            possibleSpec = ["Arms", "Fury"]
            spec = random.choices(possibleSpec)
        elif 'tank' in self.requiredRole:
            spec = "Protection"
        else:
            spec = ['Invalid!']
        return spec[0]

    def paladin(self):
        if 'melee' in self.requiredRole:
            spec = ['Retribution']
        elif 'healer' in self.requiredRole:
            spec = ['Holy']
        elif 'tank' in self.requiredRole:
            spec = ['Protection']
        else:
            spec = ['Invalid!']
        return spec[0]

    def priest(self):
        if 'healer' in self.requiredRole:
            possibleSpec = ['Holy', 'Discipline']
            spec = random.choices(possibleSpec)
        elif 'ranged' in self.requiredRole:
            spec = ['Shadow']
        else:
            spec = ['Invalid!']
        return spec[0]

    def shaman(self):
        if 'ranged' in self.requiredRole:
            spec = ['Elemental']
        elif 'melee' in self.requiredRole:
            spec = ['Enhancement']
        elif 'healer' in self.requiredRole:
            spec = ['Restoration']
        else:
            spec = ['Invalid!']
        return spec[0]

    def rogue(self):
        if 'melee' in self.requiredRole:
            possibleSpec = ['Assassination', 'Combat', 'Subtlety']
            spec = random.choices(possibleSpec)
        else:
            spec = ['Invalid!']
        return spec[0]

    def hunter(self):
        if 'ranged' in self.requiredRole:
            possibleSpec = ['Marksmanship', 'Beast Mastery']
            spec = random.choices(possibleSpec)
        elif 'melee' in self.requiredRole:
            spec = ['Survival']
        else:
            spec = ['Invalid!']
        return spec[0]

    def warlock(self):
        if 'ranged' in self.requiredRole:
            possibleSpec = ['Affliction', 'Demonology', 'Destruction']
            spec = random.choices(possibleSpec)
        else:
            spec = ['Invalid!']
        return spec[0]

    def death_knight(self):
        if 'melee' in self.requiredRole:
            possibleSpec = ['Frost', 'Unholy', 'Blood']
            spec = random.choices(possibleSpec)
        elif 'tank' in self.requiredRole:
            possibleSpec = ['Frost', 'Blood']
            spec = random.choices(possibleSpec)
        else:
            spec = ['Invalid!']
        return spec[0]

    def monk(self):
        if 'tank' in self.requiredRole:
            spec = ['Brewmaster']
        elif 'melee' in self.requiredRole:
            spec = ['Windwalker']
        elif 'healer' in self.requiredRole:
            spec = ['Mistweaver']
        else:
            spec = ['Invalid!']
        return spec[0]

    def demon_hunter(self):
        if 'tank' in self.requiredRole:
            spec = ['Vengeance']
        elif 'melee' in self.requiredRole:
            spec = ['Havoc']
        else:
            spec = ['Invalid!']
        return spec[0]

#returnSpec = (f"getSpec(requiredRole).{getClass(requiredRole)}()")
#print (returnSpec)
#print (eval(returnSpec))
#print(getClass(requiredRole))