#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Command line utility that accepts a word file and prints a dictionary of anagrams for that file.

Module provides a function find_anagrams which can be used to do the same
for an arbitrary list of strings.
"""

import sys

# Your name here, and any other people/sources who helped.
# Give credit where credit is due.
__author__ = "Mauricio"


def alphabetize(string):
	return "".join(sorted(string.lower()))


def find_anagrams(words):
	"""
    Returns a dictionary with keys that are alphabetized words and values
    that are all words that, when alphabetized, match the key.
    Example:
    {'dgo': ['dog'], 'act': ['cat', 'act']}
    """
	anagrams = {}
	for word in words:
		alphabetized_word = alphabetize(word)
		if alphabetized_word not in anagrams:
			anagrams[alphabetized_word] = [word]
		else:
			anagrams[alphabetized_word].append(word)
	return anagrams


if __name__ == "__main__":
	# run find anagrams of first argument
	if len(sys.argv) < 2:
		print("Please specify a word file!")
		sys.exit(1)
	else:
		with open(sys.argv[1], 'r') as handle:
			words = handle.read().split()
			print(find_anagrams(words))