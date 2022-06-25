# Dependencies
 - python 3.0 or newer  
 - The following python packages installed: `sh`, `argparse`, `pandas`. These can be installed using pip:
```
pip install sh argparse pandas
```

# Eigenstrat Database Tools
A tool to check two different EingenStrat databses for shared individuals, and extract or remove individuals from an EigenStrat database.

```
usage: eigenstrat_database_tools.py (-i <Input file prefix>) (-c <input ind file> | -R | -E) [-L <SAMPLE LIST> | -S Ind [-S Ind2]] [-o <OUTPUT FILE PREFIX>]

A tool to check two different EingenStrat databses for shared individuals, and extract or remove individuals from an EigenStrat database.

Available options:
  -h, --help            show this help message and exit
  -g <GENO FILE NAME>, --genoFn <GENO FILE NAME>
                        The path to the input geno file.
  -s <SNP FILE NAME>, --snpFn <SNP FILE NAME>
                        The path to the input snp file.
  -i <IND FILE NAME>, --indFn <IND FILE NAME>
                        The path to the input ind file.
  -o <OUTPUT FILES PREFIX>, --Output <OUTPUT FILES PREFIX>
                        The desired output file prefix. Three output files are created, <OUTPUT FILES PREFIX>.geno , <OUTPUT FILES PREFIX>.snp and <OUTPUT FILES PREFIX>.ind .
  -C <INPUT FILE>, --Check <INPUT FILE>
                        Check the -i .ind file and the second .ind file for duplicate individuals. Population assignment and/or individual sex are not checked, only individual names. Names are case
                        sensitive.
  -E, --Extract         Extract the selected individuals from the EigenStrat database, creating a new set of EigenStrat files with the selected individuals only.
  -R, --Remove          Remove the selected individuals from the EigenStrat database, creating a new set of EigenStrat files without the selected individuals.
  -L <INDIVIDUAL LIST FILE>, --SampleList <INDIVIDUAL LIST FILE>
                        A list of samples to be Extracted (-E) or Removed (-R) from the database. Can be a list of individual names (1 per line), or the output of duplicate check (-C). Required with -E
                        or -R. Mutually exclusive with -S.
  -S <INDIVIDUAL>, --Sample <INDIVIDUAL>
                        A samples to be Extracted (-E) or Removed (-R) from the database. Can be called multiple times. Required with -E or -R. Mutually exclusive with -L.
  -v, --version         Print the version and exit.
```
---
# Eigenstrat SNP Coverage
A tool to calculate the numbered of covered and total reads for each individual in an EigenStrat dataset.

```
usage: eigenstrat_snp_coverage.py (-i <Input file prefix>) [-s <Input file suffix>] [-o <Output filepath>] [-j | --json]

A tool to check two different EingenStrat databses for shared individuals, and extract or remove individuals from an EigenStrat database.

Available options:
  -h, --help            show this help message and exit
  -g <GENO FILE NAME>, --genoFn <GENO FILE NAME>
                        The path to the input geno file.
  -s <SNP FILE NAME>, --snpFn <SNP FILE NAME>
                        The path to the input snp file.
  -i <IND FILE NAME>, --indFn <IND FILE NAME>
                        The path to the input ind file.
  -o <OUTPUT FILEPATH>, --Output <OUTPUT FILEPATH>
                        The filepath where the output table should be saved. Omit to print to stdout.
  -j <JSON OUTPUT FILEPATH>, --json <JSON OUTPUT FILEPATH>
                        Create additional json formatted output file named <JSON OUTPUT FILEPATH> .
  -v, --version         Print the version and exit.
```
# Rename Snps
A tool to rename the SNPs in an EigenStrat snp file based on a reference EigenStrat or plink snp file. Uses the genetic coordinate of SNPs to determine identity.

```
usage: rename_snps.py (-i <INPUT .SNP FILE>) (-n <NAMED SNP FILE>) [-f <NAMED FILE FORMAT>]

Rename the SNPs in an eigenstrat snp file based on a reference eigenstrat or plink snp file. Uses the genetic coordinate of SNPs to determine identity.

Available options:
  -h, --help            show this help message and exit
  -i <INPUT .SNP FILE>, --Input <INPUT .SNP FILE>
                        The input snp file.
  -n <NAMED SNP FILE>, --Name_file <NAMED SNP FILE>
                        An Eigenstrat or plink formatted snp file with the desired SNP names.
  -f <NAMED FILE FORMAT>, --Format <NAMED FILE FORMAT>
                        The format of the desired snp name file. Can be either 'EIGENSTRAT' or 'PLINK' [default: EIGENSTRAT]
  -v, --version         Print the version and exit.
```