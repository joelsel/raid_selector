import time
print ("start")
print ("waiting...")
def getuserin():
	foo = input(f"input: ")
	#print (foo)
	return foo

for x in range(getuserin()):
    print (f'waiting for {x} second(s)')
    time.sleep(0.25)
    x+=1
print ('waiting end')
