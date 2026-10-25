with open ('rosalind_cons.txt', 'r')  as data:
    sequences = []
    actual_seq = ''
    for line in data:
        line= line.strip()
        if line.startswith('>'):
             if actual_seq:
                 sequences.append(actual_seq)
                 actual_seq = ""
        else: 
            actual_seq += line
    if actual_seq:
        sequences.append(actual_seq)
        
Ac, Gc, Cc, Tc = [],[],[],[]

for col in range (0,len(sequences[0])):
    actual_col = []
    for sequence in sequences:
        actual_col.append(sequence[col])
        
    Ac.append (actual_col.count('A'))
    Cc.append (actual_col.count('C'))
    Gc.append (actual_col.count('G'))
    Tc.append (actual_col.count('T'))
    
    consensus = ''
    for base in range(0,len(Ac)):
        frequency = {
            'A' : Ac[base], 'C': Cc[base], 'G': Gc[base], 'T':Tc[base] }
        consensus_letter = max(frequency, key=frequency.get)
        consensus += consensus_letter
        
print(consensus)
print('A:', *Ac)
print('C:', *Cc)
print('G:', *Gc)
print('T:', *Tc)
       
       

    

            