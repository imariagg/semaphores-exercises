#PRODUCER_COMSUMER

'''
Este problema tambien se conoce como el problema del almacenamiento limitado. Hay dos tipos de procesos, uno que produce informacion y otro que la consume. Ambos se comunican a traves de un
buffer de capacidad limitada. Hay tres condiciones de competencia que deben estar bajo control:
1. El acceso concurrente al buffer. Es necesario que el productor no escriba un elemento que
el consumidor este leyendo, y viceversa.
2. El buffer esta completo. Si el buffer esta completo, el productor debe esperar a que el consumidor haya
leido al menos un elemento para poder seguir almacenando informacion en el buffer.
3. El buffer esta vacio. En este caso el consumidor debe esperar a que el productor escriba nueva
informacion. 


1 producer 1 consumer
1 producer x consumer
x producer 1 consumer
x producer x consumer

La version mas tocha es hacer un buffer que este hecho ya y escrito y que vaya accediendo a cada sitio
'''


import threading, time, random

n_producers=3
n_consumers=6

c_producers=0
c_consumers=0

it_c=0
it_p=0

buff=[0,0,0,0,0]
tam_buffer=len(buff)

mutex=threading.Semaphore(1)
vacio=threading.Semaphore(tam_buffer)
lleno=threading.Semaphore(0)

def producer(id):


	global c_producers, c_consumers, it_p, buff
	
	while True:
		
		
		vacio.acquire()
		mutex.acquire()
		
		print('Soy productor '+str(id)+ ' y estoy produciendo')
		
		c=buff[it_p]
		c+=1
		buff[it_p]=c
		it_p+=1
		
		if it_p==5:
			it_p=0
		
		time.sleep(random.randrange(1,3))
		print('Buffer= '+str(buff))	
		
		mutex.release()
		lleno.release()
		
		
		

def consumer(id):

	global c_consumers, c_producers, it_c, buff
	
	while True:	
		
		
		lleno.acquire()
		mutex.acquire()
		print('Soy consumidor '+str(id)+ ' y estoy consumiendo')
		
		c=buff[it_c]
		c+=1
		buff[it_c]=c
		it_c+=1
		
		if it_c==5:
			it_c=0
			
		time.sleep(random.randrange(1,3))
		print('Buffer= '+str(buff))	
			
		mutex.release()
		vacio.release()		
		
	
		




pool=[]

for i in range(1,n_producers+1):

	pool.append(threading.Thread(name='Productor ', target=producer, args=(i,)))


for i in range(1,n_consumers+1):

	pool.append(threading.Thread(name='Consumidor '+str(id), target=consumer, args=(i,)))
	
	
	
for h in pool:

	h.start()
	
for h in pool:

	h.join()
