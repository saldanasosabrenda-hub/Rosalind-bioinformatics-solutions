with open ("rosalind_lcsm.txt", "r") as file:
    sequences_dic = {}
    current_id = ""
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            if current_id:
                sequences_dic[current_id]= actual_seq
            current_id = line[1:]
            actual_seq = ''
        else:
            actual_seq += line
    if current_id:
        sequences_dic[current_id] = actual_seq
        
#make a list with the sequences
sequences_list = list(sequences_dic.values())
#read each sequence and find motif (here i will need a loop)
incidences = []
shortest_seq = min(sequences_list, key=len)
for lenght in range (2 , len(shortest_seq) + 1): 
    for start in range (0, len(shortest_seq) -lenght + 1): 
        current_motif = shortest_seq [start : start + lenght]
        if all (current_motif in seq for seq in sequences_list):
            incidences.append(current_motif)
#look for the longest one
longest_motif = max(incidences, key=len)
print(longest_motif)