import pyautogui
import time
#pega o retorno da posicao atual de x e y do mouse e passa o valor da tupla para as duas variaveis
print('Posicione o MOUSE')
time.sleep(2)
x, y = pyautogui.position()
print ("Posicao atual do mouse:")
print ("x = "+str(x)+" y = "+str(y))