#odd = ["one", "three", "five"]
#even = ["two", "four", "six"]
'''
def xpick():
    expacSelect = input("expansions wrath, legion, cata: ")
    r = []
    if "wrath" in expacSelect:
        r = Wrath()
    elif "legion" in expacSelect:
        r = Legion()
    elif "cata" in expacSelect:
        r = Cata()
    else:
        print("selection error")
    return r

def Wrath():
    classList = ['wrathclass', 'c1', 'c2']
    roleList = ['wrathrole', 'r1', 'r2']
    expacData = [classList, roleList]
    return expacData

def Legion():
    classList = ['legionclass', 'c3', 'c4']
    roleList = ['legionrole', 'r3', 'r4']
    expacData = [classList, roleList]
    return expacData

def Cata():
    classList = ['cataclass', 'c5', 'c6']
    roleList = ['catarole', 'r5', 'r6']
    expacData = [classList, roleList]
    return expacData
#test = Legion()
#print(test)

'''