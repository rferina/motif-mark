# Motif-Marker Visualizer
### Rachel Ferina

## Overview

This script takes in an input fasta file and input motif file. It outputs an image (png file) with the same name as the input fasta file.


## Software Versions

Python: 3.10.9

The conda environment my_pycairo must be activated, which includes Pycairo version 1.21.0.

## Command to Run Script

The conda environment must first be activated.
    conda activate my_pycairo

To run the script, the following argparse arguments must be specified.
-f: the input fasta filename
-m: the input motif filename

Full example:
    python motif-mark-oop.py -f test_fa.fasta -m test_motif.txt