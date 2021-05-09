fun main(Args: Array<String>){
  //declaracion
  var altura: Int
  var base: Int
  var area: Int
  //datos de entrada
  print("base: ")
  base = readLine()!!.toInt()
  print("altura: ")
  altura = readLine()!!.toInt()
  //proceso
  area = base*altura/2
  //datos de salida
  print("area: ")
  print(area)
}