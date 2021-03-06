library("biomaRt")
mart=useMart("ensembl")
ensembl=useDataset("hsapiens_gene_ensembl",mart=mart)
data=getBM(attributes=c("ensembl_gene_id","chromosome_name","start_position","end_position","strand","band","go_id","embl","external_gene_id"),mart=ensembl)
write.table(data,"gene.symbol.postion",quote=F)
