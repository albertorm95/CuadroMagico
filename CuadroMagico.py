#Crear cuadro magico de 3x3
#veces de intento
victoria=0
#cuadro=[[0 for i in range(4)] for i in range(4)]
cuadro=[[4,9,2],[3,5,7],[8,1,4]]

print "Cuadro Magico de 3x3"
print "Favor diga ubicacion en coordenadas [x,y]"

while (victoria <=15):
    for i in range(2):
        if sum(cuadro[0:3][i])==15:
            victoria=victoria+1
        elif sum(cuadro[0:3][i])!=15:
            victoria=victoria-1
    print victoria
    

        
    #for i in range(3):
        #x=int(raw_input("x: "))#-1
        #y=int(raw_input("y: "))#-1
        #numero=int(raw_input("Ingrese numero: "))
        #cuadro[x][y]=numero

        #print str(cuadro[0][0:3])+"\n"+str(cuadro[1][0:3])+"\n"+str(cuadro[2][0:3])

    

    
raw_input("Press Enter to continue...")
