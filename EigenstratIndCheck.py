#!/usr/bin/env python3

import sys, argparse

parser = argparse.ArgumentParser(usage="%(prog)s <functional argument> <ouput target argument>" , description="Extract the frequency of shared rare variants between each test sample/group and all reference samples/groups from a freqsum file.")
parser.add_argument("-i", "--Input", type=argparse.FileType('r'), metavar="<INPUT FILES PREFIX>", required=True)
parser.add_argument("-c", "--Check", type=argparse.FileType('r'), metavar="<INPUT FILE>", required=False)

args = parser.parse_args()

if args.Check != None:
	Inds1 = []
	Inds2 = []
	c = 0
	for line in args.Input:
		fields = line.strip().split()
		Inds1.append(fields[0])
	
	for line in args.Check:
		fields = line.strip().split()
		Inds2.append(fields[0])
	
	for ind in Inds1:
		if ind in Inds2:
			print (ind, "<---", "Duplicate individual", sep="\t")#, file=o)
			c+=1
	print ("#Duplicate individual check finished. ", c, " duplicate individuals found.", sep="")#, file =o)
	sys.exit(0)

