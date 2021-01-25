import sys
import csv

dna = argv[1]

with open dna as f:
    reader = csv.DictReader(f)