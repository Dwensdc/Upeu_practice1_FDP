def estCondicional101():
  print("======================================================================")
  print("SE DESEA SABER EL NOMBRE Y LA EDAD DE LA PERSONA DE MENOR EDAD")
  print("======================================================================")
  x=0
  #variables
  nombre1=input("ingrese el nombre de la persona 1:")
  edad1=int(input("ingrese la edad de la persona 1:"))
  nombre2=input("ingrese el nombre de la persona 2:")  
  edad2=int(input("ingrese la edad de la persona 2:"))
  nombre3=input("ingrese el nombre de la persona 3:")
  edad3=int(input("ingrese la edad de la persona 3:"))
  #proceso 
  if (edad1<edad2 and edad1<edad3):
    x=print(nombre1,"es menor con su edad",edad1)
  else:
    if (edad2<edad1 and edad2<edad3):
      x=print(nombre2,"es menor con su edad",edad2)
    else:
      x=print(nombre3,"es menor con su edad",edad3)

    
  #salida
estCondicional101()
  