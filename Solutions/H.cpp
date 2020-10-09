#include <bits/stdc++.h>
 
using namespace std;
 
int main (){
    double a, b, c, d, result;

while (scanf("%lf %lf %lf %lf", &a, &b, &c, &d) && !(a==0 && b==0 && c==0 && d==0)){
    result = c *(0.5 * a+ b)/d;

    printf("%.5lf\n", result);
}

  return 0;
}