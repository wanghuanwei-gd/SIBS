GENE = {}
def alias(inF):
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split()
        if line.find('Ensembl_EntrezGene')!=-1:
            GENE[fields[1]] = fields[2]
    inFile.close()
alias('protein.aliases.v9.05.human')

def gene(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF+'.gene','w')
    for line in inFile:
        line = line.strip()
        fields = line.split()
        if int(fields[2]) >= 700:
            gene1 = fields[0].split('.')[1]
            gene2 = fields[1].split('.')[1]
            if gene1 in GENE:
                gene1 = GENE[gene1]
            if gene2 in GENE:
                gene2 = GENE[gene2]

            D.setdefault(gene1,[])
            D.setdefault(gene2,[])
            D[gene1].append(gene2)
            D[gene2].append(gene1)
    inFile.close()
    for k in D:
        ouFile.write(k+'\t'+'\t'.join(set(D[k]))+'\n')

gene('protein.links.v9.0.human')
