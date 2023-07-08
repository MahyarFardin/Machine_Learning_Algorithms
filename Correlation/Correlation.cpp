#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>

using namespace std;

void correlation_calculator(int x[], int y[], double &corr){
    int xSum = 0,
        ySum = 0, 
        xySum = 0,
        xSqrSum = 0,
        ySqrSum = 0;

    for (int i = 0 ; i < sizeof(x) ; i++){
        xSum += x[i];
        ySum += y[i];
        xySum += x[i] * y[i];
        xSqrSum += pow(x[i], 2);
        ySqrSum += pow(y[i], 2);
    }

    corr = ((sizeof(x) * xySum - xSum * ySum) / sqrt((sizeof(x)*xSqrSum - pow(xSum, 2))*(sizeof(y)*ySqrSum - pow(ySum, 2))));
}

int main(){
    int numbers = 5;
    int x[numbers];
    int y[numbers];
    double correlation;

    for (int i = 0; i < numbers; i++){
        x[i] = rand();
        y[i] = rand();
    }

    correlation_calculator(x, y, correlation);

    
    cout<<"X: "<<endl;
    for (int i = 0; i < numbers; i++){
        cout<<x[i]<<endl;
    }

    cout<<"y: "<<endl;
    for (int i = 0; i < numbers; i++){
        cout<<y[i]<<endl;
    }

    cout<<"correlation is " << correlation;

    return 0;
}