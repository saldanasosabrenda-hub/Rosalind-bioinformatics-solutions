A_count, C_count, G_count, T_count = 0,0,0,0
with open ('dna.txt' , 'r') as dna_file:

    for line in dna_file:
        for nucleotide in line:
            if nucleotide == 'A':
                A_count += 1
            elif nucleotide == 'C':
                C_count += 1
            elif nucleotide == 'G':
                G_count += 1
            elif nucleotide == 'T':
                T_count +=1
    
print (A_count, C_count, G_count, T_count)