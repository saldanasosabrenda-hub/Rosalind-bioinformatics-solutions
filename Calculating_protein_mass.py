with open('rosalind_prtm.txt', 'r') as data:
    protein = ''
    for line in data:
        line=line.strip()
        protein += line
        
from aminoacidos_dic import mass_table
protein_mass = 0
for aminoacid in protein:
    aminoacid_mass = mass_table[aminoacid]
    protein_mass += aminoacid_mass
    
print(protein_mass)