#RSA Public-Key Encryption and Decryption
p,q=61,53
n=p*q
phi=(p-1)*(q-1)
e=17
d=pow(e,-1,phi)
msg=65
enc=pow(msg,e,n)
dec=pow(enc,d,n)
print(msg)
print((e,n))
print((d,n))
print(enc)
print(dec)
