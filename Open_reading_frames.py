sequence = ''
with open('rosalind_orf.txt', 'r') as data:
    for line in data:
        line = line.strip()
        if line and not line.startswith('>'):
            sequence += line

complementary = str.maketrans('ACGT', 'TGCA')
dna_to_rna = str.maketrans('ATCG', 'AUCG')
complementary_rna = sequence[::-1].translate(complementary).translate(dna_to_rna)
rna_seq = sequence.translate(dna_to_rna)
stop = ['UAA','UGA','UAG']
rna_fragments = set()
for rna in [rna_seq, complementary_rna]:
    for base in range (0,len(rna)):
        if rna[base:base+3] == 'AUG':
            for base2 in range (base+3, len(rna), 3):
                    triplet = rna[base2 : base2 + 3]
                    if triplet in stop:
                        fragment = rna[base : base2 + 3]
                        rna_fragments.add(fragment)
                        break
    
from aminoacidos_dic import tabla_codones
frames = set()
protein= ''
for fragment in rna_fragments:
    for base in range(0,len(fragment),3):
        codon=fragment[base:base+3]
        aminoacid = tabla_codones[codon]
        if aminoacid == 'STOP':
            break
        
        protein +=aminoacid
    frames.add(protein)
    protein = ''
print (*frames, sep='\n')
    

            
        
        