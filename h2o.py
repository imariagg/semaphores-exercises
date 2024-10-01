#H2O

import threading, time, random

'''
Hay dos tipos de hilos, oxigeno e hidrogeno. Para ensamblar estos hilos en moleculas de agua, tenemos que crear una barrera que hace que cada hilo espere hasta que una molecula completa este lista para proceder.
Cuando cada hilo pasa la barrera, debe invocar el enlace. Hay que garantizar
que todos los hilos de una molecula invoquen la union antes de que lo haga cualquiera de los hilos
de la siguiente molecula lo haga.
En otras palabras:
- Si un hilo de oxigeno llega a la barrera cuando no hay hilos de hidrogeno
presente, tiene que esperar a dos hilos de hidrogeno.
- Si un hilo de hidrogeno llega a la barrera cuando no hay otros hilos
presente, tiene que esperar a un hilo de oxigeno y a otro de hidrogeno.
No tenemos que preocuparnos de emparejar los hilos explicitamente; es decir los hilos no saben necesariamente con que otros hilos estan emparejados
con los que estan emparejados. La clave esta en que los hilos pasan la barrera en conjuntos completos; asi, si
Si examinamos la secuencia de hilos que invocan a Bond y los dividimos en grupos
de tres, cada grupo deberia contener un hilo de oxigeno y dos de hidrogeno.
Acertijo: Escribe un codigo de sincronizacion para las moleculas de oxigeno e hidrogeno que
cumpla con estas restricciones.


'''


n_hidrogeno=6
n_oxigeno=3

c_hidrogeno=0
c_oxigeno=0

mutex=threading.Semaphore(1)
mutexAux=threading.Semaphore(1)
barrera=threading.Semaphore(3)
colaOxi=threading.Semaphore(0)
colaHidro=threading.Semaphore(0)










def hidro(id):

	global c_hidrogeno, c_oxigeno
	
	mutex.acquire()
	c_hidrogeno+=1
	
	#print('Soy hidrogeno ' +str(id)+ ' y he entrado en la task')
	
	if c_hidrogeno>=2 and c_oxigeno>=1:
		#print('Se cumple 2H y 1o')
		colaHidro.release()
		colaHidro.release()
		c_hidrogeno-=2
		colaOxi.release()
		c_oxigeno-=1
	
	
	else:
		mutex.release()
	
	
	colaHidro.acquire()
	barrera.acquire()
	
	
	print('Soy hidrogeno ' +str(id)+ ' y voy a formar h20')
	time.sleep(random.randrange(1,3))
	
	
	#barrera.release()
	mutex.release()
	

	
	
	
	
	
	
def oxi(id):

	global c_hidrogeno, c_oxigeno
	

	mutex.acquire()
	c_oxigeno+=1
	
	#print('Soy oxigeno ' +str(id)+ ' y he entrado en la task')
	
	
	if c_hidrogeno>=2:
		colaHidro.release()
		colaHidro.release()
		c_hidrogeno-=2
		colaOxi.release()
		c_oxigeno-=1
	
	else:
		mutex.release()
		
		
	colaOxi.acquire()
	
	barrera.acquire()
	
	
	print('Soy oxigeno ' +str(id)+ ' y voy a formar h20')
	time.sleep(random.randrange(1,3))
	
	
	#barrera.release()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
lista=[]

for i in range(1, n_hidrogeno+1):
	
	lista.append(threading.Thread(name='Hidrogeno '+str(i),target=hidro, args=(i,)))
	
	
for i in range(1, n_oxigeno+1):
	
	lista.append(threading.Thread(name='Oxigeno '+str(i),target=oxi, args=(i,)))
	
random.shuffle(lista)

for h in lista:
	h.start()
	
for h in lista:
	h.join()
