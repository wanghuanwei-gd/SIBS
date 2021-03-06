import os
DIR = 'output-First'
ouFile = open('Peptides-Identified-First', 'w')
ouFile2 = open('Peptides-Identified-First-Spec', 'w')
D = {}
Fs = os.listdir(DIR)
for F in Fs:
    if F[-4:] == '.fdr':
        inFile = open(DIR + os.sep + F)
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            protein = fields[1]
            peptide = fields[3]
            if protein.find('REVERSE') == -1:
                D.setdefault(peptide, [])
                D[peptide].append(protein)
                ouFile2.write(fields[0] + '\n')
        inFile.close()

for k in D:
    ouFile.write('>' + '+++'.join(set(D[k])) + '\n')
    ouFile.write(k + '\n')

ouFile.close()
ouFile2.close()
