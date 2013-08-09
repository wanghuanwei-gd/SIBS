def pep(inF):
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[1] and fields[2]=='':
            D.setdefault(fields[1],[])
            D[fields[1]].append(0)
        if fields[2]:
            D.setdefault(fields[2],[])
            D[fields[2]].append(2)
        if fields[3]:
            D.setdefault(fields[3],[])
            D[fields[3]].append(3)
        fds = fields[4].split(':')
        i = 4
        for item in fds:
            D.setdefault(item,[])
            D[item].append(i)
            i += 1
    inFile.close()
    ouFile = open(inF+'.pep2','w')
    for k in D:
        if 0 in D[k]:
            ouFile.write(k+'\n')
    ouFile.close()


pep('gluc-0.2013_08_09_11_29_02_qry.peptides-pep')
pep('lysc-0.2013_08_09_11_29_01_qry.peptides-pep')
pep('trypsin-0.2013_08_09_11_29_00_qry.peptides-pep')

