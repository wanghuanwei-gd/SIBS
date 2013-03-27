from xml.etree.ElementTree import *
import os

class Spectrum:
    spec_name = ''
    protein = []
class Protein:
    protein_name = ''
    protein_attr = ''
    peptide = []
class Peptide:
    peptide_seq = ''
    peptide_attr = ''


ouFile=open('tandem.peptides3','w')
dir='.'
for f in os.listdir(dir) :
    fe=dir+os.sep+f
    #if fi[-6:]=='.t.xml' :
    if f == '20090815_Velos1_NaNa_SA_10k_Hela_Trypsin_SECC_SAXpH_11.2013_03_27_17_35_24.t.xml':
        tree = ElementTree()
        tree.parse(fe)
        group=tree.findall('group')
        for item in group :
            Tandem = {}
            if item.get('id') :
                #seq=[]
                #mgf=[]
                #label=[]
                #info=[]
                #pep = []
                #pro = []
                Spec = Spectrum()
                s = item.findall('group/note')
                if len(s) == 1:
                    Spec.spec_name = s[0]
                else:
                    print('spec error')
                    return

                p=item.findall('protein')
                for x in p :
                    Spec.protein.append(Protein())
                    label.append(it.get('label'))
                b = item .findall('protein/note')
                for it in b :
                    pro.append(it.text)

                p=item.findall('protein/peptide')
                for it in p :
                    pep.append(''.join(it.text.strip().split()))

                s=item.findall('protein/peptide/domain')
                for it in s :
                    seq.append(it.get('seq'))
                    info.append(it.get('start')+':'+it.get('end')+':'+it.get('expect')+':'
                            +it.get('hyperscore')+':'+it.get('pre')+':'+it.get('post'))

        
                #ouFile.write(f+'\t'+'\t'.join(mgf)+'\t'+'\t'.join(seq)+'\n')
                #ouFile.write(f+'\t'+'\t'.join(label)+'\t'+'\t'.join(info)+'\t'+'\t'.join(seq)+'\n')

                if len(mgf)==1 and len(seq)==len(pep)==len(pro)==len(info):
                    ouFile.write(f+'\t'+'\t'.join(mgf)+'\t')
                    for i in range(len(seq)):
                        ouFile.write(seq[i]+'\t')
                        ouFile.write(pep[i]+'\t')
                        #ouFile.write(label[i]+'\t')
                        ouFile.write(pro[i]+'\t')
                        ouFile.write(info[i]+'\t')
                    ouFile.write('\n')
                else:
                    print('>'+ f )
                    print(mgf)
                    print(seq)
                    print(pep)
                    print(label)
                    print(info)
ouFile.close()
