D = {}

def unique(inF,flag=''):
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip('>\n')
        line2 = inFile.readline().strip()
        if line1:
            D.setdefault(line2,[])
            if flag:
                D[line2].append(flag+':'+line1)
            else:
                D[line2].append(line1)
        else:
            break
    inFile.close()

unique('Homo_sapiens.GRCh37.70.pep.all.fa.fa')
unique('sum_snv.exome_summary.nonsynonymous-splicing.pep.ref-alt.nonstop-KR','SNV')
unique('sum_snv.exome_summary.nonsynonymous-splicing.pep.not-ref-alt.nonstop-KR','SNV')
unique('sum_snv.exome_summary.indel.pep.ref-alt.nonstop-KR','INDEL')
unique('sum_snv.exome_summary.indel.pep.not-ref-alt.nonstop-KR','INDEL')

ouFile = open('Homo_known-protein_snv_indel-KR.fasta','w')
for k in D:
    ouFile.write('>'+'|'.join(D[k])+'\n')
    ouFile.write(k+'\n')
    #ouFile.write('>REVERSE:'+'|'.join(D[k])+'\n')
    #ouFile.write(k[::-1]+'\n')

ouFile.close()

