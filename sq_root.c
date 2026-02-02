#include<stdio.h>
#include<math.h>
double squre_root(long int n){
    double x=n;
    double y=1.0;
    double e=0.000001;
    while(fabs(x-y)>e){
        x=(x+y)/2.0;
        y=n/x;

    }
    return x;

}
int main(){
    long int n;
    printf("Enter the long int number:\n");
    scanf("%ld",&n);
    double res=squre_root(n);
    printf("The result is : %.6f",res);
return 0;
}

