# Eigenstrat Database Tools
A tool to check two different EingenStrat databses for shared individuals, and extract or remove individuals from an EigenStrat database.

```
usage: EigenStratDatabaseTools.py (-i <Input file prefix>) (-c <input ind file> | -R | -E) [-L <SAMPLE LIST> | -S Ind [-S Ind2]] [-o <OUTPUT FILE PREFIX>]

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
                        ```
