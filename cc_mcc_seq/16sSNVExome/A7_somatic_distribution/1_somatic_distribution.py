def snv_distribution(iFile1,iFile2) :
    inFile=open(iFile2)
    dict1=dict()
    dict2=dict()
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        key='\t'.join(fields[21:26])
        dict1[key]=fields[0]+'\t'+fields[2]
    inFile.close()

    inFile=open(iFile1)
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        key='\t'.join(fields[1:6])
        dict2.setdefault(dict1[key],0)
        dict2[dict1[key]]+=1
    ouFile=open(iFile1+'.dist','w')
    for key in dict2 :
        ouFile.write(key+'\t'+str(dict2[key])+'\n')
    ouFile.close()

snv_distribution('SNV.genome.somatic.ICC4.not.repeat','sum_snv16sExome.genome_summary.overall.filter')
snv_distribution('SNV.genome.somatic.ICC5.not.repeat','sum_snv16sExome.genome_summary.overall.filter')
snv_distribution('SNV.genome.somatic.ICC9.not.repeat','sum_snv16sExome.genome_summary.overall.filter')
snv_distribution('SNV.genome.somatic.ICC10.not.repeat','sum_snv16sExome.genome_summary.overall.filter')

snv_distribution('SNV.genome.somatic.CHC5.not.repeat','sum_snv16sExome.genome_summary.overall.filter')
snv_distribution('SNV.genome.somatic.CHC6.not.repeat','sum_snv16sExome.genome_summary.overall.filter')
snv_distribution('SNV.genome.somatic.CHC7.not.repeat','sum_snv16sExome.genome_summary.overall.filter')
snv_distribution('SNV.genome.somatic.CHC10.not.repeat','sum_snv16sExome.genome_summary.overall.filter')
