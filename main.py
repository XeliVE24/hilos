from libs import *
import time 
import threading

"""def Timemaker():
    print ("haciendo tiempo ....")
    time.sleep(2)#segundos
    print("tiempo hecho...")

Timemaker()
t0=time.time()
listHilos=[]
for i in range (4):
    t=threading.Thread(target=Timemaker)
    listHilos.append(t)
    t.start()

for t in listHilos:
    t.join()

tf= time.time()-t0
print("tiempo totalde ejecucion:"(tf))"""

print("hilo principalo hilo")
print()
def contador(inicio,fin):
    arrayNum=[]
    for i in range (inicio,fin+1,1):
        arrayNum.append(i)
        time.sleep(0.01)
    return arrayNum
t0=time.time()
listaNumeros=contador(1,100)
tf=time.time()-t0
print(f"tiempo total de ejecucion: {tf}")
print(listaNumeros)
print("________________________________________________________________________")

print("usando 4 hilos")
print() 

globalArrayNum=[]
def contadorDos(inicio,fin):
    for i in range(inicio,fin+1,1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return globalArrayNum

t0=time.time()
listaHilos=[]


print("---------hardcode-------------------")

t=threading.Thread(target=contadorDos,args=(1,25))
listaHilos.append(t)
t.start()
t=threading.Thread(target=contadorDos,args=(26,50))
listaHilos.append(t)
t.start()
t=threading.Thread(target=contadorDos,args=(51,75))
listaHilos.append(t)
t.start()
t=threading.Thread(target=contadorDos,args=(76,100))
listaHilos.append(t)
t.start()

#"----------------------------")
ArrayNum=[]
def contador3(inicio,fin):
    for i in range(inicio,fin+1,1):
        ArrayNum.append(i)
        time.sleep(0.01)
    return 0

t0=time.time()
listHilos=[]
#numhilos=4

rangos=[(1,25),(26,50),(51,75),(76,100)]
for i ,rango in enumerate (rangos):
   # inicio=1
   # fin=inicio+(rango/numhilos) -1 if i < numhilos -1 else rango 
    t=threading.Thread(target=contador3,args=(rango))#(inicio,fin)
    listHilos.append(t)
    t.start()
    #inicio=fin

for t in listHilos:
    t.join()


tf=time.time()-t0
print(f"tiempo total de ejecucion:{tf}")
print(globalArrayNum)

print("----------------------------")
tf=time.time()-t0
print(f"tiempo total de ejecucion:{tf}")
print(ArrayNum)