import random
from datetime import datetime
global now
now = datetime.now()

def timestamp(now):
    f = open("hello.txt", "a")
    getTime = (("\n{}{}\n\n").format("Timestamp: ",now))
    f.write("".join(getTime))
    #print(now)
    print("getTime check: {}".format(getTime))
    f.close()

prog_init = 1

#TODO terminus location
global terminus
terminus = ("\n\n{:-^60}\n\n".format(" end of output "))


def raidReport(count_tank, count_healer, count_melee, count_ranged):
    f = open("hello.txt", "a")
    report = (("\nTank count: {}, Healer count: {}, Melee count: {}, Ranged count: {}").format(count_tank, count_healer, count_melee, count_ranged))
    f.write("".join(report))
    f.close()


def sampleRole(role_wt):
    global role_sample
    role_sample = random.choices(role_list, weights=role_wt)
    return role_sample


def sampleClass():
    global class_sample
    class_sample = random.choices(class_list, weights=class_wt)
    return class_sample


def role_check(count_tank, count_healer, count_melee, count_ranged):
    global tank_wt, healer_wt, melee_wt, ranged_wt, role_wt
    if count_tank >= 2:
        tank_wt = 0
    if count_healer >= 6:
        healer_wt = 0
    if count_melee >= 0:
        pass
    if count_ranged >= 0:
        pass
    role_wt = [tank_wt, healer_wt, melee_wt, ranged_wt]


def class_check(role_sample):
    global class_wt
    if "Tank" in role_sample:
        class_wt = tank_only
    if "Healer" in role_sample:
        class_wt = healer_only
    if "Melee" in role_sample:
        class_wt = melee_only
    if "Ranged" in role_sample:
        class_wt = ranged_only



def role_counter():
    global count_tank, count_healer, count_melee, count_ranged
    if "Tank" in role_sample:
        count_tank += 1
    if "Healer" in role_sample:
        count_healer += 1
    if "Melee" in role_sample:
        count_melee += 1
    if "Ranged" in role_sample:
        count_ranged += 1



# -------------deprecated hardcoded class data, moved to expansion class data-----------------
'''
# RaidSelector - defining default values
class_list = ["Mage", "Druid", "Warrior", "Paladin",
        "Priest", "Shaman", "Rogue", "Hunter", "Warlock",
        "Demon Hunter", "Death Knight", "Monk"]

role_list = ['Tank', 'Healer', 'Melee', 'Ranged']

line_output = []
spec_sample = []
tank_wt, healer_wt, melee_wt, ranged_wt = [1, 1, 1, 1]
global role_wt
global count_tank, count_healer, count_melee, count_ranged
role_wt = [tank_wt, healer_wt, melee_wt, ranged_wt]
count_tank, count_healer, count_melee, count_ranged = [0, 0, 0, 0]

class_wt =      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
tank_only =     [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]
healer_only =   [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1]
melee_only =    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
ranged_only =   [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]

def empty_choice():
    while True:
        print("empty choice selected")
        break

def mage_spec():
    global spec_sample
    if "Ranged" in role_sample:
        possible_spec = ['Arcane', 'Fire', 'Frost']
        spec_sample = random.choices(possible_spec)
    else:
        spec_sample = "Invalid!"

def druid_spec():
    global spec_sample
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

def warrior_spec():
    global spec_sample
    if "Melee" in role_sample:
        possible_spec = ["Arms", "Fury"]
        spec_sample = random.choices(possible_spec)
    elif "Tank" in role_sample:
        spec_sample = "Protection"
    else:
        spec_sample = "Invalid!"

def paladin_spec():
    global spec_sample
    if "Melee" in role_sample:
        spec_sample = "Retribution"
    elif "Healer" in role_sample:
        spec_sample = "Holy"
    elif "Tank" in role_sample:
        spec_sample = "Protection"
    elif "Ranged" in role_sample:
        spec_sample = "Invalid!"

def priest_spec():
    global spec_sample
    if "Healer" in role_sample:
        possible_spec = ['Holy', 'Discipline']
        spec_sample = random.choices(possible_spec)
    elif "Ranged" in role_sample:
        spec_sample = "Shadow"
    else:
        spec_sample = "Invalid!"

def shaman_spec():
    global spec_sample
    if "Ranged" in role_sample:
        spec_sample = "Elemental"
    elif "Melee" in role_sample:
        spec_sample = "Enhancement"
    elif "Healer" in role_sample:
        spec_sample = "Restoration"
    else:
        spec_sample = "Invalid!"

def rogue_spec():
    global spec_sample
    if "Melee" in role_sample:
        possible_spec = ['Assassination', 'Outlaw', 'Subtlety']
        spec_sample = random.choices(possible_spec)
    else:
        spec_sample = "Invalid!"

def hunter_spec():
    global spec_sample
    if "Ranged" in role_sample:
        possible_spec = ['Marksmanship', 'Beast Mastery']
        spec_sample = random.choices(possible_spec)
    elif "Melee" in role_sample:
        spec_sample = "Survival"
    else:
        spec_sample = "Invalid!"

def warlock_spec():
    global spec_sample
    if "Ranged" in role_sample:
        possible_spec = ['Affliction', 'Demonology', 'Destruction']
        spec_sample = random.choices(possible_spec)
    else:
        spec_sample = "Invalid!"

def demon_hunter_spec():
    global spec_sample
    if "Melee" in role_sample:
        spec_sample = "Havoc"
    elif "Tank" in role_sample:
        spec_sample = "Vengeance"
    else:
        spec_sample = "Invalid!"

def death_knight_spec():
    global spec_sample
    if "Melee" in role_sample:
        possible_spec = ['Frost', 'Unholy']
        spec_sample = random.choices(possible_spec)
    elif "Tank" in role_sample:
        spec_sample = "Blood"
    else:
        spec_sample = "Invalid!"

def monk_spec():
    global spec_sample
    if "Tank" in role_sample:
        spec_sample = "Brewmaster"
    elif "Melee" in role_sample:
        spec_sample = "Windwalker"
    elif "Healer" in role_sample:
        spec_sample = "Mistweaver"
    else:
        spec_sample = "Invalid!"




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
    elif "Demon Hunter" in class_sample:
        demon_hunter_spec()
    elif "Death Knight" in class_sample:
        death_knight_spec()
    elif "Monk" in class_sample:
        monk_spec()
    else:
        print("class_picker error")

    role_counter()
'''
"""
#class_redirect debugging
    print("".join(class_sample))
    print("".join(role_sample))
    print("".join(spec_sample))
    print("Tank count: ", count_tank)
    print("Melee count: ", count_melee)
    print("Ranged count: ", count_ranged)
    print("Healer count: ", count_healer)
    print("Tankwt = ",tank_wt)
    print("Healerwt = ",healer_wt)
    print("meleewt = ", melee_wt)
    print("rangedwt = ",ranged_wt)
    print("rolewt = {}".format(role_wt))

"""
# development class_picker
def class_picker_main(class_sample, role_sample, spec_sample, cyc):
    global line_output
    out_class = ("".join(class_sample))
    out_role = ("".join(role_sample))
    out_spec = ("".join(spec_sample))
    line_output.append("Member {:03}: {} {:<10} {:<15} {:<10}\n".format((cyc + 1), " >> ", out_role, out_class, out_spec))
 
