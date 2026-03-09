import math
from collections import Counter

def get_lcm_gcd(a, b):
    return abs(a * b) // math.gcd(a, b)

def get_prime_factors(n):
    factors = []
    d, temp = 2, abs(n)
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1: factors.append(temp)
    return Counter(factors)

print("\n--- LCM Calculator ---")
try:
    num1 = int(input("Enter first large number: "))
    num2 = int(input("Enter second large number: "))

    lcm_gcd = get_lcm_gcd(num1, num2)
    
    f1, f2 = get_prime_factors(num1), get_prime_factors(num2)
    all_primes = set(f1.keys()) | set(f2.keys())
    lcm_prime = 1
    for p in all_primes:
        lcm_prime *= (p ** max(f1[p], f2[p]))

    print(f"LCM (GCD Method): {lcm_gcd}")
    print(f"LCM (Prime Method): {lcm_prime}")
except ValueError:
    print("Invalid input. Please enter numbers.")
