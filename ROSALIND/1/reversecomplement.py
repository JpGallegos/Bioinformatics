#! /usr/bin/env python
# coding: utf-8

"""In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. Given a nucleotide p, 
we denote its complementary nucleotide as p. The reverse complement of a string Pattern = p1…pn is the string 
Pattern = ~pn … ~p1 formed by taking the complement of each nucleotide in Pattern, then reversing the resulting 
string.

For example, the reverse complement of Pattern = "GTCA" is Pattern = "TGAC"."""

nucleotide_complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def reverse_complement(sequence):
    """Reverse Complement Problem
    Find the reverse complement of a DNA string.

    Given: A DNA string Pattern.

    Return: Pattern, the reverse complement of Pattern."""
    complement = ''

    for i in range(len(sequence)-1, -1, -1):
        complement += nucleotide_complements[sequence[i]]
    return complement


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as fp:
            sequence = fp.readline().strip('\n')
            print reverse_complement(sequence)
    else:
        print "Usage: reversecomplement.py [FILE]"
