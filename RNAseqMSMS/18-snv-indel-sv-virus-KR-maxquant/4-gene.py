SNVINDEL = []
inFile  = open('/netshare1/home1/people/hansun/RNAseqMSMS/1-snv/A1_csv2tsv/sum_snv.exome_summary')
for line in inFile:
    line = line.strip()
    SNVINDEL.append(line)
inFile.close()

inFile  = open('/netshare1/home1/people/hansun/RNAseqMSMS/1-snv/A1_csv2tsv/sum_snv.exome_summary.indel')
for line in inFile:
    line = line.strip()
    SNVINDEL.append(line)
inFile.close()

L = []
inFile = open('/netshare1/home1/people/hansun/Data/hg19_refGene/refGene-2013-04-22.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L.append(fields)
inFile.close()

VIRUS_GENE={}
VIRUS_GENE['E1']=[914,2887]
VIRUS_GENE['E2']=[2817,3914]
VIRUS_GENE['E4']=[3418,3684]
VIRUS_GENE['E5']=[3936,4157]
VIRUS_GENE['E6']=[105,581]
VIRUS_GENE['E7']=[590,907]
VIRUS_GENE['L1']=[5430,7136]
VIRUS_GENE['L2']=[4244,5632]
VIRUS_GENE['LCR']=[0,104]



def snv_indel(line):
    fields = line.split('\t')
    fds = fields[10].split(':')
    for i in range(len(fds)):
        if fds[i].find('SNV')!=-1 or fds[i].find('INDEL')!=-1:
            ch = fields[10].split(':')[i+1]
            pos = fields[10].split(':')[i+2]
            genes = []
            dbsnps = []
            for item in SNVINDEL:
                if item.find(ch) != -1 and item.find(pos) != -1: 
                    gene = item.split('\t')[1].split('(')[0]
                    dbsnp = item.split('\t')[8]
                    genes.append(gene)
                    dbsnps.append(dbsnp)
            if dbsnps:        
                ouFile.write('|'.join(genes)+'\t'+'|'.join(dbsnps)+'\t'+line+'\n')
            else:
                ouFile.write('|'.join(genes)+'\t'+'new'+'\t'+line+'\n')
            break

def predict(line): 
    fields = line.split('\t')
    for item in fields:
        if item.find('genscan')!=-1:
            ch ='chr'+item.split(':')[3]
            pos1 =item.split(':')[4]
            pos2 =item.split(':')[5]
            genes = []
            for item in L:
                if (item[2]==ch and (int(item[4])<=int(pos1)<=int(item[5]) or int(item[4])<=int(pos2)<=int(item[5]))) :
                    gene = item[12]
                    genes.append(gene)
            ouFile.write('|'.join(set(genes))+'\t'+''+'\t'+line+'\n')
            break

def virus(line):
    fields = line.split('\t')
    for item in fields:
        if item.find('VIRUS:')!=-1:
            nc= item.split(':')[2]
            pos1_nc = item.split(':')[9]
            pos2_nc = item.split(':')[10]
            pos5_nc_query = item.split(':')[7]
            pos6_nc_query = item.split(':')[8]
            genes = []
            for k in VIRUS_GENE:
                if VIRUS_GENE[k][0]<=int(pos1_nc)<=VIRUS_GENE[k][1] or VIRUS_GENE[k][0]<=int(pos2_nc)<=VIRUS_GENE[k][1]:
                    genes.append(k)
            ouFile.write('|'.join(set(genes))+'\t'+''+'\t'+line+'\n')
            break

def human_virus(line):
    pass

def sv_not_translocation(line):
    fields = line.split('\t')
    for item in fields:
        if item.find('SV:')!=-1:
            nc= item.split(':')[4]
            ch = item.split(':')[16]
            pos1_nc = item.split(':')[11]
            pos2_nc = item.split(':')[12]
            pos3_ch = item.split(':')[23]
            pos4_ch = item.split(':')[24]
        
            pos5_nc_query = item.split(':')[9]
            pos6_nc_query = item.split(':')[10]
            pos7_ch_query = item.split(':')[21]
            pos8_ch_query = item.split(':')[22]
            genes = []
            for item in L:
                if (item[2]==ch and (int(item[4])<=int(pos3_ch)<=int(item[5]) or int(item[4])<=int(pos4_ch)<=int(item[5]))) or \
                        (item[2]==nc and (int(item[4])<=int(pos1_nc)<=int(item[5]) or int(item[4])<=int(pos2_nc)<=int(item[5]))):
                    gene = item[12]
                    genes.append(gene)
            ouFile.write('|'.join(set(genes))+'\t'+''+'\t'+line+'\n')
            break



def sv_translocation(line):
    fields = line.split('\t')
    for item in fields:
        if item.find('SV:')!=-1:
            nc= item.split(':')[4]
            ch = item.split(':')[16]
            pos1_nc = item.split(':')[11]
            pos2_nc = item.split(':')[12]
            pos3_ch = item.split(':')[23]
            pos4_ch = item.split(':')[24]
    
            pos5_nc_query = item.split(':')[9]
            pos6_nc_query = item.split(':')[10]
            pos7_ch_query = item.split(':')[21]
            pos8_ch_query = item.split(':')[22]
            genes1 = []
            genes2 = []
            for item in L:
                if (item[2]==nc and (int(item[4])<=int(pos1_nc)<=int(item[5]) or int(item[4])<=int(pos2_nc)<=int(item[5]))):
                    genes1.append(item[12])
                if (item[2]==ch and (int(item[4])<=int(pos3_ch)<=int(item[5]) or int(item[4])<=int(pos4_ch)<=int(item[5]))):
                    genes2.append(item[12])
            if genes1:
                genes1 = '|'.join(set(genes1))
            else:
                genes1 = '*' 
            if genes2:
                genes2 = '|'.join(set(genes2))
            else:
                genes2 = '*' 
            gene = genes1+':'+genes2
            ouFile.write(gene+'\t'+''+'\t'+line+'\n')
            break



inFile = open('HeLa-peptide-snv-indel-predict-virus-sv')
ouFile = open('HeLa-peptide-snv-indel-predict-virus-sv-gene','w')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    if fields[1]=='SNV' or fields[1]=='INDEL':
        snv_indel(line)
    elif fields[1].find('PREDICT')!=-1:
        predict(line)
    elif fields[1]=='VIRUS':
        virus(line)
    elif fields[1]=='HUMAN-VIRUS':
        pass
    elif fields[1]=='SV-DELETION' or fields[1]=='SV-DUPLICATION' or fields[1]=='SV-INVERSION':
        sv_not_translocation(line)
    elif fields[1]=='SV-TRANSLOCATION':
        sv_translocation(line)


inFile.close()
ouFile.close()
