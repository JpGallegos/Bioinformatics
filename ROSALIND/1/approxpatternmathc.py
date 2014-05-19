#! /usr/bin/env python
# coding: utf-8

def hamming_distance(s1, s2):
    '''Return the Hamming distance between equal-length sequences.'''
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def approximate_pattern_match(pattern, genome, d):
    '''Find all approximate occurrences of a pattern in a string.
    We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ≠ qi. For example, CGAAT and CGGAC have two mismatches.
    
    Pattern => '''
    pattern_len = len(pattern)
    matches = []

    for i in range(0, len(Genome) - pattern_len + 1):
        distance = hamming_distance(pattern, genome[i:i+pattern_len])
        if distance <= d:
            matches.append(i)
    return matches

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as f:
            Pattern = f.readline().strip('\n')
            Genome = f.readline().strip('\n')
            d = int(f.readline().strip('\n'))
            for match in approximate_pattern_match(Pattern, Genome, d):
                print match,
            print "" 
    else:
        print "USAGE: approxpatternmatch.py [FILE]"