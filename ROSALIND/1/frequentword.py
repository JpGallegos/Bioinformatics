#! /usr/bin/env python
# coding: utf-8

"""A k-mer is defined as a string of length k. We define Count(Text, Pattern) as the number of times that 
a k-mer Pattern appears as a substring of Text. For example,

Count(ACAACTATGCATACTATCGGGAACTATCCT,ACTAT)=3

We note that Count(CGATATATCCATAG, ATA) is equal to 3 (not 2) since we should account for overlapping occurrences of Pattern in Text.

We say that Pattern is a most frequent k-mer in Text if it maximizes Count(Text, Pattern) among all k-mers. For example, "ACTAT" is 
a most frequent 5-mer in "ACAACTATGCATCACTATCGGGAACTATCCT", and "ATA" is a most frequent 3-mer of "CGATATATCCATAG"."""

from operator import itemgetter
 
string = "ACAACTATGCATACTATCGGGAACTATCCTA"
 
def count(text, pattern):
    pattern_length = len(pattern)
    matches = 0
    for i in range(0, (len(text) - pattern_length + 1)):
        sub_string = text[i:i+pattern_length]
        # print sub_string
        if sub_string == pattern:
            matches += 1
    return matches
 
def frequent_k_mers(text, k):
    k_mer_freq = {}
    for i in range(0, len(text) - k + 1):
        k_mer = text[i:i+k]
        if k_mer not in k_mer_freq:
            k_mer_freq[k_mer] = 1
        else:
            k_mer_freq[k_mer] += 1
    k_mer_freq = sorted(k_mer_freq.iteritems(), key=itemgetter(1), reverse=True)
    highest_k_mer_freq = k_mer_freq[0][1]
    most_freq_k_mers = []
    for i in range(0, len(k_mer_freq)):
        if k_mer_freq[i][1] == highest_k_mer_freq:
            most_freq_k_mers.append(k_mer_freq[i][0])
    return most_freq_k_mers
 
 
 
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as f:
            text = f.readline().strip('\n')
            k = int(f.readline().strip('\n'))
            for k_mer in frequent_k_mers(text, k):
                print k_mer,
            print "\n"
    else:
        print "Usage: frequentword.py [FILE]"
    