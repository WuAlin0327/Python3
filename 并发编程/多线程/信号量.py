from threading import Thread,Semaphore,currentThread
import time,random

sm = Semaphore(3)
def task():
	with sm:
		print('%s is run'%currentThread().getName())
		time.sleep(random.randint(1,3))

if __name__ == '__main__':
	for i in range(10):
		t = Thread(target=task)
		t.start()



