class getExpac:
    def expacMatch():
        match = ['legion', 'leg']
        return match
class pullSpec:
    def __init__():
        import random

    def mage(role_sample):
        if "Ranged" in role_sample:
            possible_spec = ['Arcane', 'Fire', 'Frost']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def druid(role_sample):
        if "Melee" in role_sample:
            spec_sample = "Feral"
        elif "Healer" in role_sample:
            spec_sample = "Restoration"
        elif "Tank" in role_sample:
            spec_sample = "Guardian"
        elif "Ranged" in role_sample:
            spec_sample = "Balance"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def warrior(role_sample):
        if "Melee" in role_sample:
            possible_spec = ["Arms", "Fury"]
            spec_sample = random.choices(possible_spec)
        elif "Tank" in role_sample:
            spec_sample = "Protection"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def paladin(role_sample):
        if "Melee" in role_sample:
            spec_sample = "Retribution"
        elif "Healer" in role_sample:
            spec_sample = "Holy"
        elif "Tank" in role_sample:
            spec_sample = "Protection"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def priest(role_sample):
        if "Healer" in role_sample:
            possible_spec = ['Holy', 'Discipline']
            spec_sample = random.choices(possible_spec)
        elif "Ranged" in role_sample:
            spec_sample = "Shadow"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def shaman(role_sample):
        if "Ranged" in role_sample:
            spec_sample = "Elemental"
        elif "Melee" in role_sample:
            spec_sample = "Enhancement"
        elif "Healer" in role_sample:
            spec_sample = "Restoration"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def rogue(role_sample):
        if "Melee" in role_sample:
            possible_spec = ['Assassination', 'Combat', 'Subtlety']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def hunter(role_sample):
        if "Ranged" in role_sample:
            possible_spec = ['Marksmanship', 'Beast Mastery', 'Survival']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def warlock(role_sample):
        if "Ranged" in role_sample:
            possible_spec = ['Affliction', 'Demonology', 'Destruction']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def monk(role_sample):
        if "Tank" in role_sample:
            spec_sample = "Brewmaster"
        elif "Melee" in role_sample:
            spec_sample = "Windwalker"
        elif "Healer" in role_sample:
            spec_sample = "Mistweaver"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def death_knight(role_sample):
        if "Melee" in role_sample:
            possible_spec = ['Frost', 'Unholy', 'Blood']
            spec_sample = random.choices(possible_spec)
        elif "Tank" in role_sample:
            possible_spec = ['Frost', 'Blood']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def demon_hunter(role_sample):
        if "Tank" in role_sample:
            spec_sample = "Vengeance"
        elif "Melee" in role_sample:
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