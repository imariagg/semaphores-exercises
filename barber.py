#BARBERO
'''
Este problema modela el acceso a un recurso limitado por parte de varios procesos, de manera que la cola de espera tiene
un tamanio fijo. El problema se plantea en una peluqueria de la siguiente manera:

En la peluqueria hay un barbero y n sillas para que los clientes esperen. El barbero tiene mucho suenio:
cuando no hay clientes esperando, se va a dormir inmediatamente. El primer cliente que llega tiene que
despertar al barbero para que le corte el pelo. Si un cliente llega cuando el barbero esta ocupado, debe esperar en una silla
hasta que llegue su turno. Si todas las sillas estan ocupadas, el cliente se va.

La solucion es muy sencilla. Se asocia un semaforo al barbero y otro a los clientes.
Ademas, se define una variable entera, waiting, que almacena el numero de clientes en espera
'''

import threading, time, random

n_clientes=7
n_barbero=1
n_sillas=3

c_clientes=0
c_sillas=0


sillas=threading.Semaphore(n_sillas)
durmiendo=threading.Semaphore(0)
mutex1=threading.Semaphore(1)
mutex2=threading.Semaphore(1)
mutex3=threading.Semaphore(0)
ocupado=threading.Semaphore(1)


def clientes(id):

	global c_clientes, c_sillas
	
	
	sillas.acquire()
	
	mutex1.acquire()
	c_clientes+=1
	print('Soy cliente '+str(id)+' y estoy esperando a entrar')
	
	if c_cliente==1:
		durmiendo.release()
		
	mutex1.release()
	
	mutex2.acquire()
	c_sillas+=1
	mutex2.release()
	
	
	
	mutex3.acquire()
	
	ocupado.acquire()
	
	sillas.release()
	
	


def barbero(id):

	global c_clientes, c_sillas


	mutex1.acquire()
	
	if c_clientes==0:
		mutex1.release()
		durmiendo.acquire()
	
	else:
		mutex3.release()
		ocupado.release()	
		
		print('Soy el barbero y voy a pelar ')
		time.sleep(random.randrange(1,3))
		
		mutex2.acquire()
		c_sillas-=1
		mutex2.release()
		
		
		c_clientes-=1	
		mutex1.release()
		
		
	
	

pool=[]

for i in range(1, n_clientes+1):
	pool.append(threading.Thread(name='clientes '+str(i), target=clientes, args=(i,)))
	

for i in range(1, n_barbero+1):
	pool.append(threading.Thread(name='barbero '+str(i), target=barbero, args=(i,)))
	
random.shuffle(pool)


for h in pool:
	h.start()
	
for h in pool:
	h.join()

