import random

class expansion:
    def expansionMatch():
        match = ['cataclysm', 'cat', 'cata']
        return match

class classes:
    def getRandClass(requiredRole):

        classesOut = []
        tank =       [0, 1, 1, 1, 0, 0, 0, 0, 0, 1]
        healer =     [0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
        melee =      [0, 1, 1, 1, 0, 1, 1, 0, 0, 1]
        ranged =     [1, 1, 0, 0, 1, 1, 0, 1, 1, 0]
        allRoles =   ['tank', 'healer', 'melee', 'ranged']
        allclasses = ['mage', 'druid', 'warrior', 'paladin',  'priest', 'shaman', 'rogue', 'hunter', 'warlock', 'death_knight']

        for x in range(len(allRoles)):
            if allRoles[x] in requiredRole:
                validClasses = eval(allRoles[x])
                for y in range(len(validClasses)):
                    if validClasses[y] == 1:
                        classesOut.append(allclasses[y])
                    else:
                        pass
            else:
                pass
        randClass = random.choices(classesOut)
        return randClass[0]

class getSpec:
    def mage(requiredRole):
        if 'ranged' in requiredRole:
            possible_spec = ['Arcane', 'Fire', 'Frost']
            spec_sample = random.choices(possible_spec)
            specOut = str(spec_sample[0])
        else:
            specOut = 'Invalid!'
        return specOut

    def druid(requiredRole):
        if 'melee' in requiredRole:
            specOut = 'Feral'
        elif 'healer' in requiredRole:
            specOut = 'Restoration'
        elif 'tank' in requiredRole:
            specOut = 'Guardian'
        elif 'ranged' in requiredRole:
            specOut = 'Balance'
        else:
            specOut = 'Invalid!'
        return specOut

    def warrior(requiredRole):
        if 'melee' in requiredRole:
            possible_spec = ['Arms', 'Fury']
            spec_sample = random.choices(possible_spec)
            specOut = str(spec_sample[0])
        elif 'tank' in requiredRole:
            specOut = 'Protection'
        else:
            specOut = 'Invalid!'
        return specOut

    def paladin(requiredRole):
        if 'melee' in requiredRole:
            specOut = 'Retribution'
        elif 'healer' in requiredRole:
            specOut = 'Holy'
        elif 'tank' in requiredRole:
            specOut = 'Protection'
        else:
            specOut = 'Invalid!'
        return specOut

    def priest(requiredRole):
        if 'healer' in requiredRole:
            possible_spec = ['Holy', 'Discipline']
            spec_sample = random.choices(possible_spec)
            specOut = str(spec_sample[0])
        elif 'ranged' in requiredRole:
            specOut = 'Shadow'
        else:
            specOut = 'Invalid!'
        return specOut

    def shaman(requiredRole):
        if 'ranged' in requiredRole:
            specOut = 'Elemental'
        elif 'melee' in requiredRole:
            specOut = 'Enhancement'
        elif 'healer' in requiredRole:
            specOut = 'Restoration'
        else:
            specOut = 'Invalid!'
        return specOut

    def rogue(requiredRole):
        if 'melee' in requiredRole:
            possible_spec = ['Assassination', 'Combat', 'Subtlety']
            spec_sample = random.choices(possible_spec)
            specOut = str(spec_sample[0])
        else:
            specOut = 'Invalid!'
        return specOut

    def hunter(requiredRole):
        if 'ranged' in requiredRole:
            possible_spec = ['Marksmanship', 'Beast Mastery', 'Survival']
            spec_sample = random.choices(possible_spec)
            specOut = str(spec_sample[0])
        else:
            specOut = 'Invalid!'
        return specOut

    def warlock(requiredRole):
        if 'ranged' in requiredRole:
            possible_spec = ['Affliction', 'Demonology', 'Destruction']
            spec_sample = random.choices(possible_spec)
            specOut = str(spec_sample[0])
        else:
            specOut = 'Invalid!'
        return specOut

    def death_knight(requiredRole):
        if 'melee' in requiredRole:
            possible_spec = ['Frost', 'Unholy', 'Blood']
            spec_sample = random.choices(possible_spec)
            specOut = str(spec_sample[0])
        elif 'tank' in requiredRole:
            possible_spec = ['Frost', 'Blood']
            spec_sample = random.choices(possible_spec)
            specOut = str(spec_sample[0])
        else:
            specOut = 'Invalid!'
        return specOut