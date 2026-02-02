#include<stdio.h>
#include<math.h>
int squre_root(long int n){
    double x=n;
    double y=1.0;
    double e=0.000001;
    while(fabs(x-y)>e){
        x=(x+y)/2.0;
        y=n/x;

    }
    return x;
}
int prime(long int n){
    long int i;
    double limit=squre_root(n);
    for (i=2;i<= (long int) limit;i++){
        if(n%i==0){
            return 0;
        }
    }
    return 1;
}
int main(){
    long int n;
    printf("Enter the long int number:\n");
    scanf("%ld",&n);
    int x=prime(n);
    if(x==0){
        printf("The given number is a prime number");
    }
    else{
        printf("The given number is a not prime number");
    }
    return 0;
}
