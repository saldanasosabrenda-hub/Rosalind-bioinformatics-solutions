import urllib.request
ids = []
keys = []
with open('rosalind_input.txt', 'r') as data:
    for line in data:
        id_line = line.strip()
        keys.append(id_line)
        clean_line = id_line.split('_')[0]
        ids.append(clean_line) 
sequences = []
for uniprot_id in ids:
    current_seq=''
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    with urllib.request.urlopen(req) as response:
        for line in response:
            url_line = line.decode('utf-8').strip()
            if url_line.startswith('>'):
                continue
            else:
                current_seq += url_line
        sequences.append(current_seq)
                            
            
    incidences = {}
    for key, sequence in zip(keys, sequences):
        current_list = []
        for base in range(0, len(sequence)-3):
            if sequence[base] == 'N':
                if sequence[base +1] != 'P':
                    if sequence[base +2] == 'S' or sequence[base +2] == 'T':
                        if sequence[base +3] != 'P':
                            current_list.append(base +1)
            incidences[key] = current_list
    
for id, motifs in incidences.items():
    if motifs:
        print(id)
        print(*motifs)