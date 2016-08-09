#Fetch normal human prostate tissue eQTL database

reference: [Identification of candidate genes for prostate cancer-risk SNPs utilizing a normal prostate tissue eQTL data set](http://www.nature.com/ncomms/2015/151127/ncomms9653/abs/ncomms9653.html)
*Nature Communication*

[Comprehensively Evaluating cis-Regulatory Variation in the Human Prostate Transcriptome by Using Gene-Level Allele-Specific Expression](http://www.sciencedirect.com/science/article/pii/S0002929715001524)
*AJHG*

##Save AJHG tables

Use this command to convert EXCEL ^M files into unix format.
```
for i in $(ls *.txt); do tr '\r' '\n' < $i > ${i}_2; done
```
## Fetch 20kbp region at each eQTL site

```
python convert_to_bed.py  AJHG_ASE.txt_2
python convert_to_bed.py AJHG_JOINT.txt_2
python convert_to_bed.py AJHG_TE.txt_2
```

