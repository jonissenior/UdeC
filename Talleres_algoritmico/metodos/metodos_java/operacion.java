package Talleres_algoritmico.metodos.metodos_java;

import javax.swing.JOptionPane;

public class operacion {
    //Atributos
    int num1;
    int num2;
    int suma;
    int resta;
    int multiplicacion;
    int division;        

    //Metodos

    //Metodo para pedir numeros al usuario
    public void leernumeros(){

        num1 = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        num2 = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
    }
    //Metodo para sumar ambos numeros

    public void suma(){
        suma = num1 + num2;
    }

    //Metodo para restar ambos numeros
    
    public void resta(){
        resta = num1 - num2;
    }
    //Metodo para multiplicar ambos numeros
    
    public void multiplicacion(){
        multiplicacion = num1 * num2;
    }
    //Metodo para dividir ambos numeros
    
    public void division(){
        division = num1 / num2;
    }

    public void mostrarResultado(){
        System.out.println("La suma es: "+suma);
        System.out.println("La resta es: "+resta);
        System.out.println("La multiplicacion es: "+multiplicacion);
        System.out.println("La division es: "+division);

    }

}
