'''
first try, not using Diagram_class
'''


from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Graphics import GenomeDiagram
from Bio.Graphics.GenomeDiagram import CrossLink
from reportlab.lib.units import cm
from reportlab.lib import colors

gdd = GenomeDiagram.Diagram('Diagram')
gdt1_features = gdd.new_track(1, greytrack=False)
gds1_features = gdt1_features.new_set()
gdt2_features = gdd.new_track(1, greytrack=False)
gds2_features = gdt2_features.new_set()


inFile=open('CHC10A.unmapped.sam.mapped.fa.fa.blasted')
NC_len=5894
num=0
startend=[]
for line in inFile :
    fields=line.split('\t')
    if fields[1]=='NC_003977.1':
        num+=1
        color = colors.linearlyInterpolatedColor(colors.white, colors.firebrick, 0, 200, num)
        line=line.strip()
        q_start=int(fields[6])
        q_end=int(fields[7])
        s_start=int(fields[9])
        s_end=int(fields[9])
    
        startend.append(q_start)
        startend.append(q_end)
        startend.append(s_start)
        startend.append(s_end)
    
        feature = SeqFeature(FeatureLocation(q_start,q_end),strand=+1)
        #gds1_features.add_feature(feature,name=str(num),label=True,color=color)
    
        feature = SeqFeature(FeatureLocation(s_start,s_end),strand=+1)
        gds2_features.add_feature(feature,name=str(num),label=True,color=color)

inFile.close()


'''
gdt_features = gdd.new_track(1, greytrack=True)
gds_features = gdt_features.new_set()

feature = SeqFeature(FeatureLocation(1125, 1125), strand=+1)
gds_features.add_feature(feature,name='4',label=True,sigil="ARROW")
feature = SeqFeature(FeatureLocation(1150, 1250), strand=None)
gds_features.add_feature(feature,name='5',label=True,sigil="ARROW")
feature = SeqFeature(FeatureLocation(1275, 1375), strand=-1)
gds_features.add_feature(feature,name='6',label=True,sigil="ARROW")

track_X=gdd.tracks[2]
track_Y=gdd.tracks[1]
link_xy =CrossLink((track_X,25,125),(track_Y,125,1125))
gdd.cross_track_links.append(link_xy)
'''

gdd.draw(format='linear', pagesize=(15*cm,4*cm), fragments=10,start=1, end=max(startend))
gdd.write("GD_labels_default.pdf", "pdf")
