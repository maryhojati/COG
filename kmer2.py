import os
import csv
import matplotlib.pylab as plt
import numpy as np
p=0
organisms={}
for filename in os.listdir("tst1"):
    with open(os.path.join('tst1', filename), 'r') as f:
        l=[{},{},{},{},{},{}]
        s=f.readline()
        groups=s.split(' ')
        name=' '.join(groups[1:3])
        with open(name+'.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            organisms.update({name:[]})
            print(name+' kmer calculating...')
            for line in f:
                if not '>' in str(line):
                    line=line.strip()
                    for i in range(2,8):
                        d=l[i-2]
                        #AGCTTTTCA
                        #AACATTGTCC
                        for j in range(0,len(line)-i):
                            sub=line[j:j+i].upper()
                            if sub in d:
                                d[sub]=d[sub]+1
                            else:
                                d.update({sub:1})
                                #d.update({sub:(1,round((sub.count('G')+sub.count('C'))*100/len(sub),3))})
            
            for dic in l:
                for key,value in dic.items():
                    writer.writerow([key,value])
            print(name+' kmer done!')
            
#Drosophila 
#start 4:25
#end   4:40

#Homo sapiens 
#start 4:40
#end   



#Arabidopsis thaliana 
#start 4:50
#end   5:08

#Caenorhabditis elegans
#start 5:08
#end   


