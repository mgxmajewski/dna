import sys
import csv

material = sys.argv[1]

dna = []

with open (material, "r") as f:
    reader = csv.DictReader(f)
    for sequence in f:
        dna.append(sequence)
        print(sequence)
        
        