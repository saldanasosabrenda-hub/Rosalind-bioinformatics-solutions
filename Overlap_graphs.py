with open ('rosalind_grph.txt','r') as data:
    sequences = {}
    current_id= ''
    for line in data:
        line = line.strip()
        if line.startswith('>'):
            if current_id:
                sequences[current_id] = current_seq
            current_id = line[1:]
            current_seq = ''
        else:
            current_seq += line
    if current_id:
        sequences[current_id] = current_seq

    for id_1,seq_1 in sequences.items():
        for id_2, seq_2 in sequences.items():
            if id_1 != id_2:
                if seq_1[-3:] == seq_2[:3]:
                    print(id_1, id_2)