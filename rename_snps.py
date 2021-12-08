#!/usr/bin/env python3
import sys,argparse

VERSION='0.0.1'

def read_line(line, format):
    fields=line.strip().split()
    if format == "EIGENSTRAT":
        (id, chrom, _, pos) = fields[:4]
    if format == "PLINK":
        (chrom, id, _, pos) = fields[:4]
    return (chrom+"_"+pos, id)

parser = argparse.ArgumentParser(usage="%(prog)s (-i <input .snp file>) (-n <named snp file>) [-f <named file format>]" , description="Rename the SNPs in an eigenstrat snp file based on a reference eigenstrat or plink snp file. Uses the genetic coordinate of SNPs to determine identity.")
parser._optionals.title = "Available options"
parser.add_argument("-i", "--Input", type=str, metavar="<input .snp file>", required=True, help="The input snp file.")
parser.add_argument("-n", "--Name_file", type=str, metavar="<named snp file>", required=True, help="An Eigenstrat or plink formatted snp file with the desired SNP names.")
parser.add_argument("-f", "--Format", type=str, default="EIGENSTRAT", metavar="<named file format>", required=False, help="The format of the desired snp name file. Can be either 'EIGENSTRAT' or 'PLINK' [default: EIGENSTRAT]")
parser.add_argument("-v", "--version", action='version', version="%(prog)s {}".format(VERSION), help="Print the version and exit.")
args = parser.parse_args()

if args.Format not in ["PLINK", "EIGENSTRAT"]:
    raise ValueError("Invalid format specified for desired SNP name file: '{}'".format(args.Format))


## First, create an index of names for each position in the named snp file.
names={}
for line in open(args.Name_file):
    (fake_id, real_id) = read_line(line, args.Format)
    names[fake_id]=real_id

## Then read the input snp file and rename the snps that can be renamed
for line in open(args.Input, 'r'):
    fields=line.strip().split()
    (id, chrom, dist, pos) = fields[:4]
    if chrom+"_"+pos in names.keys():
        new_id = names[chrom+"_"+pos]
    else:
        new_id = id
    print(new_id, chrom, dist, pos, *fields[4:], sep="\t", file=sys.stdout)

