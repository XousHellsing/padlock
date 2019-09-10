import os
import time
import random
vec=[]
lock=0
for x in range(0,10):
	vec.append(x+1) 
print(vec)
def sumaF(lock):
	os.system("cls")
	print("Suma de vector")
	a=0
	if lock==0:
		time.sleep(1)
		for x in range(0,10):
			a=a+vec[x]
			print(a)
	else:
		print("ocupado s")
def multiF(lock):
	os.system("cls")
	print("Multiplicacion de vector")
	b=1
	if lock==0:
		time.sleep(4)
		for y in range(0,10):
			b=b*vec[y]
		print(b)
	else:
		print("ocupado m")

def padlock(lock):
	lock1=lock
	x=random.randrange(0,1000)
	pad=""
	print("Execute? y/n...")
	pad=input()
	while pad=="y":
		if random.randrange(0,1000)<=500:
			sumaF(lock)
		if random.randrange(0,1000)>=500:
			multiF(lock)
		print("Want repeat? y/n...")
		pad=input()
	else:
		print("bye")





