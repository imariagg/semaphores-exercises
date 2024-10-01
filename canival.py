#CANIVAL

import threading, time, random

'''
Una tribu de salvajes come en comunidad de una gran olla que
puede contener M porciones de misionero guisado1
. Cuando un salvaje quiere
comer, se sirve de la olla, a menos que este vacia. Si la olla esta
Si la olla esta vacia, el salvaje despierta al cocinero y espera a que este
haya rellenado la olla

'''

n_salvajes=6
n_cocinero=1

n_porciones_totales=4
c_porciones=0

mutex=threading.Semaphore(1)
vacia=threading.Semaphore(0)
llena=threading.Semaphore(0)



def savage(id):

	global c_porciones, n_porciones_totales
	
	while True:
	
		time.sleep(random.randrange(1,3))
		mutex.acquire()

		if c_porciones==0:
			print('Soy salvaje ' +str(id)+' y no hay comida suficiente, despierto al cocinero')
			vacia.release()
			llena.acquire()
			

		c_porciones-=1

		print('Soy salvaje ' +str(id)+' y me he servido de la olla')
		time.sleep(random.randrange(1,3))
		
		mutex.release()
	
	
	
def cook(id):

	global c_porciones, n_porciones_totales
	
	while True:
		vacia.acquire()
		
		c_porciones=n_porciones_totales
		print('Soy cocinero ' +str(id)+ ' y he hecho '+str( n_porciones_totales)+ ' porciones')
		time.sleep(random.randrange(1,3))
		
		llena.release()
	
	
lista=[]

for i in range(1, n_salvajes+1):
	
	lista.append(threading.Thread(name='savagegeno '+str(i),target=savage, args=(i,)))
	
	
for i in range(1, n_cocinero+1):
	
	lista.append(threading.Thread(name='cookgeno '+str(i),target=cook, args=(i,)))
	
random.shuffle(lista)

for h in lista:
	h.start()
	
for h in lista:
	h.join()
