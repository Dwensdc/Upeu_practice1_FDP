import scala.io.StdIn.readLine
object AreaTSC { 
  def main(args:Array[String]) = { 
    //declaracion de variables y otros
    println("ejercicio 01: Area del triangulo")
    //datos de entrada
    println("ingrese base:")
    val b = readLine().toInt
    println("ingrese altura:")
    val h = readLine().toInt
    //proceso
    val area=(b*h)/2
    //datos de salida
    println("el area del triangulo es:"+area)
  }
}   