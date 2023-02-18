
'''
#from expac_selection import 
check = int(input("?"))
if check == 1:
    #checkval = 1
    import importone as f
elif check == 2:
    #checkval = 2
    import importtwo as f


#f.callx()
#print(x)
newx = f.num.callx()
newx2 = f.num.callx2()
print (newx, newx2)
'''

'''
#from expac_selection import 
import importlib
check = int(input("?"))
if check == 1:
    x = 'importone'
    print(x)
    f = importlib.import_module(x)
elif check == 2:
    x = 'importtwo'
    print(x)
    f = importlib.import_module(x)
#f.callx()
#print(x)
outx = f.num.callx()
outx2 = f.num.callx2()
#print (newx, newx2)
print (outx, outx2)
'''

'''
class chooseExpansion:
    def main():
        import os, importlib
        home = os.getcwd()
        userin = input("Choose Expansion: ")
        #print (home) #diag

        contents = (os.listdir(home))
        target = []
        for n in contents:
            if 'spec' in n:
                target.append(n)
        #print (target) #diag
        removeExt = []
        for n in target:
            removeExt.append(os.path.splitext(n)[0])
        #print (removeExt) #diag

        expacMatchList = []
        for n in removeExt:
            expacMatchList.append(importlib.import_module(n).getExpac.expacMatch())
            #print (importlib.import_module(n).getExpac.expacMatch()) #diag
            #print (expacMatchList) #diag

        #chosen = []
        for n in range(len(expacMatchList)):
            if userin.lower() in expacMatchList[n]:
                expacOut = (expacMatchList[n][0], removeExt[n])
                print (expacOut) #diag
                print (expacOut[0]) #diag
                print (expacOut[1]) #diag
                return expacOut
            else:
                pass
'''
               


#chooseExpansion.main()


import importlib
test = importlib.import_module('expac_selection').chooseExpansion.main()
#print (test)
print (f'expansion name is {test[0]} and expansion list will be {test[1]}')


#from expac_selection import chooseExpansion
#chooseExpansion.main()



'''
allExpac = ['tbc_match', 'wrath_match', 'cataclysm_match', 'mists_match', 'warlords_match', 'legion_match']

tbc_match = ['tbc', 'bc', 'burning', 'crusade']
wrath_match = ['wrath', 'wotlk', 'lich', 'king']
cata_match = ['cata', 'cataclysm']
mists_match = ['mist', 'pandaria']
warlords_match = ['wod', 'warlords', 'draenor']
legion_match = ['legion']
'''