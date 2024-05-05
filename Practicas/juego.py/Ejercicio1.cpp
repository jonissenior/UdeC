#include <iostream>
using namespace std;
 
int area(int a,int b){
    return a*b;
}

int perimetro(int a, int b){
    return 2*(a+b);
}

int main(){
    cout << "El area es: ";
    cout <<  area(4, 5) << endl;
    cout << "El perimetro es: ";
    cout <<  perimetro(6, 3) << endl;

}

