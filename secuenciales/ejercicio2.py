def estCondicional101():
  print("======================================================================")
  print("SUELDO SEMANAL DE UN EMPLEADO CON BASE AL PAGO POR HORA Y ALAS HORAS TRABAJADS,SI SE SUPERAN LAS 40 HORAS SE PAGARA EL DOBLE ")
  print("======================================================================")
  #variables
  M=int(input("ingrese el pago por hora:"))
  X=int(input("ingrese las horas trabajadas:"))
  #proceso
  if X>40:
    pago=(M*40)*2
  else:
    pago=M*40
  #salida
  print("SU SUELDO SEMANAL ES:",pago)
estCondicional101()