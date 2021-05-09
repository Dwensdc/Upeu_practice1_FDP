package main
import "fmt"
func main(){ 
  //declaracion de variables y otros
  fmt.Println("ejercicio 01:Area triangulo") 
  var b int
  var h int
  var area float64
  //datos de lectura
  fmt.Println("ingrese base:")
  fmt.Scanln(&b)
  fmt.Println("ingrese altura:")
  fmt.Scanln(&h)
  //proceso
  area=float64((b*h)/2)
  //datos de salida
  fmt.Println("el area es:", area)
}