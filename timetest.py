import time
startTime = time.time()
print ("start")
print ("waiting...")
def getuserin():
	foo = input(f"input: ")
	#procStart = time.process_time()
	return foo

for x in range(int(getuserin())):
    print (f'{x}', end=' ')
    time.sleep(0.25)
    if x % 5 == 0:
        print ("\n")
    else:
        continue
    x+=1
print ('waiting end')
endTime = time.time()
print(f'time taken = {round(endTime-startTime, 3)} seconds.')
#print(f'process time = {round(endTime-procStart, 3)}')