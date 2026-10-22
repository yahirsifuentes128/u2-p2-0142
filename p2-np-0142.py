import numpy as np 
# yahir sifuentes NC = 0142 
# ejemplos de numpy         numerical python 
print("------- espaciado linealmente en array ---- 0142 ")
arre=np.linspace(start=0,stop=1,num=5)
print(arre)
print(" ---- matriz identidad en 2D array ---- 0142")
matriz=np.eye(4)
print(matriz)
print("--  genera numeros al azar (aleatorios) en 2D array -- 0142 ")
print(" generarar 12 numeros aleatorios")
numale=np.random.random((3,4)) # genera 12 numeros aleatorios 
print(numale)
print(" generarar 9 numeros aleatorios entre 0 y 1")
numale=np.random.random((3,4)) # genera 9 numeros aleatorios 
print(numale)
# como generar 9 numeros aleatorios conprendidos entre 1 y 20
# con numpy en un arreglo de 3 por 3 
print(" generarar 9 numeros aleatorios entre 0 y 20")
arre=np.random.randint(1,21,size=(3,3))
print(arre)
print("yahir sifuentes NC = 0142 ")





