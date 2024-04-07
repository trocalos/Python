# @title Texto de título predeterminado
n=int(input("Introduce un número: "))
lista=[]
b=0
for a in range(1,n+1):
  if n%a==0:
    lista.append(a)
    b=b+1
print(lista)
c=len(lista)
print(b,c)
print("Los números divisores de",n,"son",b,"y son exactamente los números",lista)
