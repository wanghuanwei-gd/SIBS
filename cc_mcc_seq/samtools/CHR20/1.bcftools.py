import os
import sys 
chrs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10',
        'chr11','chr12','chr13','chr14','chr15','chr16','chr17',
        'chr18','chr19','chr20','chr21','chr22','chrX','chrY']
 
for d in [5,10,20,30,50]:

    for D in [300,500,1000]:

        for ch in chrs:
            #cmd = 'bcftools view var.raw.%s.bcf | vcfutils.pl varFilter -d 20 -D 200 > var.flt.%s.vcf'%(ch,ch)
            cmd = 'bcftools view var.raw.%s.bcf | vcfutils.pl varFilter -d %s -D %s > var.flt.%s.vcf'%(ch,d,D,ch)
            os.system(cmd)
        
        head = 27
        num = [0] * 20
        num2 = [0] * 20
        somatic = [0] * 20 
        somatic2 = [0] * 20 
        for ch in chrs:
            f = 'var.flt.%s.vcf'%ch
            inFile=open(f)
            for n in range(head):
                line = inFile.readline()
            for line in inFile:
                line = line.strip()
                fields = line.split('\t')
                for i,item in enumerate(fields[-20:]):
                    if item.find('0/0') != 0:
                        if float(item.split(':')[-1])>20:
                            num[i]+=1
                        num2[i]+=1
            inFile.close()

        print(str(d)+'\t'+str(D))
        print(num)
        print(somatic)
        print(num2)
        print(somatic2)




