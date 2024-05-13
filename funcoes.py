import time
#contagem regressiva
def contagem_regressiva(tempo):
    for i in range(tempo, 0, -1):
        print(i)
        time.sleep(1)