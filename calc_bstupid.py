import numpy as np
import pandas as pd
import argparse, math, sys
import gzip

# main function
def main():
    
    args = get_command_line()

    exons = pd.read_table(args.exons, delim_whitespace=True, header=None)
    nexon = exons.shape[0]
    all_start = exons[1].values
    all_end = exons[2].values

    ptra = 0
    ptrb = ptra + 1

    out_f = gzip.open(args.out, 'w')
    for i in xrange(args.length):
        
        # get exon boundaries
        starta, enda = all_start[ptra], all_end[ptra]
        startb = starta; endb = enda;
        if ptrb < nexon:
            startb, endb = all_start[ptrb], all_end[ptrb]

        # initialize distance
        dist = -1
        
        # first exon
        if ptra == 0 and i < starta:
            dist = starta - i

        # within exon a
        if i >= starta and i < enda:
            dist = 0

        # between exon a and exon b
        if (ptra != ptrb) and (i >= enda and i < startb):
            dist = min(i-enda, startb-i)

        # last exon
        if ptra == nexon - 1 and i >= enda:
            dist = i - enda

        # sanity check
        if dist == -1:
            print 'Something went wrong!'

        # write to file
        out_f.write('{}\t{}\n'.format(i, dist))

        # update pointers
        if i == startb - 1:
            ptra += 1
            ptrb = ptra + 1
       
    out_f.close()

# get command line
def get_command_line():
    
    parser = argparse.ArgumentParser(description='Plot sim results')

    parser.add_argument('--exons', dest='exons', type=str,
        help='', required=True)

    parser.add_argument('--length', dest='length', type=int,
        help='', required=True)

    parser.add_argument('--out', dest='out', type=str,
        help='', required=True)

    args = parser.parse_args()
    
    return args

if(__name__ == '__main__'):
    main()
