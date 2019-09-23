import numpy as np
import pandas as pd
import argparse, math, sys

# main function
def main():
    
    args = get_command_line()

    autosome = []
    for i in range(1, 23):
        autosome.append('chr{}'.format(i))
    autosome = set(autosome)

    # load mouse data
    genes = pd.read_table(args.genes, sep='\t')
   
    # parse data
    chrom_col = genes['chrom'].values
    start_col = genes['exonStarts'].values
    end_col = genes['exonEnds'].values
    exons = []
    for i in xrange(genes.shape[0]):
        chrom = chrom_col[i].strip()
        
        if chrom not in autosome:
            continue

        start = start_col[i].strip().split(',')
        end = end_col[i].strip().split(',')

        for j in xrange(len(start)-1):
            exons.append((chrom, int(start[j]), int(end[j]), int(chrom[3:])))

    # save data
    exons = pd.DataFrame(exons)
    exons = exons.sort_values(by=[3, 1, 2])
    exons = exons.reset_index(drop=True)
    exons = exons.drop_duplicates()
    exons = exons.reset_index(drop=True)
    exons = exons[[0,1,2]]
    exons.to_csv(args.out, sep='\t', header=None, index=False)

# get command line
def get_command_line():
    
    parser = argparse.ArgumentParser(description='Plot sim results')

    parser.add_argument('--genes', dest='genes', type=str,
        help='', required=True)

    parser.add_argument('--out', dest='out', type=str,
        help='', required=True)

    args = parser.parse_args()
    
    return args

if(__name__ == '__main__'):
    main()
