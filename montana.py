#MONTANA


'''
Un viaje en la montaña rusa del parque de atracciones tarda 5 minutos en completar el recorrido. Cuando llegan los vagones
los visitantes que esperan se suben, pero los que llegan mientras el resto sube deben esperar al siguiente
viaje. La capacidad de los vagones de la atraccion es de 10 pasajeros. Si hay mas de 10 visitantes en la cola
el resto tendra que esperar al siguiente viaje. Cuando todas las personas han subido, la atraccion comienza. Si el
viaje termina y no hay pasajeros (o menos de 5), la siguiente ronda no comenzara hasta que lleguen 5
visitantes lleguen. Entonces la atraccion comenzara.
Escribe un codigo de sincronizacion en python con dos tipos de hilos, Attraction y Visitor, que haga cumplir
todas estas restricciones. Para simular una situacion real, el proceso principal tendra que crear solo un
hilo de atraccion que entrara en un bucle (infinito) y generara aleatoriamente un numero finito de
hilos de visitantes. 

'''

import threading as th
import time, random

cola = th.Semaphore(10)
viaje = th.Semaphore(0)

mutex = th.Semaphore(1)

coche_esperando = th.Semaphore(0)
pasajeros_saliendo = th.Semaphore(0)

cocheEsperando = False
n_pasajeros = 0

def Attraction():
	global n_pasajeros,cocheEsperando
	
	while(True):
	
		#El tren se bloquea sio no hay pasajeros
		mutex.acquire()
		
		if n_pasajeros < 5:
			cocheEsperando = True
			print("No hay pasajeros para empezar el viaje")
			mutex.release()
			coche_esperando.acquire()
		else:
			mutex.release()	
		print("PREPARENSE PARA EL VIAJE DE SUS VIDAS")
		time.sleep(15)
		print("Salgan del tren por favor")
		
		n_pasajeros_actual = n_pasajeros
		for i in range(n_pasajeros):
			viaje.release()
			
		for i in range(n_pasajeros_actual):
			pasajeros_saliendo.acquire()

		
	
def visitor(iden):
	
	global n_pasajeros,cocheEsperando
	
	
	#Los viajeros entran a la cola, no pueden pasar mas de 5
	cola.acquire() 
	
	mutex.acquire()
	n_pasajeros += 1
	
	#Si el pasajero en entrar es el 5 y el coche esta bloqueado, lo libera
	if(cocheEsperando and n_pasajeros == 5):
		print("Pasajero "+str(iden)+" liberando al coche")
		coche_esperando.release()
	
	
	#Los viajeros han de esperar hasta que la atraccion llegue
	print("Pasajero "+str(iden)+" preparado")
	mutex.release()
	
	viaje.acquire()
	
	mutex.acquire()
	n_pasajeros -= 1
	
	
	print("Pasajero "+str(iden)+" saliendo")
	
	pasajeros_saliendo.release()
	mutex.release()
	
	#Cuando salen de la atraccion dejan que los demas se monten
	cola.release()

coche = th.Thread(target = Attraction)

coche.start()

procesos = []
iden = 0

while(True):
	if iden != 0: #Para no tener que esperar 10 segundos cada vez que ejecute
		time.sleep(10)

	tanda_pasajeros = random.randrange(8)
	
	mutex.acquire() #Mera estetica
	print("Llegan " +str(tanda_pasajeros)+ " pasajeros")
	mutex.release()
	
	
	for i in range(tanda_pasajeros):
		iden += 1
		procesos.append(th.Thread(target = visitor, args = (iden,)))
		procesos[iden-1].start()
	
	
for proceso in procesos:
	proceso.join()
	
cohe.join()
	
