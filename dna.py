import sys
import csv


people_database = sys.argv[1]

# people = []

with open (people_database, "r") as f:
    sequence_reader = csv.reader(f)
    dna_str = next(sequence_reader)[1:]
    people_reader = csv.DictReader(f)
    for row in people_reader:
        print (row)

print(dna_str)


dna_material = sys.argv[2]


with open (dna_material, "r") as f:
    dna = f.read()

print(dna)    

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
        
# print(sequences)

# print(people)
# print(dna)


# print(len(unique_sequences))
# print(len(sequences))

        