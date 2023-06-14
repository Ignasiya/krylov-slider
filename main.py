import os
 
path = r"C:/Users/Inform4/Documents/GB/Krylovo-slider/img/"
f = os.listdir(path)
n = 0
 
for i in f:
    oldname = path + f[n]
    newname = path + str(n + 1) + '.jpg'
    os.rename(oldname, newname)
    print(oldname, '======>', newname)
    n += 1