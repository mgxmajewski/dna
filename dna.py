import sys
import csv

 
# Read database of people as a dictionary


if len(sys.argv) < 3:
    print("Provide 2 arguments")
    exit(1)


people_database = sys.argv[1]


with open(people_database, "r") as f:
    people_reader = csv.DictReader(f)
    people_list = list(people_reader)
        
            
dna_str = []

# Read dna STR which are input to look for
with open(people_database, "r") as f:
    sequence_reader = csv.reader(f)
    dna_str = next(sequence_reader)[1:]

print(dna_str)

# Read DNA sequence as a string
dna_material = sys.argv[2]
with open(dna_material, "r") as f:
    dna = f.read()

# Add dictionary to keep SRT count
extracted_seq = {}
seq_counter = 0

for seq in range(len(dna_str)):
    extracted_seq[dna_str[seq]] = 2

str_found = []
    
# Check how many dna_srt are there in dna 
for seq in range(len(dna_str)):
    for char in range(len(dna)):
        char_last = len(dna_str[seq])
        if dna_str[seq] == dna[char: char + char_last]:
            str_found.append(dna_str[seq])
            if dna_str[seq] == dna[char + char_last: char + 2 * char_last]:
                if dna_str[seq] == dna[char + 2* char_last: char + 3 * char_last]:
                    extracted_seq[dna_str[seq]] += 1
                    str_found.append(dna_str[seq])  

print(extracted_seq)
# # Check how many dna_srt are there in dna 
# for seq in range(len(dna_str)):
#     seq_counter += 1
#     counter = 1
#     for char in range(len(dna)):
#         char_last = len(dna_str[seq])
#         if dna_str[seq] == dna[char: char + char_last]:
#             extracted_seq[dna_str[seq]] = str(counter)
#             if dna_str[seq] == dna[char + char_last: char + 2 * char_last]:
#                 extracted_seq[dna_str[seq]] = str(counter)
#                 counter += 1
                
                
# Print result                
flag = False

for row in people_list:
    temp = row['name'] 
    del row['name']
    print(row)
    if row == str(extracted_seq):
        print(temp)
        flag = True

if flag != True:
    print("No match")