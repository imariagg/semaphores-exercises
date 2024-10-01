#COLA

import threading, time, random, sys

num_follower = 4
num_leader = 4

lider = threading.Semaphore(0)
seguidor = threading.Semaphore(0)


def follower(iden):
	print("Follower"+str(iden)+" esperando")
	lider.release()
	seguidor.acquire()
	print("Follower"+str(iden)+" entrando")
			
def leader(iden):
	print("Leader"+str(iden)+" esperando")
	seguidor.release()
	lider.acquire()
	print("Leader"+str(iden)+" entrando")
			
		
		
procesos = []
iden = 0;

for i in range(num_follower):	
	iden += 1
	procesos.append(threading.Thread(name = "follower"+str(iden),target=follower, args = (iden,)))

iden = 0

for i in range(num_leader):	
	iden += 1
	procesos.append(threading.Thread(name = "leader"+str(iden),target=leader , args = (iden,)))


for proceso in procesos:
	proceso.start()
	
for proceso in procesos:
	proceso.join()

