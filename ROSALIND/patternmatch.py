#! /usr/bin/env python

def pattern_match(sequence, pattern):
	pattern_len = len(pattern)
	pattern_pos = []
	for i in range(0, (len(sequence) - pattern_len + 1)):
		if sequence[i:i + pattern_len] == pattern:
			pattern_pos.append(i)
	return pattern_pos

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 2:
		with open(sys.argv[1], 'r') as fp:
			pattern = fp.readline().upper().strip('\n')
			text = fp.readline().upper().strip('\n')
			positions = pattern_match(text, pattern)
			for pos in positions:
				print pos,
			print ""
	else:
		print "Usage: clumpfinding.py [FILE]"