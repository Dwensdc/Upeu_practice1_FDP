def postulanteCarreraEstMultiple():
  #Definir Variables
  notaFinal=0.0
  #Datos de Entrada
  areaCarreraNcomp=input("Ingrese el area a la que pertenece su carrera\nB=Biomedicas\nI=Ingenieria\nS=Sociales:")
  notaEP=float(input("Ingrese la nota de EP:"))
  notaRM=float(input("Ingrese la nota de RM:"))
  notaRV=float(input("Ingrese la nota de RV:"))
  notaAB=float(input("Ingrese la nota de AB:"))
  #Proceso
  if areaCarreraNcomp=="B":
    notaFinal=(notaEP*0.40)+(notaRM*0.10)+(notaRV*0.20)+(notaAB*0.30)
    areaCarreraNcomp="Biomedicas"
  elif areaCarreraNcomp=="I":
    notaFinal=(notaEP*0.40)+(notaRM*0.30)+(notaRV*0.15)+(notaAB*0.15)
    areaCarreraNcomp="Ingenierias"  
  elif areaCarreraNcomp=="S":
    notaFinal=(notaEP*0.40)+(notaRM*0.10)+(notaRV*0.30)+(notaAB*0.20);
    areaCarreraNcomp="Sociales";
  else:
    print("La opcion que ingreso no existe! intente nuevamente....")
  #Datos de Salida
  print("La persona obtuvo una nota de: ", notaFinal," y su carrera es del area : ",areaCarreraNcomp) 
