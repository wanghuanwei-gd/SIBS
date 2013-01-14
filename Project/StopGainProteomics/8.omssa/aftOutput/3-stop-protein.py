import os 


def uniprot():
    inFile = open('/netshare1/home1/people/hansun/StopGainProteomics/2.uniprot/human_uniprot_sprot.fa')
    D = {}
    while True:
        head = inFile.readline().strip()
        seq = inFile.readline().strip()
        if head:
            name = head.split('|')[1]
            D[name]=seq
        else:
            break
    inFile.close()
    return D


D = uniprot()
D2 = {}
 
def  pep2protein():
    files = os.listdir('.')
    for inF in files:
        if inF[-6:]=='stop-2':
            inFile = open(inF)
            for line in inFile:
                line = line.strip()
                fields = line.split('\t')
                for x in fields[2:]:
                    D2.setdefault(x, [])
                    D2[x].append(inF.split('.')[0].split('-')[0]+':'+fields[0]+':'+str(D[x].index(fields[0])))
            inFile.close()
pep2protein()

ouFile = open('3-stopgain-protein', 'w')
for k in D2:
    ouFile.write(k+'\t'+'\t'.join(D2[k])+'\n')
ouFile.close()


