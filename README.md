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

A tool to check two different EingenStrat databses for shared individuals, and
extract or remove individuals from an EigenStrat database.

Available options:
  -h, --help            show this help message and exit
  -i <INPUT FILES PREFIX>, --Input <INPUT FILES PREFIX>
                        The desired input file prefix. Input files are assumed
                        to be <INPUT PREFIX>.geno, <INPUT PREFIX>.snp and
                        <INPUT PREFIX>.ind .
  -o <OUTPUT FILES PREFIX>, --Output <OUTPUT FILES PREFIX>
                        The desired output file prefix. Three output files are
                        created, <OUTPUT FILES PREFIX>.geno , <OUTPUT FILES
                        PREFIX>.snp and <OUTPUT FILES PREFIX>.ind .
  -s <INPUT FILE SUFFIX>, --Suffix <INPUT FILE SUFFIX>
                        The suffix (if any) that follows .geno/.snp/.ind in
                        the input files. For example, specifying '-s .txt'
                        will treat <INPUT PREFIX>.{geno,snp,ind}.txt as the
                        desired input files.
  -C <INPUT FILE>, --Check <INPUT FILE>
                        Check the -i .ind file and the second .ind file for
                        duplicate individuals. Population assignment and/or
                        individual sex are not checked, only individual names.
                        Names are case sensitive.
  -E, --Extract         Extract the selected individuals from the EigenStrat
                        database, creating a new set of EigenStrat files with
                        the selected individuals only.
  -R, --Remove          Remove the selected individuals from the EigenStrat
                        database, creating a new set of EigenStrat files
                        without the selected individuals.
  -L <INDIVIDUAL LIST FILE>, --SampleList <INDIVIDUAL LIST FILE>
                        A list of samples to be Extracted (-E) or Removed (-R)
                        from the database. Can be a list of individual names
                        (1 per line), or the output of duplicate check (-C).
                        Required with -E or -R. Mutually exclusive with -S.
  -S <INDIVIDUAL>, --Sample <INDIVIDUAL>
                        A samples to be Extracted (-E) or Removed (-R) from
                        the database. Can be called multiple times. Required
                        with -E or -R. Mutually exclusive with -L.
  -v, --version         Print the version and exit.

```
---
# Eigenstrat SNP Coverage
A tool to calculate the numbered of covered and total reads for each individual in an EigenStrat dataset. 

```
usage: eigenstrat_snp_coverage.py (-i <Input file prefix>) [-s <Input file suffix>] [-o <Output filepath>] [-j | --json]

A tool to check two different EingenStrat databses for shared individuals, and
extract or remove individuals from an EigenStrat database.

Available options:
  -h, --help            show this help message and exit
  -i <INPUT FILES PREFIX>, --Input <INPUT FILES PREFIX>
                        The desired input file prefix. Input files are assumed
                        to be <INPUT PREFIX>.geno, <INPUT PREFIX>.snp and
                        <INPUT PREFIX>.ind .
  -s <INPUT FILE SUFFIX>, --Suffix <INPUT FILE SUFFIX>
                        The suffix (if any) that follows .geno/.snp/.ind in
                        the input files. For example, specifying '-s .txt'
                        will treat <INPUT PREFIX>.{geno,snp,ind}.txt as the
                        desired input files.
  -o <OUTPUT FILEPATH>, --Output <OUTPUT FILEPATH>
                        The filepath where the output table should be saved.
                        Omit to print to stdout.
  -j, --json            Create additional json formatted output file named
                        <OUTPUT FILE>.json . [Default: '<INPUT FILES
                        PREFIX>_eigenstrat_coverage_mqc.json']
  -v, --version         Print the version and exit.
```
