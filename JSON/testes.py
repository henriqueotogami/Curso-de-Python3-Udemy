#Aula de módulos
#Aula 27
#Usando o módulo Time (Built-In) e o Matplotlib (Externo), façaum código que pede que o
#usuário digite uma palavra 5 vezes seguidas.Conte o tempo que ele utiliza para digitar a 
#palavra a cada repetição, e ao final gera-se um gráfico com os tempos.
#%%
import time as t
import matplotlib.pyplot as plt

tempos = []
vezes = []
vez = 1 

print("Este programa marcará o tempo gasto para digitar a palavra PROGRAMAÇÃO. Você terá que digitá-la.")
print("Aperte enter para começar.")

while vez<= 5:
    inicio = time.clock()
    input("Digite a palavra: ")
    fim = time.clock()
    tempo = round(fim-inicio, 2)
    tempos.append(tempo)
    vezes.append(vez)
    vez += 1

legenda = ["1ª vez, 2ª vez, 3ª vez, 4ª vez, 5ª vez. "]
plt.xticks(vezes,legenda)
plt.plot(vezes,tempos)
plt.show()

# %%
