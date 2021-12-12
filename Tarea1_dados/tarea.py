import sys
import random
import matplotlib.pyplot as plot

sumas=[]

for i in range(0,int(sys.argv[1])):
    dado1=random.randint(1,7)
    dado2=random.randint(1,7)
    sumas.append(dado1+dado2)    
# print(sumas)
#intervalos=range(min(sumas),max(sumas)+2)
intervalos=range(2,12+2)#Le sumo mas dos caso contrario no sale en la grafica

plot.hist(x=sumas,bins=intervalos,color="red", rwidth=0.85)
plot.title('Histograma resultados')
plot.xlabel('numeros')
plot.ylabel('Frecuencia')
plot.xticks(intervalos)

plot.show() #dibujamos el histograma
#print("Dados = ",dado1,"dato 2= ",dado2)