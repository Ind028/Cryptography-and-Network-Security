def extended_gcd(a, b):#find s and t such that as+bt=gcd(a,b)
    if a == 0:
        return b, 0, 1
    gcd, s1, t1 = extended_gcd(b % a, a)
    s = t1 - (b // a) * s1
    t = s1
    return gcd, s, t5
print("Extended Euclidean Algorithm")
try:
    val_a = int(input("Enter integer a: "))
    val_b = int(input("Enter integer b: "))

    d, s, t = extended_gcd(val_a, val_b)

    print(f"\nResults:")
    print(f"GCD: {d}")
    print(f"s: {s}, t: {t}")
    print(f"Equation: ({val_a} * {s}) + ({val_b} * {t}) = {d}")
except ValueError:
    print("Please enter valid integers.")
