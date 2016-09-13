#!/usr/bin/env python3

import sys, argparse, sh

parser = argparse.ArgumentParser(usage="%(prog)s (-i <Input file prefix>) (-c <input ind file> | -R | -E) [-L <SAMPLE LIST> | -S Ind [-S Ind2]] <ouput target argument>" , description="Check two EigenStrat databases for duplicate individuals. Extract or remove individuals from an EigenStrat database.")
parser.add_argument("-i", "--Input", type=str, metavar="<INPUT FILES PREFIX>", required=True, help="The desired input file prefix. Input files are assumed to be <INPUT PREFIX>.geno, <INPUT PREFIX>.snp and <INPUT PREFIX>.ind .")
group = parser.add_mutually_exclusive_group(required=True)
group2 = parser.add_mutually_exclusive_group(required=False)
group.add_argument("-C", "--Check", type=argparse.FileType('r'), metavar="<INPUT FILE>", required=False, help="Check the -i .ind file and the second .ind file for duplicate individuals. Population assignment and/or individual sex are not checked, only individual names. Names are case sensitive.")
group.add_argument("-E", "--Extract", action="store_true", required=False,help="Extract the selected individuals from the EigenStrat database, creating a new set of EigenStrat files with the selected individuals only.")
group.add_argument("-R", "--Remove", action="store_true", required=False,help="Remove the selected individuals from the EigenStrat database, creating a new set of EigenStrat files without the selected individuals.")
group2.add_argument("-L", "--SampleList", type=argparse.FileType('r'), metavar="<INDIVIDUAL LIST FILE>", required=False, help="A list of samples to be Extracted (-E) or Removed (-R) from the database. Can be a list of individual names (1 per line), or the output of duplicate check (-C). Required with -E or -R. Mutually exclusive with -S.")
group2.add_argument("-S", "--Sample", action="append", metavar="<INDIVIDUAL>", required=False, help="A samples to be Extracted (-E) or Removed (-R) from the database. Can be called multiple times. Required with -E or -R. Mutually exclusive with -L.")
args = parser.parse_args()

if args.Extract is True or args.Remove is True:
	if args.SampleList is None and args.Sample is None:
		parser.error("Sample (-S) or SampleList (-L) required for -R/-E functions.")

IndFile = open(args.Input+".ind", "r")
GenoFile = open(args.Input+".geno", "r")
# SnpFile = open(args.Input+".snp", "r")
o = sys.stdout

#Check function
if args.Check != None:
	Inds1 = []
	Inds2 = []
	c = 0
	for line in IndFile:
		fields = line.strip().split()
		Inds1.append(fields[0])
	
	for line in args.Check:
		fields = line.strip().split()
		Inds2.append(fields[0])
	
	for ind in Inds1:
		if ind in Inds2:
			print ("{:25s}".format(ind), "<---", "Duplicate individual", sep="\t", file=o)
			c+=1
	print ("#Duplicate individual check finished.", c, "duplicate individuals found.", sep=" ", file =o)
	sys.exit(0)

#Read sample names into list of individuals of interest, from either input option
Samples = []
if args.SampleList != None:
	for line in args.SampleList:
		fields = line.strip().split()
		if fields[0][0]!="#":
			Samples.append(fields[0])

if args.Sample != None:
	for i in args.Sample:
		if i not in Samples:
			Samples.append(i)
print (Samples)

if args.Remove == True:
	print ("Detected", len(Samples), "individuals for REMOVAL.", sep=" ", file=sys.stderr)
elif args.Extract == True:
	print ("Detected", len(Samples), "individuals for EXTRACTION.", sep=" ", file=sys.stderr)
#Get sample index in geno and ind files.
Index = {}
for i in Samples:
	for line in sh.grep(sh.cat("-n",args.Input+".ind"), "{}".format(i)):
		fields=line.strip().split()
		Index[fields[1]]=(int(fields[0]) -1)
print (Index)
print ("Indexed", len(Index), "individuals.", sep =" ", file=sys.stderr)

#Extract function
if args.Extract == True:
	for line in GenoFile:
		fields=line.strip()
		for i in Index:
			print (fields[Index[i]], end="")
		print("")




