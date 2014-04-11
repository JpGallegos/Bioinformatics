#! /usr/bin/env python
# coding: utf-8

def Skew(Genome):
    """Define Skew(Genome) as the difference between the total number of 
    occurrences of G and C in the first i nucleotides of Genome, where i 
    ranges from 0 to |Genome|.

    Genome => A DNA string"""

    # For i = 0, the skew of Genome is 0
    skew = [0]

    # i changes meaning depending on the context.
    # When applied to Genome it means the ith nucleotide,
    # and when applied to skew i means the skew of Genome
    # at the substring of length i (prefix i).
    for i in range(0, len(Genome)):
        if Genome[i] == 'C':
            skew.append(skew[i] - 1)
        elif Genome[i] == 'G':
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
    return skew

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        for i in Skew("GAGCCACCGCGATA"):
            print i,
        print ""
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as fp:
            Genome = fp.readline().strip('\n')
            print Skew(Genome)[53]

    else:
        print "Usage: skew.py [FILE]"