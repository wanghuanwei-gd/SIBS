#!/bin/bash
### Job name
#LJRS -N tandem
### Queue name
#LJRS -q dpool
### Number of nodes
#LJRS -l nodes=2:ppn=4

cd /netshare1/home1/people/hansun/GeneFusions/Tandem3

tandem.exe inputxml/input_Adeno_11_343_rep2_step01.xml
