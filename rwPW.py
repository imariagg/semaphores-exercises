#READ_WRITER_PW

'''
Este problema ocurre muy a menudo en todas las aplicaciones relacionadas con las bases de datos. Se trata de gestionar
el acceso concurrente a la informacion, en el que hay dos tipos de procesos: lectores y escritores.


Lectores pueden acceder concurrentemente ya que no modifican la informacion, pero cuando un
escritor hace un acceso no puede haber otro proceso accediendo concurrentemente, lector o escritor.

Las soluciones deben basarse siempre en una precedencia de los lectores sobre los escritores o viceversa. 

La idea de la solucion es bastante simple. Para el acceso a la informacion se debe utilizar un semaforo, db. Cualquier escritor
que intente acceder debe ejecutar wait (db), con esto garantizamos el acceso exclusivo de los
escritores.
Para que los lectores puedan acceder de forma concurrente, solo el primer lector ejecutara wait(db), el resto
acceden directamente. El ultimo lector que abandona la base de datos es el que libera el recurso, ejecutando signal(db).
'''

import threading, time, random

n_lectores=4
n_escritores=3

c_lectores_bloqueados=0
c_escritores=0
c=0

write=threading.Semaphore(1)
mutex=threading.Semaphore(1)
block=threading.Semaphore(0)
read=threading.Semaphore(1)

def escribir(id):

	global c, c_escritores, c_lectores_bloqueados
	

	
	mutex.acquire()
	
	print('Soy escritor '+str(id)+' y estoy entrando')
	c_escritores+=1	
	
	mutex.release()	
	
	
	
	write.acquire()

	print('Soy escritor '+str(id)+' y estoy escribiendo')
	time.sleep(random.randrange(1,3))
	c+=1
	print('Soy escritor '+str(id)+' y he terminado de escribir')
	
	write.release()
	
	
	mutex.acquire()
	print('Soy escritor '+str(id)+' y estoy saliendo')
	c_escritores-=1
	if c_escritores==0:
		for i in range(c_lectores_bloqueados):
			block.release()
			c_lectores_bloqueados-=1		
	mutex.release()
	
		
		



def leer(id):

	global c, c_escritores, c_lectores_bloqueados


	
	mutex.acquire()
	
	if c_escritores!=0:
		print('Soy lector '+str(id)+' y estoy esperando a leer')
		c_lectores_bloqueados+=1
		mutex.release()
		block.acquire()
		
		
	else:
		mutex.release()

	
	
	print('Soy lector '+str(id)+' y estoy leyendo. C='+str(c))
	time.sleep(random.randrange(1,3))
		
		
		
		


pool=[]

for i in range(1, n_escritores+1):
	pool.append(threading.Thread(name='Escritor '+str(i), target=escribir, args=(i,)))
	

for i in range(1, n_lectores+1):
	pool.append(threading.Thread(name='Lector '+str(i), target=leer, args=(i,)))

random.shuffle(pool)

for h in pool:
	h.start()
	
for h in pool:
	h.join()

'''
import threading, time, random

n_readers=3
n_writers=3

c_writers=0
c_readers=0

c=0

mutex=threading.Semaphore(1)
block=threading.Semaphore(1)
#b=threading.Semaphore(0)

def escribir(id):


	global c_writers,c, c_readers
	
	while True:
	
		
		write.acquire()

		print('Soy escritor '+str(id)+ ' y estoy escribiendo')
		c+=1
		time.sleep(random.randrange(1,3))
		
		write.release()
		

		

def leer(id):

	global c_writers,c, c_readers
	
	while True:	
		
		
		mutex.acquire()
		c_readers+=1
		if c_readers==1:
			write.acquire()

		mutex.release()
		
		
		print('Soy lector '+str(id)+ ' y estoy leyendo. Contador='+str(c))
		time.sleep(random.randrange(1,3))	
		
			
		mutex.acquire()
		c_readers-=1
		if c_readers==0:
			write.release()
		mutex.release()
		
		
		
		
		

pool=[]

for i in range(1,n_writers+1):

	pool.append(threading.Thread(name='Escritor '+str(i), target=escribir, args=(i,)))


for i in range(1,n_readers+1):

	pool.append(threading.Thread(name='Lector '+str(i), target=leer, args=(i,)))
	
	
	
for h in pool:

	h.start()
	
for h in pool:

	h.join()
'''
