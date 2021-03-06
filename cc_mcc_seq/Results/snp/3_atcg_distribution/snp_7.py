dict1=dict()
dict2=dict()
inFile=open('sum_snp.genome_combined.sorted.pass012.known.atcg.coding')
for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')
    dict1[fields[0]]=[int(i) for i in fields[1:11]]
    dict2[fields[0]]=[int(i) for i in fields[11:21]]

inFile.close()



type=['AT','AC','AG','TA','TC','TG','CA','CT','CG','GA','GT','GC']
type2=['T>G/A>C','T>C/A>G','T>A/A>T','C>A/G>T','C>G/G>C','C>T/G>A']
dict3=dict()
dict4=dict()
dict5=dict()
dict6=dict()


for item in type2 :
    dict5.setdefault(item,[0]*10)
    dict6.setdefault(item,[0]*10)
for i in range(10) :
    dict5[type2[0]][i]=dict1['TG'][i]+dict1['AC'][i]
    dict5[type2[1]][i]=dict1['TC'][i]+dict1['AG'][i]
    dict5[type2[2]][i]=dict1['TA'][i]+dict1['AT'][i]
    dict5[type2[3]][i]=dict1['CA'][i]+dict1['GT'][i]
    dict5[type2[4]][i]=dict1['CG'][i]+dict1['GC'][i]
    dict5[type2[5]][i]=dict1['CT'][i]+dict1['GA'][i]
    dict6[type2[0]][i]=dict2['TG'][i]+dict2['AC'][i]
    dict6[type2[1]][i]=dict2['TC'][i]+dict2['AG'][i]
    dict6[type2[2]][i]=dict2['TA'][i]+dict2['AT'][i]
    dict6[type2[3]][i]=dict2['CA'][i]+dict2['GT'][i]
    dict6[type2[4]][i]=dict2['CG'][i]+dict2['GC'][i]
    dict6[type2[5]][i]=dict2['CT'][i]+dict2['GA'][i]



import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
for item in type2 :
    dict3.setdefault(item,[])
    dict4.setdefault(item,[])

    dict3[item].append(np.array(dict5[item]).mean())
    dict3[item].append(np.array(dict5[item]).std())
    dict3[item].append(np.array(dict5[item]))

    dict4[item].append(np.array(dict6[item]).mean())
    dict4[item].append(np.array(dict6[item]).std())
    dict4[item].append(np.array(dict6[item]))
    
#    dict3[item].append(np.array([i/300 for i in dict1[item]]).mean())
#    dict3[item].append(np.array([i/300 for i in dict1[item]]).std())
#    dict3[item].append(np.array([i/300 for i in dict1[item]]))

#    dict4[item].append(np.array([i/300 for i in dict2[item]]).mean())
#    dict4[item].append(np.array([i/300 for i in dict2[item]]).std())
#    dict4[item].append(np.array([i/300 for i in dict2[item]]))
 

#N = len(type)
#danMean   = [dict3[item][0] for item in type]
#hunMean   = [dict4[item][0] for item in type]
#danStd   = [dict3[item][1] for item in type]
#hunStd  = [dict4[item][1] for item in type]
N = len(type2)
danMean   = [dict3[item][0] for item in type2]
hunMean   = [dict4[item][0] for item in type2]
danStd   = [dict3[item][1] for item in type2]
hunStd  = [dict4[item][1] for item in type2]



fig = plt.figure()
ax = fig.add_subplot(111)

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = ax.bar(ind, danMean,   width, color='r', yerr=danStd)
p2 = ax.bar(ind+width, hunMean, width, color='y', yerr=hunStd)

#plt.title('Scores by group and gender')

ax.set_xlim(-0.3,6)
ax.set_ylabel('Number of substitutions')
#plt.yticks(np.arange(0,81,10))

ax.set_xticks(ind+width)
ax.set_xticklabels(type2) 
#ax.legend( (p1[0], p2[0]), ('CC', 'MCC') )
ax.legend( (p1[0], p2[0]), ('CC', 'MCC'),loc = 'upper right',bbox_to_anchor=(0.85,0.95))

plt.savefig('sum_snp.genome_combined.sorted.pass012.known.atcg.coding.pdf')


'''



N = 5
menMeans   = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd     = (2, 3, 4, 1, 2)
womenStd   = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans,   width, color='r', yerr=womenStd)
p2 = plt.bar(ind, womenMeans, width, color='y',
                     bottom=menMeans, yerr=menStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind+width/2., ('G1', 'G2', 'G3', 'G4', 'G5') )
plt.yticks(np.arange(0,81,10))
plt.legend( (p1[0], p2[0]), ('Men', 'Women') )

plt.show()

'''
