with open ('rosalind_hamm.txt', 'r') as data:
    seq_a= data.readline().strip()
    seq_b = data.readline().strip()
    hd= 0
    for base_a,base_b in zip(seq_a, seq_b):
        if base_a != base_b:
            hd += 1
            
print (hd)