class expansion:
    def expansionMatch():
        match = ['tbc', 'bc', 'burning', 'crusade', 'the burning crusade', 'burning crusade']
        return match

class classes:
    def __init__():
        import random

    def getRandClass(requiredRole):
        
        import random

        classesOut = []
        tank =       [0, 1, 1, 1, 0, 0, 0, 0, 0]
        healer =     [0, 1, 0, 1, 1, 1, 0, 0, 0]
        melee =      [0, 1, 1, 1, 0, 1, 1, 0, 0]
        ranged =     [1, 1, 0, 0, 1, 1, 0, 1, 1]
        allRoles =   ['tank', 'healer', 'melee', 'ranged']
        allclasses = ['mage', 'druid', 'warrior', 'paladin',  'priest', 'shaman', 'rogue', 'hunter', 'warlock']

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
    def __init__():
        import random

    def mage(requiredRole):
        #spec_sample = ''
        if 'ranged' in requiredRole:
            possible_spec = ['Arcane', 'Fire', 'Frost']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def druid(requiredRole):
        #spec_sample = ''
        if 'melee' in requiredRole:
            spec_sample = "Feral"
        elif 'healer' in requiredRole:
            spec_sample = "Restoration"
        elif 'tank' in requiredRole:
            spec_sample = "Guardian"
        elif 'ranged' in requiredRole:
            spec_sample = "Balance"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def warrior(requiredRole):
        #spec_sample = ''
        if 'melee' in requiredRole:
            possible_spec = ["Arms", "Fury"]
            spec_sample = random.choices(possible_spec)
        elif 'tank' in requiredRole:
            spec_sample = "Protection"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def paladin(requiredRole):
        #spec_sample = ''
        if 'melee' in requiredRole:
            spec_sample = "Retribution"
        elif 'healer' in requiredRole:
            spec_sample = "Holy"
        elif 'tank' in requiredRole:
            spec_sample = "Protection"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def priest(requiredRole):
        #spec_sample = ''
        if 'healer' in requiredRole:
            possible_spec = ['Holy', 'Discipline']
            spec_sample = random.choices(possible_spec)
        elif 'ranged' in requiredRole:
            spec_sample = "Shadow"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def shaman(requiredRole):
        #spec_sample = ''
        if 'ranged' in requiredRole:
            spec_sample = "Elemental"
        elif 'melee' in requiredRole:
            spec_sample = "Enhancement"
        elif 'healer' in requiredRole:
            spec_sample = "Restoration"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def rogue(requiredRole):
        #spec_sample = ''
        if 'melee' in requiredRole:
            possible_spec = ['Assassination', 'Combat', 'Subtlety']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def hunter(requiredRole):
        #spec_sample = ''
        if 'ranged' in requiredRole:
            possible_spec = ['Marksmanship', 'Beast Mastery', 'Survival']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def warlock(requiredRole):
        #spec_sample = ''
        if 'ranged' in requiredRole:
            possible_spec = ['Affliction', 'Demonology', 'Destruction']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample
'''
    # class picker redirection
    def class_redirect(class_sample):
        if "Mage" in class_sample:
            mage_spec()
        elif "Druid" in class_sample:
            druid_spec()
        elif "Warrior" in class_sample:
            warrior_spec()
        elif "Paladin" in class_sample:
            paladin_spec()
        elif "Priest" in class_sample:
            priest_spec()
        elif "Shaman" in class_sample:
            shaman_spec()
        elif "Rogue" in class_sample:
            rogue_spec()
        elif "Hunter" in class_sample:
            hunter_spec()
        elif "Warlock" in class_sample:
            warlock_spec()
        else:
            print("class_picker error")

        role_counter() 
'''