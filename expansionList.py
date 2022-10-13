#def main():
#    print ("\nexpansionList imported")
#    pass
#if __name__ == "__main__":
def xpick():
    expacSelect = input("Input desired expansion: TBC, Wrath, Cataclysm, Mists, WoD, Legion -: ")
    expacSelect = expacSelect.lower()
    r = []
    tbc_match = ['tbc', 'bc', 'burning', 'crusade']
    wrath_match = ['wrath', 'wotlk', 'lich', 'king']
    cata_match = ['cata', 'cataclysm']
    mists_match = ['mist', 'pandaria']
    warlords_match = ['wod', 'warlords', 'draenor']
    legion_match = ['legion']
    if any(x in expacSelect for x in tbc_match):
        r = TBC()
        print (f"\nexpansion chosen was TBC due to {expacSelect} inside TBC keyword list\n")
    elif any(x in expacSelect for x in wrath_match):
        r = Wrath()
        print (f"\nexpansion chosen was Wrath of the Lich King due to {expacSelect} inside Wrath keyword list\n")
    elif any(x in expacSelect for x in cata_match):
        r = Cata()
        print (f"\nexpansion chosen was Cataclysm due to {expacSelect} inside Cataclysm keyword list\n")
    elif any(x in expacSelect for x in mists_match):
        r = Mists()
        print (f"\nexpansion chosen was Mists of Pandaria due to {expacSelect} inside Mists keyword list\n")
    elif any(x in expacSelect for x in warlords_match):
        r = WOD()
        print (f"\nexpansion chosen was Warlords of Draenor due to {expacSelect} inside Warlords keyword list\n")
    elif any(x in expacSelect for x in legion_match):
        r = Legion()
        print (f"\nexpansion chosen was Legion due to {expacSelect} inside Legion keyword list\n")
    else:
        print("selection error")
    return r

def TBC():
    classList = ['Mage', 'Druid', 'Warrior', 'Paladin', 'Priest', 'Shaman', 'Rogue', 'Hunter', 'Warlock']

    roleList = ['Tank', 'Healer', 'Melee', 'Ranged']

    class_wt =      [1, 1, 1, 1, 1, 1, 1, 1, 1]
    tank_only =     [0, 1, 1, 1, 0, 0, 0, 0, 0]
    healer_only =   [0, 1, 0, 1, 1, 1, 0, 0, 0]
    melee_only =    [0, 1, 1, 1, 0, 1, 1, 0, 0]
    ranged_only =   [1, 1, 0, 0, 1, 1, 0, 1, 1]

    expacName = ['TBC']

    expacData = [classList, roleList, class_wt, tank_only, healer_only, melee_only, ranged_only, expacName]
    return expacData

def Wrath():
    classList = ['Mage', 'Druid', 'Warrior', 'Paladin', 'Priest', 'Shaman', 'Rogue', 'Hunter', 'Warlock', 'Death Knight']

    roleList = ['Tank', 'Healer', 'Melee', 'Ranged']

    class_wt =      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    tank_only =     [0, 1, 1, 1, 0, 0, 0, 0, 0, 1]
    healer_only =   [0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
    melee_only =    [0, 1, 1, 1, 0, 1, 1, 0, 0, 1]
    ranged_only =   [1, 1, 0, 0, 1, 1, 0, 1, 1, 0]

    expacName = ['Wrath']

    expacData = [classList, roleList, class_wt, tank_only, healer_only, melee_only, ranged_only, expacName]
    return expacData

def Cata():
    classList = ['Mage', 'Druid', 'Warrior', 'Paladin', 'Priest', 'Shaman', 'Rogue', 'Hunter', 'Warlock', 'Death Knight']

    roleList = ['Tank', 'Healer', 'Melee', 'Ranged']

    class_wt =      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    tank_only =     [0, 1, 1, 1, 0, 0, 0, 0, 0, 1]
    healer_only =   [0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
    melee_only =    [0, 1, 1, 1, 0, 1, 1, 0, 0, 1]
    ranged_only =   [1, 1, 0, 0, 1, 1, 0, 1, 1, 0]

    expacName = ['Cata']

    expacData = [classList, roleList, class_wt, tank_only, healer_only, melee_only, ranged_only, expacName]
    return expacData

def Mists():
    classList = ['Mage', 'Druid', 'Warrior', 'Paladin', 'Priest', 'Shaman', 'Rogue', 'Hunter', 'Warlock', 'Death Knight', 'Monk']

    roleList = ['Tank', 'Healer', 'Melee', 'Ranged']

    class_wt =      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    tank_only =     [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1]
    healer_only =   [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1]
    melee_only =    [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    ranged_only =   [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0]

    expacName = ['Mists']

    expacData = [classList, roleList, class_wt, tank_only, healer_only, melee_only, ranged_only, expacName]
    return expacData

def WOD():
    classList = ['Mage', 'Druid', 'Warrior', 'Paladin', 'Priest', 'Shaman', 'Rogue', 'Hunter', 'Warlock', 'Death Knight', 'Monk']

    roleList = ['Tank', 'Healer', 'Melee', 'Ranged']

    class_wt =      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    tank_only =     [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1]
    healer_only =   [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1]
    melee_only =    [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    ranged_only =   [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0]

    expacName = ['WOD']

    expacData = [classList, roleList, class_wt, tank_only, healer_only, melee_only, ranged_only, expacName]
    return expacData

def Legion():
    classList = ['Mage', 'Druid', 'Warrior', 'Paladin', 'Priest', 'Shaman', 'Rogue', 'Hunter', 'Warlock', 'Death Knight', 'Monk', 'Demon Hunter']

    roleList = ['Tank', 'Healer', 'Melee', 'Ranged']

    class_wt =      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    tank_only =     [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]
    healer_only =   [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0]
    melee_only =    [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
    ranged_only =   [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]

    expacName = ['Legion']

    expacData = [classList, roleList, class_wt, tank_only, healer_only, melee_only, ranged_only, expacName]
    return expacData
