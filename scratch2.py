'''
class sample_expansion:
    def druid_spec(role_sample):
        #global spec_sample
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
'''
'''
class pull_expac_spec:
    def mage(role_sample):
        #global spec_sample
        if "Ranged" in role_sample:
            possible_spec = ['Arcane', 'Fire', 'Frost']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def druid(role_sample):
        #global spec_sample
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
        #global spec_sample
        if "Melee" in role_sample:
            possible_spec = ["Arms", "Fury"]
            spec_sample = random.choices(possible_spec)
        elif "Tank" in role_sample:
            spec_sample = "Protection"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def paladin(role_sample):
        #global spec_sample
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
        #global spec_sample
        if "Healer" in role_sample:
            possible_spec = ['Holy', 'Discipline']
            spec_sample = random.choices(possible_spec)
        elif "Ranged" in role_sample:
            spec_sample = "Shadow"
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def shaman(role_sample):
        #global spec_sample
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
        #global spec_sample
        if "Melee" in role_sample:
            possible_spec = ['Assassination', 'Combat', 'Subtlety']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def hunter(role_sample):
        #global spec_sample
        if "Ranged" in role_sample:
            possible_spec = ['Marksmanship', 'Beast Mastery', 'Survival']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample

    def warlock(role_sample):
        #global spec_sample
        if "Ranged" in role_sample:
            possible_spec = ['Affliction', 'Demonology', 'Destruction']
            spec_sample = random.choices(possible_spec)
        else:
            spec_sample = "Invalid!"
        return spec_sample
'''

'''
raidSize = int(input("number: "))

with open ('trial.txt', 'a') as f:
    f.write(f"\n\n")
    for x in range(raidSize):
        foo = ['foo']
        bar = ['bar']
        baz = ['baz']
        f.write((f'\n{(x+1):<4}{foo[0]:_<15}{bar[0]:+^15}{baz[0]:~>25}'))


    
'''
'''
from testLocal import test
array = ['1', '2', '3']
print(test.picker(array))
'''

checkList = [['list_test']]
checkString = 'string_test'

'''

def makeString(getTerm):
    if type(getTerm) == list:
        temp = getTerm[0]
        phrase = str(temp)
    elif type(getTerm) == str:
        phrase = getTerm
    else:
        phrase = "error"
    return phrase

def capAll(getString):
    print(f"getString is {getString}")
    rawTemp = str(getString).replace('_' ,' ')
    tempWords = rawTemp.split()
    readable = []
    readableOut = []
    for x in range(len(tempWords)):
        readable.append(tempWords[x].capitalize())
        readableOut = " ".join(readable)
    return readableOut

'''


def makeReadable(getTerm):
    hold = []
    readableOut = []
    if type(getTerm) == list:
        #temp = getTerm[0]
        phrase = str(getTerm[0]).lower()
    elif type(getTerm) == str:
        phrase = getTerm.lower()
    else:
        phrase = 'error'
   # print(f"getString is {getString}")
    #rawTemp = str(phrase).replace('_' ,' ')
    #tempWords = rawTemp.split()
    tempWords = (phrase.replace('_', ' ')).split()

    for x in range(len(tempWords)):
        hold.append(tempWords[x].capitalize())
        readableOut = ' '.join(hold)
    return readableOut


print(makeReadable(checkList))
print(makeReadable(checkString))