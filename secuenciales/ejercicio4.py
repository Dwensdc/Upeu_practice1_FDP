def estCondicional101():
  print("======================================================================")
  print("       ALGORITMO PARA DETERMINAR EL DESCUENTO DE UN ARTICULO")
  print("======================================================================")
  #variables
  precio=int(input("ingrese el precio del ARTICULO:"))
  #proceso
  if precio<=100:
   x=precio-(precio*0.10)
   print("SU DESCUENTO ES DE 10% Y SU PRECIO ES DE ",x) 
  else:
    if 200>precio>100:
      x=precio-(precio*0.12)
      print("SU DESCUENTO ES DE 12% Y SU PRECIO ES DE",x) 
    if precio>200:
      x=precio-(precio*0.15)
      print("SU DESCUENTO ES DE 15% Y SU PRECIO ES DE ",x) 
estCondicional101()