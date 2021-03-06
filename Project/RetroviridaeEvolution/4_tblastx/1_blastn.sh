#cd /netshare1/home1/people/hansun/Data/S3/blast

#db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta
#query=ucsc.mouse.fa
#out=ucsc.mouse.out1
#tblastx  -db $db  -query $query -out $out -outfmt 6  -num_threads 8  -num_threads 6
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



cd /netshare1/home1/people/hansun/Project/RetroviridaeEvolution/4_tblastx
query=RetroviridaeGenome.fasta.fa



out=Retroviridae.human.out
tblastx  -db $humandb  -query $query -out $out -outfmt 6  -num_threads 8 

out=Retroviridae.mouse.out
tblastx  -db $mousedb  -query $query -out $out -outfmt 6  -num_threads 8  

out=Retroviridae.rat.out
tblastx  -db $ratdb  -query $query -out $out -outfmt 6  -num_threads 8  

out=Retroviridae.chicken.out
tblastx  -db $chickendb  -query $query -out $out -outfmt 6  -num_threads 8  

out=Retroviridae.chimpanzee.out
tblastx  -db $chimpanzeedb  -query $query -out $out -outfmt 6  -num_threads 8  

out=Retroviridae.cow.out
tblastx  -db $cowdb  -query $query -out $out -outfmt 6  -num_threads 8  

out=Retroviridae.dog.out
tblastx  -db $dogdb  -query $query -out $out -outfmt 6  -num_threads 8  

out=Retroviridae.elephant.out
tblastx  -db $elephantdb  -query $query -out $out -outfmt 6  -num_threads 8  

out=Retroviridae.fugu.out
tblastx  -db $fugudb  -query $query -out $out -outfmt 6  -num_threads 8  

out=Retroviridae.opossum.out
tblastx  -db $opossumdb  -query $query -out $out -outfmt 6  -num_threads 8  

out=Retroviridae.platypus.out
tblastx  -db $platypusdb  -query $query -out $out -outfmt 6  -num_threads 8  


out=Retroviridae.tetraodon.out
tblastx  -db $tetraodondb  -query $query -out $out -outfmt 6  -num_threads 8  


out=Retroviridae.xenopus.out
tblastx  -db $xenopusdb  -query $query -out $out -outfmt 6  -num_threads 8  

out=Retroviridae.zebrafish.out
tblastx  -db $zebrafishdb  -query $query -out $out -outfmt 6  -num_threads 8  
