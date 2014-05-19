#! /usr/bin/env python
# coding: utf-8
from operator import itemgetter

def frequent_k_mers_mismatch(Genome, k, d):
    k_mer_freq = {}
    for i in range(0, len(Genome) - k + 1):
        k_mer = Genome[i:i+k]
        if k_mer not in k_mer_freq:
            k_mer_freq[k_mer] = 1
        else:
            k_mer_freq[k_mer] += 1
    k_mer_freq = sorted(k_mer_freq.iteritems(), key=itemgetter(1), reverse=True)
    highest_k_mer_freq

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        pass
    else:
        print "USAGE: frequentwordmismatch.py [FILE]"