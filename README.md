# bstupid script

## Files:

1. **UCSC_genes.gz**: UCSC gene
2. **chrom_length.txt**: length of each chromosome in number of base pairs
3. **exons_by_chr/**: bed files containing exon boundaries

## Pipeline:

1. **Run step1_make_bed.sh**: This will parse UCSC_genes.gz to extract the exons,
and create a bed file containing all exons.
2. **Run step2_merge.sh**: This will call bedtools to merge any overlapping exons.
The output will be a bed file containing all exons. I separated them by
chromosome to speed up computation.
3. **Run step3_calc_bstupid.sh**: This takes as input the exon bed file for each
chromosome, and the length of the chromosome. The output will be a gzipped
text file with 2 columns. The 1st column is the 0-based base pair position.
And the 2nd column is the distance to the nearest exon.

## calc_bstupid.py

The basic idea of how this works is as follows:

1. Maintain 2 pointers pointing to 2 neighboring exons: exon A and exon B
2. Iterating from position 0 to the length of chromosome
3. If base pair position is within A, set distance to 0
4. If base pair is between A and B, take min distance to A end and B start
5. After processing (exon B start - 1), advance pointers to point exons B and C
