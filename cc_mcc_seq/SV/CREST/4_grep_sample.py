import os

files=''' /netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/10A/10A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/1A/1A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/2A/2A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/3A/3A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/4A/4A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/5A/5A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/6A/6A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/7A/7A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/8A/8A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/9A/9A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/10A/10A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/1A/1A.bam.predSV.txt.ctx.genelevel.tmp \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/2A/2A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/3A/3A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/4A/4A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/5A/5A.bam.predSV.txt.ctx.genelevel.tmp \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/6A/6A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/7A/7A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/8A/8A.bam.predSV.txt.ctx.genelevel \
/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/9A/9A.bam.predSV.txt.ctx.genelevel.tmp '''



inFile1=open('ctx_gene_sample','r')
for line in inFile1 :
    gene=line.split('\t')[0]
    os.system('echo '+gene)
    cmd='grep '+gene+files
    os.system(cmd)
    os.system('echo')
    os.system('echo')
inFile1.close()
