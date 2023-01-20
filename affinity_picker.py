'''
import os
check = os.getcwd()
print(check)
newdir = 'C:\\Users\\Joel\\Downloads'
os.chdir(newdir)
check = os.getcwd()
print(check)
contents = os.listdir()
for x in range(len(contents)):
    print (f"{contents[x]} \n")
'''
'''
import psutil
p = psutil.Process(30680)
print(p.cpu_affinity())
p.cpu_affinity([0, 1, 2, 3, 4])
print(p.cpu_affinity())
'''



#psutil.Process(30680).cpu_count()
process_list = []
import psutil
search = input('Process Search Term? : ')
for proc in psutil.process_iter(['name', 'pid', 'cwd', 'cpu_percent']):
    if search.lower() in proc.info['name'].lower():
        process_list.append(proc.info)
for d in range(len(process_list)):
    print (f"item #{d+1}: {process_list[d]}\n")
sel = input ('item?: ')
chosenProc = process_list[(int(sel)-1)]["pid"]
#print (chosenProc)
cpuNewAff = []
maxCpuCount = int(psutil.cpu_count()-1)

a, b, x, y = 0, 0, 0, 0
print(f"Existing core affinity set to :{(psutil.Process(chosenProc).cpu_affinity())}")
x = input("Lower Process Core Bound, inclusive: ")
if float(x) < 0:
    print("Lowest core cannot be less than 0, value set to 0.\n")
    x == 0
else:
    pass
y = input(f"Upper Process Core Bound, inclusive (max {maxCpuCount}): ")


if int(x) > maxCpuCount:
    print (f"Minimum CPU core cannot be above {maxCpuCount}, value set to {maxCpuCount}")
else:
    pass
if int(y) > maxCpuCount:
    print (f"Highest core cannot exceed {maxCpuCount}, value set to {maxCpuCount}")
    y = maxCpuCount
else:
    pass

cpuNewAff.append(int(x))
a = int(x)+1
b = int(y)+1
while a < b:
    cpuNewAff.append(a)
    a+=1
print (cpuNewAff)
psutil.Process(chosenProc).cpu_affinity(cpuNewAff)
print(f"New core affinity set to :{(psutil.Process(chosenProc).cpu_affinity())}")

#import psutil
#for proc in psutil.process_iter(['name', 'pid', 'cpu_affinity']):
#    print (proc.info)



#a = [1, 2, 3, 56]
#print(max(a))
#import psutil
#print(psutil.cpu_count()-1)
