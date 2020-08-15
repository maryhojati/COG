#import necessary modules
import csv
import matplotlib.pylab as plt
import numpy as np
import math 
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
        values=[]

        std=[]
        for row in rows:
            skip=False
            sub=row[0]
            for char in no:
                if char in sub:
                    skip=True
            if skip==False:
                k=k+[sub]
                gcc=(sub.count('G')+sub.count('C'))*100*int(row[1])/len(sub)
                if len(k[-2])==len(k[-1]):
                    std=std+[round(gcc,4)]
                else:
                    std=[round(gcc,4)]
                    values.append(std)
            
        print(filename+ 'reading...')
        lstk= list(len(i) for i in k)
        y=tuple([mean(std) for std in values])
        x=(2,3,4,5,6,7)
        vplot.append([x,y])

        colors = (0,0,0)
        area = np.pi*3
        plt.xlabel("size k: len(k-mer)")
        plt.ylabel("GC content (mean in set of k-mers)")
        plt.scatter(x, y, s=area, c=col[t], alpha=0.5) 
        plt.plot(x,y,label=filenames[t])
        plt.legend()
        t+=1
plt.show()

