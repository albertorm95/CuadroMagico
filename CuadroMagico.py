# -*- coding: cp1252 -*-
#Crear cuadro magico de 1 a 9
#Empieza en el centro con 1 y luego uno arriba y a la izq, si no abajo
#2,3,4,5...
#El primer [fila] [columna] [[fila]columna]
print "CUADRO MAGICO"
tamano=int(raw_input("Ingrese el tamaño del Cuadro: "))
centro=int(tamano/2)
cuadro=[[0 for i in range(tamano)] for i in range(tamano)]

cuadro[0][2]=2
cuadro[1][2]=3
#for n in range(tamano):
print cuadro
print str(cuadro[0:3][0])
print str(cuadro[0][0:3])


#cuadro=[[4,9,2],[3,5,7],[8,1,4]]

#print "Favor diga ubicacion en coordenadas [x,y]"

#while (victoria <=15):
 #   for i in range(2):
  #      if sum(cuadro[0:3][i])==15:
   #         victoria=victoria+1
    #    elif sum(cuadro[0:3][i])!=15:
     #       victoria=victoria-1
    #print victoria
    

        
    #for i in range(3):
     #   x=int(raw_input("x: "))#-1
      #  y=int(raw_input("y: "))#-1
      #  numero=int(raw_input("Ingrese numero: "))
      #  cuadro[x][y]=numero

#        print str(cuadro[0][0:3])+"\n"+str(cuadro[1][0:3])+"\n"+str(cuadro[2][0:3])

    

    
raw_input("Press Enter to continue...")
