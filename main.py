import os
 
path = r"C:/Users/Inform4/Documents/GB/Krylovo-slider/img/"
f = os.listdir(path)
n = 1
 
for i in f:
    # name = 1000 + int(i.split()[0])
    oldname = path + i
    newname = path + str(n) + '.jpg'
    os.rename(oldname, newname)
    print(oldname, '======>', newname)
    n += 1