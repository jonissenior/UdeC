import java.util.Scanner;

public class Ejercicio_ude {
	
	public static void main(String[] arg) {
		
		Scanner leer = new Scanner(System.in);
		System.out.println("Hay 5 opciones de peliculas:");
		System.out.println("1. Cars");
		System.out.println("2. Up");
		System.out.println("3. Buscando a Nemo");
		System.out.println("4. Ralph el demoledor");
		System.out.println("5. La bruja de blair :)");
		System.out.println("Ingrese un numero que sera su opcion ==> ");
		int n = leer.nextInt();
		
		switch(n){
			case 1:
				System.out.println("Asi que cars, BRUMMM");
				break;
			case 2:
				System.out.println("Up, QUE BONIS");
				break;
			case 3:
				System.out.println("VAMOS POR NEMO");
				break;
			case 4:
				System.out.println("ROMPELO RALP");
				break;
			case 5:
				System.out.println("QUE MIEDOTOOTOTOTOTOT NOOOO");
				break;
			default:
				System.out.println("Esa opcion no es niguna peli :C");
				break;
		}
		
	}

}
