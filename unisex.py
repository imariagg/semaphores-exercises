#UNISEX
import threading, time, random

n_mujeres=4
n_hombres=4

c_mujeres=0
c_hombres=0


mujers=threading.Semaphore(3)
hombrs=threading.Semaphore(3)
mutexmujeres=threading.Semaphore(1)
mutexhombres=threading.Semaphore(1)
mutex=threading.Semaphore(1)
block=threading.Semaphore(1)


def mujer(id):

	global c_mujeres, c_hombres
	
	mutex.acquire()
	mutexmujeres.acquire()

	c_mujeres+=1
	print('Soy mujer '+str(id)+' y estoy esperando a entrar')
	if c_mujeres==1:
		block.acquire()
		
	mutexmujeres.release()
	mutex.release()
	
	
	mujers.acquire()
	
	print('Soy mujer '+str(id)+' y estoy en el banio')
	time.sleep(random.randrange(1,3))
	print('Soy mujer '+str(id)+' y voy a salir del banio')
	
	mujers.release()
	


	mutexmujeres.acquire()

	c_mujeres-=1
	print('Soy mujer '+str(id)+' y ya me voy')
	if c_mujeres==0:
		block.release()
		
	mutexmujeres.release()


def hombre(id):

	global c_mujeres, c_hombres


	mutex.acquire()
	mutexhombres.acquire()

	c_hombres+=1
	print('Soy hombre '+str(id)+' y estoy esperando a entrar')
	if c_hombres==1:
		block.acquire()
		
	mutexhombres.release()
	mutex.release()
	
	hombrs.acquire()
	print('Soy hombre '+str(id)+' y y estoy en el banio')
	time.sleep(random.randrange(1,3))
	print('Soy hombre '+str(id)+' y voy a salir del banio')
	hombrs.release()
	
	
	mutexhombres.acquire()
	
	c_hombres-=1
	print('Soy hombre '+str(id)+' y ya me voy')
	if c_hombres==0:
		block.release()
		
	mutexhombres.release()



pool=[]

for i in range(1, n_mujeres+1):
	pool.append(threading.Thread(name='Mujer '+str(i), target=mujer, args=(i,)))
	

for i in range(1, n_hombres+1):
	pool.append(threading.Thread(name='Hombre '+str(i), target=hombre, args=(i,)))
	
random.shuffle(pool)


for h in pool:
	h.start()
	
for h in pool:
	h.join()

