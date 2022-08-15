
def xpick():
    expacSelect = input("expansions wrath, legion, cata: ")
    expacSelect = expacSelect.lower()
    r = []
    if 'tbc' in expacSelect:
        r = TBC()
    if 'wrath' in expacSelect:
        r = Wrath()
    elif 'cata' in expacSelect:
        r = Cata()
    elif 'mists' in expacSelect:
        r = Mists()
    elif 'wod' in expacSelect:
        r = WOD()
    elif 'legion' in expacSelect:
        r = Legion()
    else:
        print("selection error")
    return r

def TBC():
    classList = []
    roleList = []
    expacData = []
    return expacData

def Wrath():
    classList = ['wrathclass', 'c1', 'c2']
    roleList = ['wrathrole', 'r1', 'r2']
    expacData = [classList, roleList]
    return expacData

def Cata():
    classList = ['cataclass', 'c5', 'c6']
    roleList = ['catarole', 'r5', 'r6']
    expacData = [classList, roleList]
    return expacData

def Mists():
    classList = []
    roleList = []
    expacData = []
    return expacData
def WOD():
    classList = []
    roleList = []
    expacData = []
    return expacData

def Legion():
    classList = ['legionclass', 'c3', 'c4']
    roleList = ['legionrole', 'r3', 'r4']
    expacData = [classList, roleList]
    return expacData



#test = Legion()
#print(test)