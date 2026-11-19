#Diffie-Hellman Key Exchange
p=23
g=5
a=6
b=15
A=pow(g,a,p)
B=pow(g,b,p)
key1=pow(B,a,p)
key2=pow(A,b,p)
print(A)
print(B)
print(key1)
print(key1==key2)
