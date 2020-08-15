import matplotlib.pyplot as plt
import numpy as np
import csv
import os

dic=dict()#dictionary of visited characters
with open('Content.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for filename in os.listdir("data"):
        with open(os.path.join('data', filename), 'r') as f:
            #parse first line for name:
            s=f.readline()
            groups=s.split(' ')
            name=' '.join(groups[1:3])


            l=[0,0,0,0]
            #check occurence:
            for line in f:
                if not '>' in str(line):
                    line=line.strip()
                    for i in str(line):
                        if(i.upper()=='A'):
                            l[0]+=1
                        elif i.upper()=='T':
                            l[1]+=1
                        elif i.upper()=='C':
                            l[2]+=1
                        elif i.upper()=='G':
                            l[3]+=1


            #calculate percentage
            su=sum(l[0:])
            for i in range(len(l)):
                l[i]=round((l[i]/su*100),5)
            dic.update({name:l})
    #write on csv file:
    for key,value in dic.items():
        writer.writerow([key,value])

#parameters of plot:
category_names = ['A','T','C','G']

#drawing plot:
def survey(results, category_names):
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdBu')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            ax.text(x, y, '%.3f'%c, ha='center', va='center',
                    color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax


survey(dic, category_names)
plt.show()