import random

class expansion:
    def expansionMatch():
        match = ['wrath', 'wotlk', 'lich', 'king', 'lich king', 'wrath of the lich king']
        return match

class classes:
    def __init__():
        import random

    def getRandClass(requiredRole):

        import random
        
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
    def __init__():
        import random

    def mage(requiredRole):
        #import random
        #spec_sample = ''
        if 'ranged' in requiredRole:
            possible_spec = ['Arcane', 'Fire', 'Frost']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def druid(requiredRole):
        #import random
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
        #import random
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
        #import random
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
        #import random
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
        #import random
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
        #import random
        #spec_sample = ''
        if 'melee' in requiredRole:
            possible_spec = ['Assassination', 'Combat', 'Subtlety']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def hunter(requiredRole):
        #import random
        #spec_sample = ''
        if 'ranged' in requiredRole:
            possible_spec = ['Marksmanship', 'Beast Mastery', 'Survival']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def warlock(requiredRole):
        #import random
        #spec_sample = ''
        if 'ranged' in requiredRole:
            possible_spec = ['Affliction', 'Demonology', 'Destruction']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def death_knight(requiredRole):
        #import random
        #spec_sample = ''
        if 'melee' in requiredRole:
            possible_spec = ['Frost', 'Unholy', 'Blood']
            spec_sample = random.choices(possible_spec)
        elif 'tank' in requiredRole:
            possible_spec = ['Frost', 'Blood']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample
# class picker redirection
def class_redirect(class_sample):
    if "Mage" in class_sample:
        mage()
    elif "Druid" in class_sample:
        druid()
    elif "Warrior" in class_sample:
        warrior()
    elif "Paladin" in class_sample:
        paladin()
    elif "Priest" in class_sample:
        priest()
    elif "Shaman" in class_sample:
        shaman()
    elif "Rogue" in class_sample:
        rogue()
    elif "Hunter" in class_sample:
        hunter()
    elif "Warlock" in class_sample:
        warlock()
    elif "Death Knight" in class_sample:
        death_knight()
    else:
        print("class_picker error")

    role_counter()