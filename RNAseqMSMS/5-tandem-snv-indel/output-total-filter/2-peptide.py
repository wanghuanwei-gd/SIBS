inFile = open('HeLa-SNV-INDEL-ALT')

D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    start = int(fields[4].split(':')[0])
    pre = fields[4].split(':')[5]
    post = fields[4].split(':')[6]
    s = int(fields[1].split(':')[-3])
    e = int(fields[1].split(':')[-2])
    D.setdefault(fields[3], [])
    D[fields[3]].append(fields[1]+':'+str(s-start+1)+':'+str(e-start+1)+':'+pre+':'+post)

inFile.close()

ouFile = open('HeLa-SNV-INDEL-ALT-pep','w')
for k in D:
    v = '\t'.join(D[k])
    if v.find('SNV')!=-1:
        ouFile.write(k+'\t'+v+'\n')
for k in D:
    v = '\t'.join(D[k])
    if v.find('INDEL')!=-1:
        ouFile.write(k+'\t'+v+'\n')

ouFile.close()
