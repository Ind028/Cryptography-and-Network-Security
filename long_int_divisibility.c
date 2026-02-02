#include<stdio.h>
int main(){
    long int n;
    printf("Enter the long int number:\n");
    scanf("%ld",&n);
    for (int i=2;i<=15;i++){
        if(n%i==0){
            printf("\nThe given number %ld is divisible by %d\n",n,i);
        }
        else{
            printf("\nThe given number %ld is not divisible by %d\n",n,i);
        }

    }
return 0;
}