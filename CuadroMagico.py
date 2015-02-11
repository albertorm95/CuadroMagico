# -*- coding: cp1252 -*-
#Crear cuadro magico de 1 a 9
#Empieza en el centro con 1 y luego uno arriba y a la izq, si no abajo
#2,3,4,5...
#El primer [fila] [columna] [[fila]columna]

print "CUADRO MAGICO"
tamano=int(raw_input("Ingrese el tamaño del Cuadro: "))
centro=int(tamano/2)
cuadro=[[0 for i in range(tamano)] for i in range(tamano)]
cuadro[0][centro]=1

num=1
fila=0
columna=centro
ubacion=0

print cuadro[tamano-1][tamano-1]

for i in range((tamano*tamano)-1):
    
    for n in range(tamano):    
        print str(cuadro[0:tamano][n])
    print "------------------------------"
    num=num+1
    print "VA EL NUMERO"+str(num)
    print "principio"
    fila=fila-1
    print "fila1"
    print fila
    ubicacion=columna
    print "ubicacion"
    print ubicacion
    columna=columna-1
    print "columna1"
    print columna
    if fila<0:        
        fila=tamano-1
        print "fila2"
        print fila
    if columna<0:        
        columna=tamano-1
        print "columna2"
        print columna
    else:        
        columna=ubicacion-1
        print "columna3"
        print columna
    print "desnalgue"        
    if cuadro[fila][columna]==0:
        print "PRIMER IF ==0"
        cuadro[fila][columna]=num
        
    elif cuadro[fila][columna]!=0:
        print "SEGUNDO IF !=0"
        fila=fila-1
        if fila<0:        
            fila=tamano-1
        print "fila3"
        print fila
        columna=ubicacion
        print cuadro[-1][columna]
        cuadro[fila][columna]=num
       


for n in range(tamano):    
    print str(cuadro[0:tamano][n])

   
raw_input("Press Enter to continue...")
