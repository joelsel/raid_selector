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
            expacMatchList.append(importlib.import_module(n).expansion.expansionMatch())
            #print (importlib.import_module(n).getExpac.expacMatch()) #diag

        #chosen = []
        expacOut = []
        for n in range(len(expacMatchList)):
            if userin.lower() in expacMatchList[n]:
                    expacOut = (expacMatchList[n][0], removeExt[n])
                    #print (expacOut) #diag
                    #print (expacOut[0]) #diag
                    #print (expacOut[1]) #diag
                    return expacOut
                    '''
                    # -- attempted to allow reverse search of match list from user input.
                    # -- current solution to add plausible inputs to matchlist
            elif len(expacOut) == 0 :
                expacMatchListCombined = " ".join(expacMatchList)
                if userin.lower() in expacMatchListCombined:
                    expacOut = (expacMatchList[n][0], removeExt[n])
                    #print (expacOut) #diag
                    #print (expacOut[0]) #diag
                    #print (expacOut[1]) #diag
                    return expacOut
                    '''
            else:
                pass

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