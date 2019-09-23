#!/bin/bash
#SBATCH -c 1
#SBATCH -N 1
#SBATCH -t 0-12:00
#SBATCH -p short
#SBATCH --mem=4096
#SBATCH -o ./job_out/hostname_%j.out
#SBATCH --mail-type=NONE

exon_dir=/n/groups/price/huwenbo/PART_TE_GCOV/data/annotation/annot_bstupid/exon/exons_by_chr

src=/n/groups/price/huwenbo/PART_TE_GCOV/scripts/misc
chrom=$1
chrom=22
chromlen=$(head -n $chrom chrom_length.txt | tail -n 1)

python $src/calc_bstupid.py \
    --exons $exon_dir/exons_chr${chrom}.bed \
    --length $chromlen \
    --out ./out/bstupid_bp_chr"$chrom".gz
