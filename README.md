# Motif-Marker Visualizer
### Rachel Ferina

## Overview

This script takes in an input FASTA file and input motif file. It outputs an image (png file) with the same name as the input fasta file.

Among other elements, a gene includes exons, which are regions that code for proteins, and introns, which are non-protein coding regions. Typically, introns are spliced out to form mature mRNA which can then be translated into protein. Sometimes exons are also spliced out, known as 
casette exons. Casette exons can be alternatively spliced, remaining either in or out of the gene depending on developmental stage and the environment. Motifs are small repeating patterns of sequences that can serve as binding sites of regulatory proteins. When regulatory proteins bind to motifs, it can activate or suppress the inclusion of exons.

This script assumes the input FASTA file contains the sequence of the casette exon, and parts of the surrounding introns. It also assumes the 
sequences are all in the same orientation (reverse complement is not accounted for).

The gene is mapped in the output figure, along with the casette exon. Which motifs are present in all the genes are shown in different colors.
This figure is drawn to scale. Note that 100 was added to every position so the drawings weren't off the page.


## Software Versions

Python: 3.10.9

The conda environment my_pycairo must be activated, which includes Pycairo version 1.21.0.

## Command to Run Script

The conda environment must first be activated.
    
    **conda activate my_pycairo**

To run the script, the following argparse arguments must be specified.

    **-f: the input fasta filename**
    **-m: the input motif filename**

Full example:

    **python motif-mark-oop.py -f test_fa.fasta -m test_motif.txt**