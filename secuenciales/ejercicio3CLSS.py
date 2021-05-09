def muestraMenorEdad():
  #Definir Variables y otros
  pnombre=""
  pedad=0
  #Datos de entrada
  p1nombre=input("Ingrese Nombre 1ra Persona:")
  p1edad=int(input("Ingrese edad 1ra Persona:"))
  p2nombre=input("Ingrese Nombre 2da Persona:")
  p2edad=int(input("Ingrese edad 2da Persona:"))
  p3nombre=input("Ingrese Nombre 3ra Persona:")
  p3edad=int(input("Ingrese edad 3ra Persona:"))  
  #Proceso
  if p1edad<p2edad and p1edad<p3edad:
    pnombre=p1nombre
    pedad=p1edad
  elif p2edad<p1edad and
  #datos de salida
  print("la persona con menor edad es:",pnombre,"y su edad es:",pedad)