def estCondicional101():
  #definir variables y otros
  print("ejemplo estructura Condicional en python")
  montoP=0
  #datos de entrada
  cantidadX=int(input("ingrese la cantidad de lapices:"))
  #proceso
  if cantidadX>=1000:
    montoP=cantidadX*0.80
  else:
    montoP=cantidadX*0.90
  #datos de salida
  print("el monto a pagar es:",montoP)    
estCondicional101()  