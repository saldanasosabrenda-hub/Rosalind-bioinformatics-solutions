with open ('rosalind_subs.txt', 'r') as data:
    sequence = data.readline().strip()
    motif = data.readline().strip()

incidencias = []
for base in range (0, len(sequence) - len(motif) + 1):
    if sequence[base: base + len(motif)] == motif:
        incidencias.append (base +1)
print (*incidencias)