n = 35
k = 4
mes_anterior = 1
mes_actual = 1
for mes in range(3,n +1):
    #el total es = los conejos que tengo + (los conejos que ya pueden reproducirse y que ya tienen al menos un mes de antiguedad)
    nuevo_total = mes_actual + (mes_anterior * k)
    #sobreescribo mes_anterior
    mes_anterior = mes_actual
    #sobreescribo el es actual
    mes_actual = nuevo_total 
    
    
print (mes_actual)