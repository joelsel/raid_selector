class expac:
    def getExpac():
        match = ['legion', 'leg']
        return match

class classes:
    def getClasses(requiredRole):
        classesOut = []
        tank =       [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]
        healer =     [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0]
        melee =      [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
        ranged =     [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
        allRoles =   ['tank', 'healer', 'melee', 'ranged']
        allclasses = ['mage', 'druid', 'warrior', 'paladin',  'priest', 'shaman', 'rogue', 'hunter', 'warlock', 'death_knight', 'monk', 'demon_hunter']

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
        return classesOut
        #for x in rolevariants, classwt[x] + tankonly[x] > 0, do something
        # method is elegant but doesnt do what is needed
        # requiredRole>validClasses>random valid class > valid spec for class > output
#-----------------------------------------------
class spec(queryClasses):
    def getSpec():
        nothinghere

class getSpec:
    def __init__():
        import random

    def mage(requiredRole):
        if "ranged" in requiredRole:
            possible_spec = ['Arcane', 'Fire', 'Frost']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def druid(requiredRole):
        if "melee" in requiredRole:
            spec_sample = "Feral"
        elif "healer" in requiredRole:
            spec_sample = "Restoration"
        elif "tank" in requiredRole:
            spec_sample = "Guardian"
        elif "ranged" in requiredRole:
            spec_sample = "Balance"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def warrior(requiredRole):
        if "melee" in requiredRole:
            possible_spec = ["Arms", "Fury"]
            spec_sample = random.choices(possible_spec)
        elif "tank" in requiredRole:
            spec_sample = "Protection"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def paladin(requiredRole):
        if "melee" in requiredRole:
            spec_sample = "Retribution"
        elif "healer" in requiredRole:
            spec_sample = "Holy"
        elif "tank" in requiredRole:
            spec_sample = "Protection"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def priest(requiredRole):
        if "healer" in requiredRole:
            possible_spec = ['Holy', 'Discipline']
            spec_sample = random.choices(possible_spec)
        elif "ranged" in requiredRole:
            spec_sample = "Shadow"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def shaman(requiredRole):
        if "ranged" in requiredRole:
            spec_sample = "Elemental"
        elif "melee" in requiredRole:
            spec_sample = "Enhancement"
        elif "healer" in requiredRole:
            spec_sample = "Restoration"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def rogue(requiredRole):
        if "melee" in requiredRole:
            possible_spec = ['Assassination', 'Combat', 'Subtlety']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def hunter(requiredRole):
        if "ranged" in requiredRole:
            possible_spec = ['Marksmanship', 'Beast Mastery', 'Survival']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def warlock(requiredRole):
        if "ranged" in requiredRole:
            possible_spec = ['Affliction', 'Demonology', 'Destruction']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def death_knight(requiredRole):
        if "melee" in requiredRole:
            possible_spec = ['Frost', 'Unholy', 'Blood']
            spec_sample = random.choices(possible_spec)
        elif "tank" in requiredRole:
            possible_spec = ['Frost', 'Blood']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def monk(requiredRole):
        if "tank" in requiredRole:
            spec_sample = "Brewmaster"
        elif "melee" in requiredRole:
            spec_sample = "Windwalker"
        elif "healer" in requiredRole:
            spec_sample = "Mistweaver"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def demon_hunter(requiredRole):
        if "tank" in requiredRole:
            spec_sample = "Vengeance"
        elif "melee" in requiredRole:
            spec_sample = "Havoc"
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
    elif "Death Knight" in class_sample:
        death_knight_spec()
    elif "Monk" in class_sample:
        monk_spec()
    elif "Demon Hunter" in class_sample:
        demon_hunter_spec()
    else:
        print("class_picker error")

    role_counter()
'''