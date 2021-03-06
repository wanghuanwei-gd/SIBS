from PyPlot.PyPlotClass import *

def venn_diagram(iFile1,iFile2,iFile3=0,setname1='A',setname2='B',setname3='C',filename='test.pdf') :
    pp=PyPlot(filename)
    A=[]
    B=[]
    C=[]
    inFile1=open(iFile1)
    inFile2=open(iFile2)
    for line in inFile1 :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:-1])
        A.append(k)
    for line in inFile2 :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:-1])
        B.append(k)
    inFile1.close()
    inFile2.close()
    if iFile3==0 :
        pp.venn_diagram([set(A),set(B)],setname1,setname2)

    else :
        inFile3=open(iFile3)
        for line in inFile3 :
            line=line.strip()
            fields=line.split('\t')
            k='\t'.join(fields[1:-1])
            C.append(k)
        inFile3.close()
        pp.venn_diagram([set(A),set(B),set(C)],setname1,setname2,setname3)


venn_diagram('SNV.genome.CHC10A','SNV.genome.CHC10B',filename='SNV.genome.CHC10.pdf',setname1='CHC10A',setname2='CHC10B')
venn_diagram('SNV.genome.CHC5A','SNV.genome.CHC5B',filename='SNV.genome.CHC5.pdf',setname1='CHC5A',setname2='CHC5B')
venn_diagram('SNV.genome.CHC6A','SNV.genome.CHC6B',filename='SNV.genome.CHC6.pdf',setname1='CHC6A',setname2='CHC6B')
venn_diagram('SNV.genome.CHC7A','SNV.genome.CHC7B',filename='SNV.genome.CHC7.pdf',setname1='CHC7A',setname2='CHC7B')


venn_diagram('SNV.genome.ICC10A','SNV.genome.ICC10B',filename='SNV.genome.ICC10.pdf',setname1='ICC10A',setname2='ICC10B')
venn_diagram('SNV.genome.ICC4A','SNV.genome.ICC4B',filename='SNV.genome.ICC4.pdf',setname1='ICC4A',setname2='ICC4B')
venn_diagram('SNV.genome.ICC5A','SNV.genome.ICC5B',filename='SNV.genome.ICC5.pdf',setname1='ICC5A',setname2='ICC5B')
venn_diagram('SNV.genome.ICC9A','SNV.genome.ICC9B',filename='SNV.genome.ICC9.pdf',setname1='ICC9A',setname2='ICC9B')
