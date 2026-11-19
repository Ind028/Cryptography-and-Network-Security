#RSA PSS
import hashlib
import secrets 
p,q=61,53
n=p*q
phi=(p-1)*(q-1)
e=17
d=pow(e,-1,phi)
msg="hello"
s=secrets.token_bytes(4)
h=hashlib.sha256(msg.encode()+s).digest()
m=int.from_bytes(h,'big')%n
sig=pow(m,d,n)
v=pow(sig,e,n)
print(msg)
print(sig)
print("valid"if v==m else "invalid")
msg2="hello world"
h2=hashlib.sha256(msg2.encode()+s).digest()
m2=int.from_bytes(h2,'big')%n
print("valid" if v==m2 else "rejected")
