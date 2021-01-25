import sys
import csv

material = sys.argv[1]

dna = []

with open (material, "r") as f:
    reader = csv.DictReader(f)
    for nucleotide in f:
        dna.append(nucleotide)


sequences = []

i = 0


sequences = []

i = 0


for i in range (i, len(nucleotide), i+4):
    sequences.append(nucleotide[i:i+4])
    i += 1


print(sequences)