k=23
m=24
n=29
total = k+m+n 
prob_nn = ((n/total) * ((n-1) / (total -1))) * 1.0
prob_mm = ((m/total) * ((m-1) / (total -1))) * 0.25
prob_mn = ((m / total) * (n / (total - 1)) + (n / total) * (m / (total - 1))) * 0.5
prob_recesivo = (prob_nn + prob_mm + prob_mn)
prob_dominante = 1  - prob_recesivo

print (prob_dominante)