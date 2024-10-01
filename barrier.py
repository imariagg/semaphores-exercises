#BARRERA

import threading, time, random

mutex = threading.Semaphore(1)
barrera = threading.Semaphore(0)

contador_coches = 0

total_coches = 5

def Coche(iden):
	global contador_coches, total_coches

	while True:
	
		time.sleep(random.randrange(2,5))
	
		#rendezVous
		print("---Sale del RendeVous el proceso: "+str(iden))	
		
		mutex.acquire()
		contador_coches += 1	
		print('...Contador antes de la seccion: '+str(contador_coches))
		mutex.release()

		if contador_coches == total_coches:
			barrera.release()

		barrera.acquire()
		barrera.release()
		
			

		print("---Sale de la barrera el proceso: "+str(iden))
		
		#Critical point

		
		mutex.acquire()
		contador_coches-=1
		print('...Contador despues de la seccion: '+str(contador_coches))
		mutex.release()
		
		if contador_coches==0:
			barrera.acquire()
			
			

pool = []

iden = 0

for i in range(total_coches):
	iden += 1
	pool.append(threading.Thread(target=Coche, args = (iden,)))


for proceso in pool:
	proceso.start()
	
for proceso in pool:
	proceso.join()	
