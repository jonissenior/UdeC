#include <iostream>
using namespace std;

int main(){
    //Definimos variable a usar
    int opcion = 0;
    //PEdir el valor de la opcion que se quiera usar
    cout << "Opciones: 1.Dormir, 2.Videojuegos, 3.Pelicula, 4.Estudiar, 5.Paseo" << endl;
    cout << "Elija la opcion que desea ejecutar ==> "; cin >> opcion;
    //un switch case con todas las opciones puestas segun la eleccion
    switch (opcion)
    {
    case 1:
        cout << "Listo, que descanses muy bien esta noche :)" << endl;
        break;
    case 2:
        cout << "Entonces vamos con toda a por nuevo record!!"<< endl;
        break;
    case 3:
        cout << "Me parece perfecto, es hora de ir por palomitas"<< endl;
        break;
    case 4:
        cout << "Excelente opcion, vamos por el futuro que queremos!"<< endl;
        break;
    case 5:
        cout << "Un buen paseo, el parque debe ser el lugar perfecto" << endl;
        break;
    default:
        cout << "Esa opcion no esta aun, lo lamento :c "<< endl;
        break;
    }

}