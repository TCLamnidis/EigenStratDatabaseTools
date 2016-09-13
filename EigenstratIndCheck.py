#!/usr/bin/env python3

import sys, argparse

parser = argparse.ArgumentParser(usage="%(prog)s <functional argument> <ouput target argument>" , description="Check two EigenStrat databases for duplicate individuals. Extract or expunge individuals from an EigenStrat database.")
parser.add_argument("-i", "--Input", type=argparse.FileType('r'), metavar="<INPUT FILES PREFIX>", required=True)
parser.add_argument("-c", "--Check", type=argparse.FileType('r'), metavar="<INPUT FILE>", required=False)

args = parser.parse_args()

o = sys.stdout

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
			print ("{:25s}".format(ind), "<---", "Duplicate individual", sep="\t", file=o)
			c+=1
	print ("#Duplicate individual check finished. ", c, " duplicate individuals found.", sep="", file =o)
	sys.exit(0)

