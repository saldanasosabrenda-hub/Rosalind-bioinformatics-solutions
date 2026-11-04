with open ('rosalind_revc.txt', 'r') as file:
    dna = file.readline()
    tabla_cambio = dna.maketrans ('ATCG','TAGC')
    complementary_dna = dna[::-1].translate(tabla_cambio)
    print (complementary_dna)