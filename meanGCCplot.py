#import necessary modules
import csv
import matplotlib.pylab as plt
import numpy as np
from math import sqrt
import os
from statistics import stdev
from statistics import mean

import csv
vplot=[]
col=['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
no=['R','Y','K','M','S','W','B','D','H','V','M','N','U']

t=0
filenames=[]
for filename in os.listdir("csvdata"):
    with open(filename,'rt')as f:
        filenames.append(filename[:-4])
        rows=[]
        data = csv.reader(f)
        for row in data:
                rows.append(row)
        k=['']
        lstgcc=[]
        valuesgcc=[]
        sumOcc=0
        lstOcc=[]
        maxgcc=mingcc=[(rows[0][0].count('G')+row[0][0].count('C'))*100/len(rows[0][0])]

        for row in rows:
            skip=False
            sub=row[0]
            for char in sub:
                if char in no:
                    skip=True
            if skip==False:
                k=k+[sub]
                curGCC=(sub.count('G')+sub.count('C'))*100/len(sub)

                
                fgcc=curGCC*int(row[1])
                if len(k[-2])==len(k[-1]):
                    lstgcc=lstgcc+[round(fgcc,4)]
                    sumOcc=sumOcc+int(row[1])
                    #sum ro ezafe kon

                    ##min:
                    if(curGCC<mingcc[-1] and  curGCC!=0):
                        mingcc[-1]=curGCC
                    elif(curGCC>maxgcc[-1]):
                        maxgcc[-1]=curGCC
                else:
                    

                    if(len(k)!=2):
                        valuesgcc.append(lstgcc)
                        mingcc=mingcc+[curGCC]
                        maxgcc=maxgcc+[curGCC]
                    lstgcc=[round(fgcc,5)]
                    if(sumOcc!=0 ):
                        lstOcc+=[sumOcc]
                    sumOcc=int(row[1])
        

        lstOcc+=[sumOcc]
        valuesgcc.append(lstgcc)
        print(filename+ 'reading...')

        #max  and min number of gcc-s

        maxgccs=tuple(maxgcc)
        mingccs=tuple(mingcc)
        #mean calculation
        y=tuple([sum(valuesgcc[i])/lstOcc[i] for i in range(len(valuesgcc))])

        #stedv
        std=[]
        for k in range(len(valuesgcc)):
            power=0
            for j in range(len(valuesgcc[k])):
                power+=(valuesgcc[k][j]-y[k])**2
            std+=[sqrt(power/lstOcc[k])]
        

        x=(2,3,4,5,6,7)
        vplot.append([x,y])

        colors = (0,0,0)
        area = np.pi*3
        #draw max and min:
        f1=plt.figure(1)
        plt.plot(x,maxgccs,color=col[t],label=filenames[t])
        plt.plot(x,mingccs,color=col[t],label=filenames[t])
        plt.fill_between(x, maxgcc,mingcc,color='k',alpha=.5)
        
        #draw mean
        f2=plt.figure(2)
        plt.xlabel("size k: len(k-mer)")
        plt.ylabel("mean GC content mean in k-mer set")
        plt.scatter(x, y, s=area, c=col[t]) 
        #plt.scatter(x, y1, s=area, c=col[t])
        plt.plot(x,y,label=filenames[t])
        plt.legend()
        #draw stdev
        f3=plt.figure(3) 
        plt.xlabel("size k: len(k-mer)")
        plt.ylabel("stdev GC content in k-mer set")
        plt.plot(x,std,label=filenames[t])

        plt.legend()
        t+=1

plt.show()

