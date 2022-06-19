a = float(input())     
b = str(input()).upper()[0]
tupla1 = (a, b)

c = float(input())
d = str(input()).upper()[0]
tupla2 = (c, d)


def temperatura(n,m):
  if n[1] == m[1]:
    return max(n[0],m[0]), n[1]   #CERTO
  elif n[1] != m[1]:   #ESCALAS DIFERENTES. CELSIUS DIFERENTE DE FEIHREINHEIT
    if n[1] == 'C':
        celsius = (m[0]-32)*(5/9)
        if celsius < n[0]:
            return n[0], n[1]
        else:
            return m[0], m[1]
    

    elif n[1] == 'F':
        fahre = (m[0]*(9/5))+32
        if fahre < n[0]:
            return n[0], n[1]
        else:
            return m[0], m[1]
      
    
print(temperatura(tupla1, tupla2))


    




