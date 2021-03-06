#!/usr/bin/env python

D = {}
def unique(inF,flag=''):
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip('>\n')
        line2 = inFile.readline().strip()
        if line1:
            D.setdefault(line2,[])
            if flag:
                D[line2].append(flag+':'+':'.join(line1.split('\t')))
            else:
                D[line2].append(':'.join(line1.split('\t')))
        else:
            break
    inFile.close()

unique('Peptides-Identified-First-Mutated.fa')

ouFile = open('Peptides-Identified-First-Mutated-reversed.fa','w')
for k in D:
    ouFile.write('>'+'|'.join(D[k])+'\n')
    ouFile.write(k+'\n')
    ouFile.write('>REVERSE:'+'|'.join(D[k])+'\n')
    ouFile.write(k[::-1]+'\n')

ouFile.close()

