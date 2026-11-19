# Elliptic Curve Arithmetic
p = 17
a = 2

def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if P == Q:
        m = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:
        m = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x = (m * m - x1 - x2) % p
    y = (m * (x1 - x) - y1) % p
    return (x, y)

def mul(k, P):
    R = None
    while k:
        if k % 2:
            R = add(R, P)
        P = add(P, P)
        k //= 2
    return R

P = (5, 1)
print(add(P, P))
print(add(P, P))
print(mul(3, P))
