from numpy import *
import os
import time



os.system("uniq t.txt > tmp.txt ; cp tmp.txt t.txt")
os.system("uniq L.txt > tmp.txt ; cp tmp.txt L.txt")
os.system("uniq D.txt > tmp.txt ; cp tmp.txt D.txt")
os.system("uniq M.txt > tmp.txt ; cp tmp.txt M.txt")


tarr = loadtxt("t.txt")
Larr = loadtxt("L.txt")
Darr = loadtxt("D.txt")
Marr = -loadtxt("M.txt")

minlen = min(len(tarr), len(Darr), len(Larr), len(Marr))

tarr = tarr[:minlen]
Larr = Larr[:minlen]
Darr = Darr[:minlen]
Marr = Marr[:minlen]

aoa = 10.02

def aoaf(t):
    return aoa

tarr = tarr[:len(Larr)]
aoaarr = array(tarr)
for i in range(0, len(tarr)):
    #if tarr[i] < 3.0:
    #    aoaarr[i] = 7.0
    #if tarr[i] >= 3.0 and tarr[i] <= 11.0:
    #    aoaarr[i] = 7.0 + 2*(tarr[i] - 3.0)
    #if tarr[i] >= 11.0:
    aoaarr[i] = aoaf(tarr[i])
    #aoaarr[i] = aoa

def myclean(arr, arrmean, arrmax):
    i = 0
    for x in arr:
        if abs(x) > 2*abs(arrmean):
            arr[i] = arrmean
        i += 1
        
M = int(9.0*len(Larr)/10.)
print("M:", M)

L = mean(Larr[M:])
D = mean(Darr[M:])
MP = mean(Marr[M:])

def myclip(arr, arrmean, arrmax):
    i = 0
    for x in arr:
        if i < len(arr) - 20:
            arrmeanw = mean(arr[i:i + 20])
            print(arr[i], abs(arr[i] - arrmeanw), arrmax*abs(arrmeanw))
            if abs(arr[i] - arrmeanw)/abs(arr[i]) > (arrmax - 1.):
                arr[i] = arrmeanw
        i += 1

print("max before: ", max(Larr))

print("max after: ", max(Larr))

print("L:", L)
print("D:", D)
print("M:", MP)

A = 0.9144 * 0.6010
C = 275.8*1e-3

CL = 2*L/A
CD = 2*D/A
CM = 2*MP/(A*C)


print("CL:", CL, "CD:", CD, "CM:", CM, "L/D:", L/D)

import matplotlib
matplotlib.use('Agg')

from pylab import *

rcParams['font.size'] = 40
rcParams['axes.titlesize'] = "Large"
rcParams['axes.labelsize'] = "Large"
rcParams['figure.figsize'] = 12, 10
rcParams["font.weight"] = "bold"


subplot(3, 1, 1)

plot(tarr[int(.5*len(Larr)/10.):], 2/A*Larr[int(.5*len(Larr)/10.):], linewidth=8.)

grid(True)
title("CL", loc='right')
xlim((xlim()[0], 1.45*xlim()[1]))

legend(["sim"])


ax = gca()
fig = gcf()

fig.canvas.draw()

labels = [item.get_text() for item in ax.get_xticklabels()]

j = 0
for label in labels:
    #print(label)
    if label.isnumeric():
        t = float(label)
        i = searchsorted(tarr, t, side='left')
        if i == 0:
            #aoa = aoaarr[i]
            aoa = aoaf(t)
            newlabel = (label + " " + "(" + str(int(aoa)) + "Â°" + ")")
            labels[j] = newlabel
        else:
            #aoa = aoaarr[i-1]
            aoa = aoaf(t)
            newlabel = (label + " " + "(" + str(int(aoa)) + "Â°" + ")")
            labels[j] = newlabel
            print("t: ", t, " aoa: ", aoa, "label: ", newlabel)
    j += 1
    

subplot(3, 1, 2)

plot(tarr[int(.5*len(Darr)/10.):], 2/A*Darr[int(.5*len(Darr)/10.):], linewidth=8.)

grid(True)
title("CD", loc='right')
xlim((xlim()[0], 1.45*xlim()[1]))


ax = gca()
fig = gcf()

fig.canvas.draw()

labels = [item.get_text() for item in ax.get_xticklabels()]

j = 0
for label in labels:
    
    if label.isnumeric():
        t = float(label)
        i = searchsorted(tarr, t, side='left')
        if i == 0:
            aoa = aoaf(t)
            newlabel = (label + " " + "(" + str(int(aoa)) + "Â°" + ")")
            labels[j] = newlabel
        else:
            aoa = aoaf(t)
            newlabel = (label + " " + "(" + str(int(aoa)) + "Â°" + ")")
            labels[j] = newlabel
            print("t: ", t, " aoa: ", aoa, "label: ", newlabel)
    j += 1
    

subplot(3, 1, 3)

plot(tarr[int(.5*len(Marr)/10.):], 2/(A*C)*Marr[int(.5*len(Marr)/10.):], linewidth=8.)

grid(True)
title("CM", loc='right')
xlim((xlim()[0], 1.45*xlim()[1]))


ax = gca()
fig = gcf()

fig.canvas.draw()

labels = [item.get_text() for item in ax.get_xticklabels()]
j = 0
for label in labels:

    if label.isnumeric():
        t = float(label)
        i = searchsorted(tarr, t, side='left')
        if i == 0:
            
            aoa = aoaf(t)
            newlabel = (label + " " + "(" + str(int(aoa)) + "Â°" + ")")
            labels[j] = newlabel
        else:
            
            aoa = aoaf(t)
            newlabel = (label + " " + "(" + str(int(aoa)) + "Â°" + ")")
            labels[j] = newlabel
            print("t: ", t, " aoa: ", aoa, "label: ", newlabel)
    j += 1
    
modTimesinceEpoc = os.path.getmtime("log1")

modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
print(modificationTime)

tight_layout()

savefig("forces.svg")
show()