# development file write
def write_file(line_output,cycle_count):
    while True:
            try:
                if write_mode == 0:
                    with open("hello.txt", "a") as f:
                        print("selection is: ", write_mode, " overwrite mode active.")
                        f.write("".join(line_output))
                        print("\n{} line(s) output to file.\n".format(cycle_count))
                        f.write("\n{} line(s) output to file.\n".format(cycle_count))
                    break

                elif write_mode == 1:
                    with open("hello.txt", "a") as f:
                        print("selection is: ", write_mode, " append mode active.")
                        f.write("".join(line_output))
                        print("\n{} line(s) output to file.\n".format(cycle_count))
                        f.write("\n{} line(s) output to file.\n".format(cycle_count))

                elif run_choice == 0:
                    print("Under Construction, please try again.")

            except ValueError:
                print("E-03: Invalid input, returning to main menu")
                continue

            break
            # else:
            #     print("E-04: Input not recognized")
            #     continue


# MAIN
def class_picker_v2():
    global cycle_count
    cycle_count = int(input("Number of cycles, 0 to exit: "))

    if cycle_count < 0:
        print(" try again , value cannot be less than 0")

    elif cycle_count == 0:
        print(" Thank you")

    elif cycle_count > 0:
        for cyc in range(cycle_count):
            role_check(count_tank, count_healer, count_melee, count_ranged)
            sampleRole(role_wt)
            class_check(role_sample)
            sampleClass()
            class_redirect(class_sample)
            class_picker_main(class_sample, role_sample, spec_sample, cyc)
       
        write_file(line_output, cycle_count) 

    print("End of class_picker\n")


while prog_init == 1:
        
    try:
        run_choice = int(input("Main Menu: Press 1 for class_dev, Press 2 for Class Picker: "))
        print("selection is going to be: ", run_choice)

    except ValueError:
        print("E-01: Invalid input / no input, please try again.")
        continue

    if run_choice < 0:
        print("E-02: Choice must be greater than 0, please try again.")
        continue

    elif run_choice == 1:
        print("Selection is: ", run_choice, " executing class_redirect.")
        class_redirect()

    elif run_choice == 2:
        while run_choice == 2:
            try:
                print("Selection is ", run_choice, " executing Class Picker.")
                write_mode = int(input("1 for Append, 0 for overwrite: "))

                if write_mode == 0:
                    timestamp(now)
                    with open("hello.txt", "a") as f:
                        print("selection is: ", write_mode, " overwrite mode active.")
                        f.write("\n")
                        class_picker_v2()
                        raidReport(count_tank, count_healer, count_melee, count_ranged)
                        f.write(terminus)
                    break

                elif write_mode == 1:
                    timestamp(now)
                    with open("hello.txt", "a") as f:
                        print("selection is: ", write_mode, " append mode active.")
                        class_picker_v2()
                        raidReport(count_tank, count_healer, count_melee, count_ranged)
                        f.write(terminus)

            except ValueError:
                print("E-03: Invalid input, returning to main menu")
                continue
            break

    elif run_choice == 0:
        print("Under Construction, please try again.")
    break

print("\nend of program")