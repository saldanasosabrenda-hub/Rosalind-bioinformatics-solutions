from aminoacidos_dic import conteo_codones
with open ('rosalind_mrna.txt', 'r') as data:
    line=data.readline().strip()
    sequence =line
    total = 1
    for aminoacid in sequence:
        num_cod = conteo_codones[aminoacid]
        total = (total * num_cod) % 1000000
        
    actual_total = (total * 3)%1000000
    print (actual_total)
    
    
