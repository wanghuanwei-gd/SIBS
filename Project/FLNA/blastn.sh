#cd /netshare1/home1/people/hansun/Data/S3/blast

#db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta
#query=lncdb.human.fa
#out=lncdb.human.out1
#blastn  -db $db  -query $query -out $out -outfmt 6    -num_threads 6
#####################################################################

humandb=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta
mousedb=/netshare1/home1/people/hansun/Data/GenomeSeq/Mouse/ucsc.mouse.fasta
ratdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Rat/ucsc.rat.fasta
chickendb=/netshare1/home1/people/hansun/Data/GenomeSeq/Chicken/ucsc.chicken.fasta
chimpanzeedb=/netshare1/home1/people/hansun/Data/GenomeSeq/Chimpanzee/ucsc.chimpanzee.fasta
cowdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Cow/ucsc.cow.fasta
dogdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Dog/ucsc.dog.fasta
elephantdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Elephant/ucsc.elephant.fasta
fugudb=/netshare1/home1/people/hansun/Data/GenomeSeq/Fugu/ucsc.fugu.fasta
opossumdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Opossum/ucsc.opossum.fasta
platypusdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Platypus/ucsc.platypus.fasta
tetraodondb=/netshare1/home1/people/hansun/Data/GenomeSeq/Tetraodon/ucsc.tetraodon.fasta
xenopusdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Xenopus/ucsc.xenopus.fasta
zebrafishdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Zebrafish/ucsc.zebrafish.fasta



cd /netshare1/home1/people/hansun/Data/S3/blast10


for ((i=44;i<45;i++))
do 
	query=lncrna_lncdb_human_genomic.$i
	out=lncdb.human.human.out.$i
	#blastn  -db $chimpanzeedb  -query $query -out $out -outfmt 6    
	blastn  -db $humandb  -query $query -out $out -outfmt 6   
done





