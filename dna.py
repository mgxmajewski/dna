import sys
import csv
import itertools,operator

 
# Validate arguments provided by user
if len(sys.argv) < 3:
    print("Provide 2 arguments")
    exit(1)


# Read database of people as a dictionary
people_database = sys.argv[1]

with open(people_database, "r") as f:
    people_reader = csv.DictReader(f)
    people_list = list(people_reader)
        

# Read dna STR which are input to look for
dna_str = []

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

# Check how many dna_srt are there in dna

separated_srt_dna = []

# separator = "-"
# for seq in dna_str:
#     counter = 0
#     for nucleotide in range(len(dna)):
#         seq_len = len(seq)
#         if seq == dna[nucleotide:nucleotide + seq_len]:
#             separated_srt_dna.append(separator)
#             if seq == dna[nucleotide + seq_len : nucleotide + 2 * seq_len]:
#               separated_srt_dna.append(seq)
#                 # print(dna[nucleotide:nucleotide + seq_len])
              
# https://stackoverflow.com/questions/40166522/find-longest-sequence-of-0s-in-the-integer-list         
r = max((list(y) for (x,y) in itertools.groupby((enumerate(A)),operator.itemgetter(1)) if x == 0), key=len)
print(r[0][0]) # prints 12
print(r[-1][0]) # prints 19

print(separated_srt_dna)  
                
# for char in range(len(separated_srt_dna)):
#     if '-' in separated_srt_dna[char] and '-' in separated_srt_dna[char-1]:
#         separated_srt_dna[char] = "x"
   
   
# print(separated_srt_dna)
            
# print(extracted_seq)
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
                
        
        
# print(extracted_seq)
# Print result                
flag = False

for row in people_list:
    temp = row['name'] 
    del row['name']
    # print(row)
    if row == extracted_seq:
        print(temp)
        flag = True

if flag != True:
    print("No match")