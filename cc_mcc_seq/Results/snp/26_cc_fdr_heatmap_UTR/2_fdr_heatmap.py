inFile=open('gene_fdr_0.05_c')

ouFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted_heat','w')

dict1=dict()
for line in inFile :
    line=line.strip()
    gene=line.split('\t')[0]
    fdr=line.split('\t')[1]

    inFile1=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted')

    for line in inFile1 :
        line=line.strip()
        fields=line.split('\t')
        if fields[1] == gene :
            ouFile.write(fdr+'\t'+line+'\n')


    inFile1.close()


inFile.close()
