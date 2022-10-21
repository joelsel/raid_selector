#implement read method from reference file, map output to local variable, read nested list element from local variable
from expansionList import xpick

class expac_data_write:
    def __init__ (self, expacData):
        self.expacData = expacData

    def castExpacData(self):
        classList =   self.expacData[0]
        roleList =    self.expacData[1]
        class_wt =    self.expacData[2]
        tank_only =   self.expacData[3]
        healer_only = self.expacData[4]
        melee_only =  self.expacData[5]
        ranged_only = self.expacData[6]
        expacName =   self.expacData[7]
        '''
        return classList, roleList, class_wt, tank_only, healer_only, melee_only, ranged_only, expacName
        print(f'classList = {classList}\n')
        print(f'roleList = {roleList}\n')
        print(f'class_wt = {class_wt}\n')
        print(f'tank only = {tank_only}\n')
        print(f'healer only = {healer_only}\n')
        print(f'melee only = {melee_only}\n') 
        print(f'expansion name = {expacName}\n')
        '''

    def returndata(self):
        print ('returning data')
        return self.expacData
        
'''
    def testdata(self):
        #r = (f"\n\n whole expac data is: {self.expacData}")
        r = (f'\n \
            current classList =   {self.expacData[0]} \n\n \
            current roleList =    {self.expacData[1]} \n \
            current class_wt =    {self.expacData[2]} \n \
            current tank_only =   {self.expacData[3]} \n \
            current healer_only = {self.expacData[4]} \n \
            current melee_only =  {self.expacData[5]} \n \
            current ranged_only = {self.expacData[6]} \n \
            ')
        print (r)
'''        
'''    
    def readData(self):
        #r = (f"\nreading class data: {self.expacData[0]}, reading role data: {self.expacData[1]}")
        #r1 = (f"\nread element 2 of class: {self.expacData[0][1]}, read element 3 of role: {self.expacData[1][2]}")
        #print (r)
        #print (r1)
        r = 'none'
'''
w = expac_data_write(xpick())
#w.readData()
#w.testdata()
w.castExpacData()


