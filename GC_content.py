with open ('rosalind_gc.txt', 'r') as fasta:
    lines = fasta.readlines()
    #Open a dictionary to save the secuences
    secuencias = {}
    #Make a variable for the loop
    id_actual = ''
    for linea in lines:
        if linea.startswith('>'): #When a line is an ID
            id_actual = linea.strip() [1:]
            secuencias[id_actual] = ""
        else:
            secuencias[id_actual] += linea.strip()
            
    #for id, secuencia in secuencias.items(): esto solo sirve para poder leerlo en orden
        #print (id,'=', secuencia)

    resultados = {}
    
    for id_seq, dna in secuencias.items(): #Utilizo la clave y el valor al mismo tiempo
         bases = len (dna)
         conteo_gc = dna.count ('G') + dna.count ('C')
         porcentaje_gc = conteo_gc / bases * 100
         
         resultados[id_seq] = porcentaje_gc
         
    id_max = max(resultados, key=resultados.get)

print (id_max)
print (resultados[id_max])