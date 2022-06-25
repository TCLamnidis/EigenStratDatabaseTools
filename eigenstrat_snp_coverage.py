#!/usr/bin/env python3

import argparse,json, sys
import pandas as pd
from collections import OrderedDict

VERSION = "1.1.0"

## A function to return the number of lines of a file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

## A function to return the number of genotypes per line in a .geno file. 
def file_width(fname):
    with open(fname) as f:
        for i in f:
            return(len(i.strip()))
            break

## Function to check the consistency of an eigenstrat database
def validate_eigenstrat(genof, snpf, indf):
  dimsGeno = [file_len(genof), file_width(genof)]
  linesSnp = file_len(snpf)
  linesInd = file_len(indf)
  
  # print(dimsGeno,linesSnp,linesInd)
  ##Check geno and snp compatibility
  if dimsGeno[0] !=  linesSnp:
      raise IOError("Input .snp and .geno files do not match.")

  ##Check geno and ind compatibility
  if dimsGeno[1] !=  linesInd:
      raise IOError("Input .ind and .geno files do not match.")

## Function to get individual names and number of individuals from an ind file
def get_ind_names(indf):
  ind_list = []
  with open(indf,'r') as f:
    for line in f:
      fields = line.strip().split()
      ind = fields[0]
      ind_list.append(ind)
  return (ind_list, len(ind_list))

parser = argparse.ArgumentParser(usage = "%(prog)s (-i <Input file prefix>) [-s <Input file suffix>] [-o <Output filepath>] [-j | --json]" , description = "A tool to check two different EingenStrat databses for shared individuals, and extract or remove individuals from an EigenStrat database.")
parser._optionals.title = "Available options"
parser.add_argument("-g", "--genoFn", type = str, metavar = "<GENO FILE NAME>", required = True, help = "The path to the input geno file.")
parser.add_argument("-s", "--snpFn", type = str, metavar = "<SNP FILE NAME>", required = True, help = "The path to the input snp file.")
parser.add_argument("-i", "--indFn", type = str, metavar = "<IND FILE NAME>", required = True, help = "The path to the input ind file.")
parser.add_argument("-o", "--Output", type = str, metavar = "<OUTPUT FILEPATH>", required = False, help = "The filepath where the output table should be saved. Omit to print to stdout.")
parser.add_argument("-j", "--json", type = str, metavar = "<JSON OUTPUT FILEPATH>", default = None, help = "Create additional json formatted output file named <JSON OUTPUT FILEPATH> .")
parser.add_argument("-v", "--version", action='version', version="%(prog)s {}".format(VERSION), help="Print the version and exit.")
args = parser.parse_args()

## Set dynamic output files
if args.Output ==  None:
  out_file = sys.stdout
else:
  out_file = open(args.Output, 'w')

if args.json == None:
  json_output = None
else:
  json_output = args.json

## Initialise empty data table as dictionary
data = {}
## Add script metadata
data['Metadata'] = {'tool_name' : "EigenStratSnpCoverage.py", "version" : VERSION}

## Get input file paths
genof = args.genoFn
snpf = args.snpFn
indf = args.indFn
  
## Perform checks on Eigenstrat dataset
validate_eigenstrat(genof, snpf, indf)

## Initialise coverage dictionary and infer number of individuals
ind_list,num_inds = get_ind_names(indf)

## Add entries for the individuals in data table
for ind in ind_list:
  data[ind]={"Covered_Snps":0, "Total_Snps":file_len(snpf)}

## Read in the genotype matrix (in chunks) and count non-missing calls per individual to add to data table
for genotypes in pd.read_fwf(genof, widths = [1 for _ in range(num_inds)], max_rows=10, names=ind_list, header = None, chunksize=250000):
  for ind in ind_list:
    data[ind]["Covered_Snps"]+=sum(genotypes[ind]!=9)

## Print output and dump json
print ("#Sample", "#SNPs_Covered", "#SNPs_Total", sep="\t", file=out_file)
for ind in ind_list:
  print(ind, data[ind]["Covered_Snps"], data[ind]["Total_Snps"], sep="\t", file=out_file)

if json_output != None:
  with open(json_output, 'w') as json_outfile:
    json.dump(data, json_outfile)
  
