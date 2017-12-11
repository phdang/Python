# -*- coding: utf-8 -*-
"""
Created on Mon May 23 11:18:46 2016

@author: Dang
"""
import os
import shutil
import csv
A = []
B = []
C = []
D = []
def extract(x,z):
    with open("dens_z.xvg","r") as myfile:
        Allrowlist = csv.reader(myfile)
        for currentRow in Allrowlist:
            A.append(','.join(currentRow))
        k = -1
        for i in range(A.index('@ legend 0.78, 0.8'),len(A),1):
            k += 1
            B.append(A[A.index('@ legend 0.78, 0.8')+k].split())
        for i in range(len(B)):
            if len(B[i])>0:
                C.append(B[i][x-1])
    myfile.close()
    filename = z + '.txt'
    file = open(filename, mode = 'w')
    for i in range(3,len(C),1) :
       file.write(str(C[i])+"\n")
    file.close()
extract(1,'z')
A = []
B = []
C = []
D = []
extract(2,'dens')
print('File written successfully')
A = []
B = []
import os
import shutil
import csv
def clean(x):
    os.mkdir(x)
    source = os.listdir(os.getcwd())
    for files in source:
        if files.endswith(".txt") or files.endswith(".png"):
            shutil.move(files,x)
def density(x):
    with open("z.txt","r") as myfile:
        Allrowlist = csv.reader(myfile)
        for currentRow in Allrowlist:
            A.append(float(','.join(currentRow))*10)
    myfile.close()
    
    with open("dens.txt","r") as myfile:
        Allrowlist = csv.reader(myfile)
        for currentRow in Allrowlist:
            B.append(float(','.join(currentRow))/1000)
    myfile.close()
    i = -1
    inx = 0
    surface = 0
    while surface == 0:
        i += 1
        if A[i]>20 and B[i]>0:
          surface = A[i]
          inx = i
    lenA = A[len(A)-1]
    for i in range(len(B)):
        if i >= inx:
            A[i] = A[i]-surface
    i = -1
    inxb = 0
    bound = 0
    stop = False
    while bound == 0 or stop == False:
        i += 1
        if A[i]<20 and B[i]==0:
            bound = A[i]
            inxb = i
            stop = True
    for i in range(inxb):
        A.append(A[i]+lenA-surface)
        B.append(B[i])
    for i in range(inx):
        del A[0]
        del B[0]
    filename = 'resdens.txt'
    file = open(filename, mode = 'w')
    for i in range(len(B)-1) :
       file.write(str(B[i])+"\n")
    file.close()
    filename = 'resz.txt'
    file = open(filename, mode = 'w')
    for i in range(len(A)-1) :
       file.write(str(A[i])+"\n")
    file.close()
    filename = 'resdenstip3p.txt'
    file = open(filename, mode = 'w')
    for i in range(len(B)-1) :
       file.write(str(B[i])+"\n")
    file.close()
    filename = 'resztip3p.txt'
    file = open(filename, mode = 'w')
    for i in range(len(A)-1) :
       file.write(str(A[i])+"\n")
    file.close()
    import numpy as np
    import matplotlib
    matplotlib.use('agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    fig, ax = plt.subplots()
    #fig, ay = plt.subplots()
    
    plt.plot(A,B)
    plt.xticks(np.arange(int(min(A)), int(max(A)+1), 5.0))   
    plt.yticks(np.arange(int(min(B)), int(max(B)+1), 0.5)) 
    minorLocator = MultipleLocator(1)
    ax.xaxis.set_minor_locator(minorLocator)
    minorLocator = MultipleLocator(0.1)
    ax.yaxis.set_minor_locator(minorLocator)
    plt.xlabel('Distance with respect to the surface [A]')
    plt.ylabel('Density [$\mathregular{g/cm^3}$]')
    plt.savefig('density_' + x + '.png', format='png', dpi=150)
    plt.close()

    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    fig, ax = plt.subplots()
    #fig, ay = plt.subplots()

    plt.plot(A,B)
    plt.xticks(np.arange(int(min(A)), int(max(A)+1), 5.0))
    plt.yticks(np.arange(int(min(B)), int(max(B)+1), 0.5))
    minorLocator = MultipleLocator(1)
    ax.xaxis.set_minor_locator(minorLocator)
    minorLocator = MultipleLocator(0.1)
    ax.yaxis.set_minor_locator(minorLocator)
    plt.xlabel('Distance with respect to the surface [A]')
    plt.ylabel('Density [$\mathregular{g/cm^3}$]')
    plt.savefig('Density_' + x + '.png', format='png', dpi=2000)
    plt.close()

def make(x):
    source = os.listdir(os.getcwd())
    if x not in source:
        os.mkdir(x)
        os.mkdir(x+'/Figure')
        os.mkdir(x+'/Data')
    source = os.listdir(os.getcwd())
    for files in source:
        if  files.endswith(".png"):
            shutil.move(files,x+'/Figure') 
        if files.endswith(".txt") or files.endswith("z.xvg") :
            shutil.move(files,x+'/Data')
density('HAP_001_TIP3P_me_z6ns')
make('Density_HAP_001_TIP3P_me_z6ns')
print('Graphs exported successfully')
