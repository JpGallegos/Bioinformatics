#! /usr/bin/env python
# coding: utf-8

def Skew(Genome):
    """Define Skew of Genome as the difference between the total number of 
    occurrences of G and C in the first i nucleotides of Genome, where i 
    ranges from 0 to |Genome|. Let prefix_i of Genome denote a prefix 
    (i.e, an initial substring) of Genome with length i.

    Genome => A DNA string

    Return: The list of the skews of Genome at prefix_i, i = 0,...,|Genome|"""

    # For prefix_i = 0, the skew of Genome is 0
    skew = [0]

    for i in range(0, len(Genome)):
        # i changes meaning depending on the context:
        #   - When applied to Genome it means the ith nucleotide.
        #   - When applied to skew, i means the skew of Genome
        #     at prefix_i.
        if Genome[i] == 'C':
            skew.append(skew[i] - 1)
        elif Genome[i] == 'G':
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
    return skew

def minimum_skew(Genome):
    """Find the position(s) in a genome minimizing the skew.

    Genome => A DNA string
    Returns: All integer(s) i minimizing Skew(Genome) over all values of i (from 0 to |Genome|)."""

    skew = Skew(Genome)
    minimal_skew = 0
    minimal_skew_ints = []

    for i in range(0, len(Genome)):
        current_skew = skew[i]
        if current_skew == minimal_skew:
            minimal_skew_ints.append(i)
        elif current_skew < minimal_skew:
            minimal_skew = current_skew
            minimal_skew_ints = []
            minimal_skew_ints.append(i)
    return minimal_skew_ints
        

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as fp:
            Genome = fp.readline().strip('\n')
            for skew in minimum_skew(Genome):
                print skew,
            print

    else:
        print "Usage: skew.py [FILE]"