a = float(input())     
b = str(input()).upper()[0]
tupla1 = (a, b)

c = float(input())
d = str(input()).upper()[0]
tupla2 = (c, d)

def temperatura(n,m):
  if n[1] == m[1]:
    t1 = n[0]+m[0]
    return t1.__round__(4), n[1]
  
  elif n[1] != 0:
    if n[1] == 'C' and m[1] == 'F':
        fahre = (n[0] * (9/5)) + 32
        t2 = fahre + m[0]
        return t2.__round__(4), m[1]

    elif n[1] == 'F' and m[1] == 'C':
        celsius = (n[0] - 32) * (5/9)
        t3 = celsius + m[0]
        return t3.__round__(4), m[1]
    
print(temperatura(tupla1, tupla2))
