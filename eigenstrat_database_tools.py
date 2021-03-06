#!/usr/bin/env python3

import sys, argparse, sh

VERSION = "1.0.2"

parser = argparse.ArgumentParser(usage="%(prog)s (-i <Input file prefix>) (-c <input ind file> | -R | -E) [-L <SAMPLE LIST> | -S Ind [-S Ind2]] [-o <OUTPUT FILE PREFIX>]" , description="A tool to check two different EingenStrat databses for shared individuals, and extract or remove individuals from an EigenStrat database.")
parser._optionals.title = "Available options"
parser.add_argument("-i", "--Input", type=str, metavar="<INPUT FILES PREFIX>", required=True, help="The desired input file prefix. Input files are assumed to be <INPUT PREFIX>.geno, <INPUT PREFIX>.snp and <INPUT PREFIX>.ind .")
parser.add_argument("-o", "--Output", type=str, metavar="<OUTPUT FILES PREFIX>", required=False, help="The desired output file prefix. Three output files are created, <OUTPUT FILES PREFIX>.geno , <OUTPUT FILES PREFIX>.snp and <OUTPUT FILES PREFIX>.ind .")
parser.add_argument("-s", "--Suffix", type = str, metavar = "<INPUT FILE SUFFIX>", required = False, default = '', help = "The suffix (if any) that follows .geno/.snp/.ind in the input files. For example, specifying '-s .txt' will treat <INPUT PREFIX>.{geno,snp,ind}.txt as the desired input files.")
group = parser.add_mutually_exclusive_group(required=True)
group2 = parser.add_mutually_exclusive_group(required=False)
group.add_argument("-C", "--Check", type=argparse.FileType('r'), metavar="<INPUT FILE>", required=False, help="Check the -i .ind file and the second .ind file for duplicate individuals. Population assignment and/or individual sex are not checked, only individual names. Names are case sensitive.")
group.add_argument("-E", "--Extract", action="store_true", required=False,help="Extract the selected individuals from the EigenStrat database, creating a new set of EigenStrat files with the selected individuals only.")
group.add_argument("-R", "--Remove", action="store_true", required=False,help="Remove the selected individuals from the EigenStrat database, creating a new set of EigenStrat files without the selected individuals.")
group2.add_argument("-L", "--SampleList", type=argparse.FileType('r'), metavar="<INDIVIDUAL LIST FILE>", required=False, help="A list of samples to be Extracted (-E) or Removed (-R) from the database. Can be a list of individual names (1 per line), or the output of duplicate check (-C). Required with -E or -R. Mutually exclusive with -S.")
group2.add_argument("-S", "--Sample", action="append", metavar="<INDIVIDUAL>", required=False, help="A samples to be Extracted (-E) or Removed (-R) from the database. Can be called multiple times. Required with -E or -R. Mutually exclusive with -L.")
parser.add_argument("-v", "--version", action='version', version="%(prog)s {}".format(VERSION), help="Print the version and exit.")
args = parser.parse_args()

if args.Extract is True or args.Remove is True:
	if args.SampleList is None and args.Sample is None:
		parser.error("Sample (-S) or SampleList (-L) required for -R/-E functions.")

if args.Extract is True or args.Remove is True:
	if args.Output is None:
		parser.error("Output files (-o) must be specified when using -R/-E functions")

IndFile = open(args.Input+".ind"+args.Suffix, "r")
GenoFile = open(args.Input+".geno"+args.Suffix, "r")
SnpFile = open(args.Input+".snp"+args.Suffix, "r")


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
			print ("{:25s}".format(ind), "<---", "Duplicate individual", sep="\t", file=sys.stdout)
			c+=1
	print ("#Duplicate individual check finished.", c, "duplicate individuals found.", sep=" ", file =sys.stdout)
	sys.exit(0)

#Check for errors in input files
##Check geno and snp compatibility
lineNo = ""
for line in sh.grep(sh.wc("-l", args.Input+".geno"+args.Suffix, args.Input+".snp"+args.Suffix), args.Input):
	if lineNo=="":
		lineNo=line.strip().split()[0]
	elif lineNo==line.strip().split()[0]:
		break
	elif lineNo!=line.strip().split()[0]:
		raise IOError("Input .snp and .geno files do not match.")

##Check geno and ind compatibility
with open(args.Input+".geno"+args.Suffix, "r") as f:
	for line in f:
		if str(len(line.strip())) == sh.wc("-l", args.Input+".ind"+args.Suffix).strip().split()[0]:
			break
		else:
			raise IOError("Input .ind and .geno files do not match.")

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

if args.Remove == True:
	print ("Detected", len(Samples), "individuals for REMOVAL.", sep=" ", file=sys.stderr)
elif args.Extract == True:
	print ("Detected", len(Samples), "individuals for EXTRACTION.", sep=" ", file=sys.stderr)

#Get sample index in geno and ind files.
Index = {}
Sex = {}
Pop = {}
for i in Samples:
	for line in sh.grep(sh.cat("-n",args.Input+".ind"+args.Suffix), "{}".format(i),_ok_code=[0,1]):
		fields=line.strip().split()
		if fields[1] == i:
			Index[fields[1]]=(int(fields[0]) -1)
			Sex [fields[1]]=fields[2]
			Pop [fields[1]]=fields[3]

print ("Indexed", len(Index), "individuals.", sep =" ", file=sys.stderr)

IndOutFile = open(args.Output+".ind", "w")
GenoOutFile = open(args.Output+".geno", "w")
SnpOutFile = open(args.Output+".snp", "w")

#Extract function
if args.Extract == True:
	for line in GenoFile:
		fields=line.strip()
		for i in Samples:
			if i in Index:
				print (fields[Index[i]], end="", file=GenoOutFile)
		print("",file=GenoOutFile)
	
	for i in Samples:
		try: print (i, Sex[i], Pop[i], sep="\t", file=IndOutFile)
		except KeyError:
			print ("Individual \"",i,"\" not found in ",args.Input+".ind"+args.Suffix+" file.", sep="", file=sys.stderr)
	
	for line in SnpFile:
		print (line, end="", file =SnpOutFile)
	print ("Extraction of ", len(Index)," individuals complete.", sep="", file=sys.stderr)
	sys.exit(0)

#Remove function
sorted_indx = tuple(sorted(Index.values()))

if args.Remove == True:
	for line in GenoFile:
		count=0
		repeat=0
		fields=line.strip()
		for i in range(len(sorted_indx)+1):
			if repeat == len(sorted_indx):
				print (fields[count:], end = "", file=GenoOutFile)
				break
			else:
				print (fields[count:sorted_indx[i]], end="", file=GenoOutFile)
			count=sorted_indx[i]+1
			repeat += 1
		print("",file=GenoOutFile)

	for line in IndFile:
		fields=line.strip().split()
		if fields[0] not in Samples:
			print (line, end="", file=IndOutFile)


	for line in SnpFile:
		print (line, end="", file=SnpOutFile)
	print ("Removal of ", len(Index)," individuals complete.", sep="", file=sys.stderr)
	sys.exit(0)

