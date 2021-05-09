// Primer programa de ejemplo en C++
 
#include <iostream>
 
int main () {
    //definir variables y otros
    printf("ejercicio 01:Area de un triangulo|n");
    int b=0, h=0, area=0;
    //datos de entrada
    printf("ingrese base:");
    scanf("%i",b);
    printf("ingrese altura:");
    scanf("%i",&h);
    //proceso
    area=(b*h)/2;
    //datos de salida
    printf("area del triangulo es:%i%s",area,"/n");
    return 0;
}