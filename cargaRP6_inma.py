'''
Carga 1 v2
Moneda: Monero
Algoritmo: cryptonight
Tiempo minando: 300, 600
Tiempo dormido: 60
Threads: variables de 1 a 4
Ejecucion paralela (F=apagado, V=encendido):

Nº3	Nº1	Nº5	Nº6	Nº2	Nº4
F	V	F	F	V	F
F	V	F	F	V	V
F	V	F	V	V	F
F	V	F	V	V	V
F	V	V	F	V	F
F	V	V	F	V	V
F	V	V	V	V	F
F	V	V	V	V	V
V	V	F	F	V	F
V	V	F	F	V	V
V	V	F	V	V	F
V	V	F	V	V	V
V	V	V	F	V	F
V	V	V	F	V	V
V	V	V	V	V	F
V	V	V	V	V	V

Tiempo total = 4.8 + 2 = 6.8 horas
'''
import time
import os

def carga():
	for threads in range(1,5):
		minerd = "sudo ./minerd -a cryptonight -o stratum+tcp://xmr.pool.minergate.com:45700 -u i.mmagallon@alumnos.upm.es -p X -t " + str(threads) + " -B"
		os.system(minerd)
		time.sleep(minando)
		os.system("sudo pkill minerd")
		time.sleep(dormido)

i, j = 0, 0
minando = 300
dormido = 60
os.system("sudo cpufreq-set -r -g userspace")
os.system("sudo cpufreq-set -r -f 1.4Ghz")
#time.sleep((minando+dormido)*4)

while(True):
	if(i%16==0):
		time.sleep((minando+dormido)*4)
	elif(i%16==1):
		time.sleep((minando+dormido)*4)
	elif(i%16==2):
		carga()
	elif(i%16==3):
		carga()
	elif(i%16==4):
		time.sleep((minando+dormido)*4)
	elif(i%16==5):
		time.sleep((minando+dormido)*4)
	elif(i%16==6):
		carga()
	elif(i%16==7):
		carga()
	elif(i%16==8):
		time.sleep((minando+dormido)*4)
	elif(i%16==9):
		time.sleep((minando+dormido)*4)
	elif(i%16==10):
		carga()
	elif(i%16==11):
		carga()
	elif(i%16==12):
		time.sleep((minando+dormido)*4)
	elif(i%16==13):
		time.sleep((minando+dormido)*4)
	elif(i%16==14):
		carga()
	elif(i%16==15):
		carga()
		j = j + 1
		if(j>2):
			minando = 600
			dormido = 60
		if(j%3==0):
			os.system("sudo cpufreq-set -r -g userspace")
			os.system("sudo cpufreq-set -r -f 1.4Ghz")
		elif(j%3==1):
			os.system("sudo cpufreq-set -r -g userspace")
			os.system("sudo cpufreq-set -r -f 600Mhz")
		elif(j%3==2):
			os.system("sudo cpufreq-set -r -g ondemand")
	i = i + 1
