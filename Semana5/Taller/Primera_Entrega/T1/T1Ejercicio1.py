
from base64 import encode
from cmath import pi
from re import X
from turtle import clear, end_fill
import numpy as np

print("Prueba1!")

# ASIGNO VARIABLES
#Código estudiante 
x = 2 + 1 + 8 + 4 + 1 + 4 + 3
E = 200 * 1000
Angulo_BC = 40  
Angulo_BE = 50 

#Cables
L = 1.5
Acable = ( (pi / 4 ) * ( 6.35 ) ** 2 )

#Barra
l = ((x) * 0.2)

#Pasadores
Apasador = ( ( pi / 4 ) * ( 12.7 ) ** 2 ) 

#Fluencia - factor de seguridad, teórico, admisible 

fy = 250
admy = int(fy / 1.23) 


#Rotura - factor de seguridad, teórico, admisible

fu = 400
admu = int(fu / 1.26) 


#SOLUCIÓN

adm = ( admy, admu )

F_Cables = (Acable * adm)

#Pasadores C D E 
F_PasadoresS = Apasador * adm
#Pasadores A B
F_PasadoresD = 2 * Apasador * adm

F = [ F_Cables, F_PasadoresS, F_PasadoresD ]
F_max = min(F_Cables, F_PasadoresS, F_PasadoresD)
 
matriz = np.array([
    [1, 0, 0], 
    [0, 1, -1],
    [0, 0, - l/2 ]
])

vector = np.array([np.sin(Angulo_BC)*F_BC-np.sin(Angulo_BE)*F_BE, -np.cos(Angulo_BC)*F_BC - np.cos(Angulo_BE)*F_BE - F_max, -l * np.cos(Angulo_BC)*F_BE - l * np.cos(Angulo_BE)*F_BE - l * F_max])

solution = np.linalg.solve(matriz,vector)

WMax = solution[2]

Ax = solution[0]
Ay = solution[1]

print("1." " " " W es igual a: " + str( WMax) + " N")
print("2." " " " La fuerza en la reacción AX es igual a " + str( Ax) )
print("2." " " " La fuerza en la reacción AY es igual a " + str( Ay) )

Def_BC = F_BC * l / (Acable * E )
Def_BD = F_BD * l / (Acable * E )
Def_BE = F_BE * l / (Acable * E )

encode