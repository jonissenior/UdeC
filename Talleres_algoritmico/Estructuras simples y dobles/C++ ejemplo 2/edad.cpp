#include <iostream>
using namespace std;

//Edad
//Algoritmo para saber si alguien es mayor de edad


int main(){

    int edad = 0;
    //Pedimos el valor de edad
    cout << "Ingrese su edad ==> "; cin >> edad;

    //Con el if logramos identificar si es mayor o menor de edad 
    // y mostramos uno u otro resultado
    if(edad >= 18)
        cout << "Es mayor de edad";

    else 
        cout << "Es menor de edad ";

}




