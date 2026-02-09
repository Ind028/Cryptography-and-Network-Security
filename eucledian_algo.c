#include <stdio.h>
int findGCD(long int a, long int b) {
    if (a == 0)
        return b;
    return findGCD(b % a, a);
}
int main() {
    long int a, b, r;
    printf("Enter two long int numbers:\n");
    scanf("%ld %ld", &a, &b);
    int result=findGCD(a,b);
    printf("GCD is %ld\n", result);
    return 0;
}
