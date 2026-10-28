n=80
k=1
m=16
edades = [0] * m
edades[0] = 1 
for mes in range (1,n):
    crias = sum(edades[1:])
    edades = [crias] + edades[:-1]
    
print (sum(edades))