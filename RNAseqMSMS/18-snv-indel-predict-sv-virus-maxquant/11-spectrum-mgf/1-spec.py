def spec(inF):
    inFile = open(inF)
    ouFile = open(inF+'-spec','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        pep = fields[6]
        sc = fields[8].split(';')
        '''
        for item in sc:
            ouFile.write(pep+'\t'+item+'\n')
        '''
        ouFile.write(pep+'\t'+sc[0]+'\n')
    inFile.close()
    ouFile.close()

spec('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict')

