//En este programa se hace una calculadora muy sencilla
//Empezamos con mostrar las opciones
#include <iostream>
#include <math.h>
using namespace std;
int main(){
    //Definimos las variables
    int opciones = 0;
    float a = 0;
    float b = 0;
    float resultado = 0; // Mover la declaración de resultado aquí
    //Mostramos opciones y recogemos
    cout << "Bienvenido a la calculadora" << endl;
    cout << "Elija su opcion " << endl;
    cout << "1.Suma, 2.Resta, 3.Multiplicacion, 4.Division ==> "; cin >> opciones;
    cout << "Ingrese el primer numero ==> "; cin >> a;
    cout << "Ingrese el segundo numero ==> "; cin >> b;
    //Usamos un switch para ejecutar las opciones
    switch (opciones)
    {
    case 1:
        resultado = a + b;
        cout << "La suma es: " << resultado;
        break;
    case 2:
        resultado = a - b;
        cout << "La resta es: " << resultado;
        break;
    case 3:
        resultado = a * b;
        cout << "La multiplicacion es: " << resultado;
        break;
    case 4:
        if(b != 0) { // Añadir comprobación para evitar división por cero
            resultado = a / b;
            cout << "La division es: " << resultado;
        } else {
            cout << "Error: No se puede dividir por cero.";
        }
        break;
    default:
        cout << "Esa opcion aun no esta amiguito";
        break;
    }
    return 0; // Añadir retorno de la función main
}
