#! /usr/bin/env python

def clump_finding(sequence, k, L, t):
    """Given integers L and t, a string Pattern forms an (L, t)-clump
    inside a (larger) string Genome if there is an interval of Genome 
    of length L in which Pattern appears at least t times.

    k => size of the k-mer
    L => length of the sequence
    t => times the k-mer must appear, at least, in the sequence

    This version is expensive computational-wise, but it has potential 
    for distributed environment, and/or parallelism (with a little fix)."""
    clumps = []
    for i in range(0, len(sequence) - L + 1):
        distinct_k_mers = {}
        for j in range(i, (i + L) - k + 1):
            k_mer = sequence[j:j+k]    
            if not k_mer in distinct_k_mers:
                distinct_k_mers[k_mer] = 1
            else:
                distinct_k_mers[k_mer] += 1
        [clumps.append(c) for c, v in distinct_k_mers.items() if v >= t and c not in clumps]
        del distinct_k_mers
    return clumps

def clump_finding1(sequence, k, L, t):
    """Same as clump_finding, but with a different approach.
    Tries to find all k-mers in sequence first, and then filter
    them by the positions where they occur."""
    distinct_k_mers = {}

    # Find all distinct k-mers in sequence and their locations
    for i in range(0, len(sequence) - k + 1):
        k_mer = sequence[i:i+k]
        if not k_mer in distinct_k_mers:
            distinct_k_mers[k_mer] = [i]
        else:
            distinct_k_mers[k_mer].append(i)
    
    # Filter out all those with occurrence less than t. They can't possibly 
    # form (L, t)-clumps is they appear less than t times in the WHOLE sequence.
    k_mers_with_t_occurrences = dict((k_mer, locations) for k_mer, locations in distinct_k_mers.items() if len(locations) >= t)

    # Now filter further by checking that t of those occurrences are within L of each other.
    return [k_mer for k_mer, location in k_mers_with_t_occurrences.items() if within_interval(location, L, t, k)]

def within_interval(p, L, t, s):
    """Given a set p of numbers, check if at least t of them are in the same interval L.
    Return True if there are t numbers within a distance L of each other, False otherwise.

    p => A list of numbers
    L => Length of the interval
    t => Amount of point that have to be within L"""

    for base_location in range(0, len(p) - t + 1):
        if p[base_location + t - 1] - p[base_location] < L - s:
            return True
    return False


def time_test(sequence, k, L, t, n=1000):
    """Run the both clump finding functions n times and clock the wall time of each
    execution. Average the wall times, and determine the performance increase, if any.

    n => the number of times each function is going to be measured
    Other arguments => same as for the clump finding fucntions"""
    cf_timings = []
    cf1_timings = []

    for i in range(0, n):
        print "CF time", i
        t0 = time.time()
        clump_finding(genome, k, L, t)
        cf_timings.append(time.time() - t0)
        print "CF1 time", i

    for i in range(0, n):
        t0 = time.time()
        clump_finding1(genome, k, L, t)
        cf1_timings.append(time.time() - t0)

    sum_cf_timings = sum(cf_timings)
    sum_cf1_timings = sum(cf1_timings)

    print sum_cf_timings, cf_timings


if __name__ == "__main__":
    import sys
    import time

    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as fp:
            # Get the genome from the file
            genome = fp.readline().upper().strip('\n')
            # Get the k, L, t values from file as a tuple of strings and convert each to an 
            # int.
            k, L, t =  map(int, fp.readline().strip('\n').split(" "))

            # print k, L, t

            result = clump_finding(genome, k, L, t)
            for clump in result:
                print clump,
            print ""
    else:
        print "Usage: clumpfinding.py [FILE]"
