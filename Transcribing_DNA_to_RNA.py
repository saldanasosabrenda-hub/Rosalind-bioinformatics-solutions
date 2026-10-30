with open ('rosalind_rna.txt', 'r') as file:
    DNA = file.readline()
    RNA = DNA.replace('T', 'U')
    print (RNA)