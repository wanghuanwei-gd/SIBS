#!/bin/bash
### Job name
#LJRS -N rna_seq 
### Queue name 
#LJRS -q dpool
### Number of nodes 
#LJRS -l nodes=2:ppn=4
 
# This job's working directory
cd 
perl code/flag.pl tte65.sam tte65flag 
