import sys
import csv

 
# Read database of people as a dictionary
people_database = sys.argv[1]



with open (people_database, "r") as f:
    people_reader = csv.DictReader(f)
    people_list = list(people_reader)
        
            
# print(people_list)
            


dna_str = []

# Read dna STR which are input to look for
with open (people_database, "r") as f:
    sequence_reader = csv.reader(f)
    dna_str = next(sequence_reader)[1:]

# print(dna_str)
# for seq in range(len(dna_str)):
#     print(dna_str[seq])

# Read DNA sequence as a string
dna_material = sys.argv[2]
with open (dna_material, "r") as f:
    dna = f.read()

print(type(dna))

extracted_seq = {}

# Check how many dna_srt are there in dna 
for seq in range(len(dna_str)):
    counter = 1
    for char in range(len(dna)):
        if dna_str[seq] == dna[char:char+len(dna_str[seq])]:
            if dna_str[seq] == dna[char+len(dna_str[seq]):char+ 2*len(dna_str[seq])]:
                counter +=1
                extracted_seq[dna_str[seq]] = counter
                # print(dna_str[seq] + " " + str(counter))
                # extracted_seq.append(dna[char:char+len(dna_str[seq])])
            # if dna_str[seq]
            # print(dna_str[seq] + "#" + dna[char:char+len(dna_str[seq])])
        # print(dna[seq:len(dna_str[seq])])
        # print(dna_str[seq])
        # if dna_str[seq] == dna[seq:len(dna_str[seq])]:
        #     print(dna[seq:len(seq)])




# for key, value in people_reader.items():
#     if key not in name:
#         print( key, value)

for row in people_list:
    for key, value in row.items():
        if key not in 'name':
            print(key, value, end=" ")
    
    print(row['name'])
            
 
 
 
 
# print(extracted_seq)


# sequences = []

# i = 0

# for i in range (i, len(nucleotide), i+4):
#     sequences.append(nucleotide[i:i+4])
#     i += 1


# unique_sequences = []

# x = len(sequences)
# for k in range(x):
#     if sequences[k] not in unique_sequences:
#         unique_sequences.append(sequences[k])

# print(sequences)

# print(people)
# print(dna)


# print(len(unique_sequences))
# print(len(sequences))

