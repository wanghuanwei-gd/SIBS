inFile=open('SNV.genome.somatic.exome.UTR.nondbsnp.geneLevel')
dict1=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1[fields[0]]=line

inFile.close()

inFile=open('PPI_somatic.pageranked')
ouFile=open('SNV.genome.somatic.exome.UTR.nondbsnp.geneLevel_pageranked','w')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if fields[0] in dict1 :
        ouFile.write(dict1[fields[0]]+'\n')
inFile.close()
ouFile.close()
