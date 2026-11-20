import math

def probabilidad_aabb(k, N):
    n = 2**k  # Total de individuos en la generación k
    p = 0.25  # Probabilidad de ser AaBb
    
    probabilidad_total = 0
    
    # Sumamos desde N hasta el total de individuos (n)
    for x in range(N, n + 1):
        combinaciones = math.comb(n, x)
        prob_x = combinaciones * (p**x) * ((1 - p)**(n - x))
        probabilidad_total += prob_x
        
    return probabilidad_total 

print (probabilidad_aabb (6,18))