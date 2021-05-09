import java.util.Scanner;

class AreaTriangulo{ 
  static Scanner teclado=new Scanner(System.in);

  public static void main(String[] arg){
    //definir variables y otros 
    System.out.println("Ejercicio 01:Area Triangulo");
    int b=0, h=0, area=0;
    //datos de entrada por dispositivos de entrada
    System.out.println("ingrese base:");
    b=teclado.nextInt();
    System.out.println("ingrese altura:");
    h=teclado.nextInt();
    //proceso
    area=(b*h)/2;
    //datos de salida
    System.out.println("el area del triangulo es:"+area);
  }
}  