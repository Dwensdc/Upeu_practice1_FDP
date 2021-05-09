def estCondicional101():
  print("======================================================================")
  print("ALORITMO PARA DAR BECAS A ALUMNOS MENORES Y MAYORES A 18 DEPENDIENDO SU PROMEDIO")
  print("======================================================================")
  #variables
  edad=int(input("ingresar la edad del estudiante:"))
  promedio=int(input("ingresar el promedio del estudiante"))
  #proceso
  if (promedio>=9)and(edad>18):
    print("HAS SIDO RECOMPENSADO CON UNA BECA DE $2.000")
  else:
    if (7.5<promedio<9)and(edad>18):
     print("HAS SIDO RECOMPENSADO CON UNA BECA DE $1.000")
    else:
      if (6<=promedio<7.5)and(edad>18):
        print("HAS SIDO RECOMPENSADO CON UNA BECA DE $500")  
  if (promedio>=9)and(edad<=18):
    print("HAS SIDO RECOMPENSADO CON UNA BECA DE $3.000")
  else:
    if (7.5<promedio<9)and(edad<=18):
     print("HAS SIDO RECOMPENSADO CON UNA BECA DE $2.000")
    else:
      if (6<=promedio<7.5)and(edad<=18):
        print("HAS SIDO RECOMPENSADO CON UNA BECA DE $100")
      else:
        print("EL ALUMNO NO RECIBIO NINGUNA BECA DEBIDO A SU BAJO PROMEDIO")  
  
estCondicional101()  
