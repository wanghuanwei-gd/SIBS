cd /netshare1/home1/szzhongxin/proj1/hansun/16sTranslocation/4.blat
db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta

query=ICC5A.unmapped.filtered.trans.fa
out=${query}.blated

blat $db $query  -out=blast8 $out    
