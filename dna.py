import sys
import csv


people_database = sys.argv[1]

people = []

with open (people_database, "r") as f:
    people_reader = csv.DictReader(f)
    for person in f:
        people.append(person)


dna_material = sys.argv[2]

dna = []

with open (dna_material, "r") as f:
    reader = csv.reader(f)
    for nucleotide in f:
        dna.append(nucleotide)

sequences = []

i = 0

for i in range (i, len(nucleotide), i+4):
    sequences.append(nucleotide[i:i+4])
    i += 1
    

unique_sequences = []

x = len(sequences)
for k in range(x):
    if sequences[k] not in unique_sequences:
        unique_sequences.append(sequences[k])
        

print(people)
print(dna)


print(len(unique_sequences))
print(len(sequences))

        