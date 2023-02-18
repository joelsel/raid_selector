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
    tank =       [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]
    healer =     [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0]
    melee =      [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
    ranged =     [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
    allRoles =   ['tank', 'healer', 'melee', 'ranged']
    allClasses = ['mage', 'druid', 'warrior', 'paladin', 'priest', 'shaman', 'rogue', 'hunter', 'warlock', 'death_knight', 'monk', 'demon_hunter']

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

# ------ clearer naming scheme needed for this to work
#print(random.choices(eval(fooRun[0])))
#print(f'\ninput was {requiredRole} and classes are {getClass(requiredRole)}')

class getSpec:
    def __init__(self, requiredRole):
        import random
        self.requiredRole = requiredRole

    def mage(self):
        if "ranged" in self.requiredRole:
            possibleSpec = ['Arcane', 'Fire', 'Frost']
            spec = random.choices(possibleSpec)
        else:
            spec = "Invalid!"
        return spec

    def druid(self):
        if "melee" in self.requiredRole:
            spec = "Feral"
        elif "healer" in requiredRole:
            spec = "Restoration"
        elif "tank" in requiredRole:
            spec = "Guardian"
        elif "ranged" in requiredRole:
            spec = "Balance"
        else:
            spec = "Invalid!"
        return spec

    def warrior(self):
        if "melee" in self.requiredRole:
            possibleSpec = ["Arms", "Fury"]
            spec = random.choices(possibleSpec)
        elif "tank" in requiredRole:
            spec = "Protection"
        else:
            spec = "Invalid!"
        return spec

    def paladin(self):
        if "melee" in self.requiredRole:
            spec = "Retribution"
        elif "healer" in requiredRole:
            spec = "Holy"
        elif "tank" in requiredRole:
            spec = "Protection"
        else:
            spec = "Invalid!"
        return spec

    def priest(self):
        if "healer" in self.requiredRole:
            possibleSpec = ['Holy', 'Discipline']
            spec = random.choices(possibleSpec)
        elif "ranged" in requiredRole:
            spec = "Shadow"
        else:
            spec = "Invalid!"
        return spec

    def shaman(self):
        if "ranged" in self.requiredRole:
            spec = "Elemental"
        elif "melee" in requiredRole:
            spec = "Enhancement"
        elif "healer" in requiredRole:
            spec = "Restoration"
        else:
            spec = "Invalid!"
        return spec

    def rogue(self):
        if "melee" in self.requiredRole:
            possibleSpec = ['Assassination', 'Combat', 'Subtlety']
            spec = random.choices(possibleSpec)
        else:
            spec = "Invalid!"
        return spec

    def hunter(self):
        if "ranged" in self.requiredRole:
            possibleSpec = ['Marksmanship', 'Beast Mastery', 'Survival']
            spec = random.choices(possibleSpec)
        else:
            spec = "Invalid!"
        return spec

    def warlock(self):
        if "ranged" in self.requiredRole:
            possibleSpec = ['Affliction', 'Demonology', 'Destruction']
            spec = random.choices(possibleSpec)
        else:
            spec = "Invalid!"
        return spec

    def death_knight(self):
        if "melee" in self.requiredRole:
            possibleSpec = ['Frost', 'Unholy', 'Blood']
            spec = random.choices(possibleSpec)
        elif "tank" in requiredRole:
            possibleSpec = ['Frost', 'Blood']
            spec = random.choices(possibleSpec)
        else:
            spec = "Invalid!"
        return spec

    def monk(self):
        if "tank" in self.requiredRole:
            spec = "Brewmaster"
        elif "melee" in requiredRole:
            spec = "Windwalker"
        elif "healer" in requiredRole:
            spec = "Mistweaver"
        else:
            spec = "Invalid!"
        return spec

    def demon_hunter(self):
        if "tank" in self.requiredRole:
            spec = "Vengeance"
        elif "melee" in requiredRole:
            spec = "Havoc"
        else:
            spec = "Invalid!"
        return spec

returnSpec = (f"getSpec(requiredRole).{getClass(requiredRole)}()")
print (returnSpec)
print (eval(returnSpec))