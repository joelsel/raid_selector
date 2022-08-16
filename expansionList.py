
def xpick():
    expacSelect = input("Input desired expansion: TBC, Wrath, Cataclysm, Mists, WoD, Legion -: ")
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
    classList = ['tbcclass', 'tbcc1', 'tbcc2']
    roleList = ['tbcrole', 'tbcr1', 'tbcr2']
    expacData = [classList, roleList]
    return expacData

def Wrath():
    classList = ['wrathclass', 'wrathc1', 'wrathc2']
    roleList = ['wrathrole', 'wrathr1', 'wrathr2']
    expacData = [classList, roleList]
    return expacData

def Cata():
    classList = ['cataclass', 'catac1', 'catac2']
    roleList = ['catarole', 'catar1', 'catar2']
    expacData = [classList, roleList]
    return expacData

def Mists():
    classList = ['mistclass', 'mistc1', 'mistc2']
    roleList = ['mistrole', 'mistr1', 'mistr2']
    expacData = [classList, roleList]
    return expacData
def WOD():
    classList = ['WODclass', 'wodc1', 'wodc2']
    roleList = ['WODrole', 'wodr1', 'wodr2']
    expacData = [classList, roleList]
    return expacData

def Legion():
    classList = ['legionclass', 'legionc1', 'legionc2']
    roleList = ['legionrole', 'legionr1', 'legionr2']
    expacData = [classList, roleList]
    return expacData
