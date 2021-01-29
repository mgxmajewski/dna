import sys
import csv

 
# Read database of people as a dictionary
people_database = sys.argv[1]


with open(people_database, "r") as f:
    people_reader = csv.DictReader(f)
    people_list = list(people_reader)
        
            
dna_str = []

# Read dna STR which are input to look for
with open(people_database, "r") as f:
    sequence_reader = csv.reader(f)
    dna_str = next(sequence_reader)[1:]


# Read DNA sequence as a string
dna_material = sys.argv[2]
with open(dna_material, "r") as f:
    dna = f.read()

# Add dictionary to keep SRT count
extracted_seq = {}
seq_counter = 0


# Check how many dna_srt are there in dna 
for seq in range(len(dna_str)):
    seq_counter += 1
    counter = 1
    for char in range(len(dna)):
        char_last = len(dna_str[seq])
        if dna_str[seq] == dna[char: char + char_last]:
            extracted_seq[dna_str[seq]] = str(counter)
            if dna_str[seq] == dna[char + char_last: char + 2 * char_last]:
                extracted_seq[dna_str[seq]] = str(counter)
                counter += 1
                
                
# Print result                
flag = False

for row in people_list:
    temp = row['name'] 
    del row['name']
    if row == extracted_seq:
        print(temp)
        flag = True

if flag != True:
    print("No match")
