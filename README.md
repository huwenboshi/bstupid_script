# bstupid script

## Files:

1. UCSC_genes.gz: UCSC gene
2. chrom_length.txt: length of each chromosome in number of base pairs
3. exons_by_chr/: bed files containing exon boundaries

## Pipeline:

1. Run step1_make_bed.sh: This will parse UCSC_genes.gz to extract the exons,
and create a bed file containing all exons.
2. Run step2_merge.sh: This will call bedtools to merge any overlapping exons.
The output will be a bed file containing all exons. I separated them by
chromosome to speed up computation.
3. Run step3_calc_bstupid.sh: This takes as input the exon bed file for each
chromosome, and the length of the chromosome. The output will be a gzipped
text file with 2 columns. The 1st column is the 0-based base pair position.
And the 2nd column is the distance to the nearest exon.
