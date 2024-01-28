import pyautogui
import time

#definir tempo entre cada execução da automação
pyautogui.PAUSE = 0.3

#sequencia de passos
pyautogui.press("win")
pyautogui.write("firefox.exe")
pyautogui.press("enter")
pyautogui.write("https://mail.google.com/")
pyautogui.press("enter")

#esperar a pagina da web carregar
time.sleep(5)

pyautogui.click(x=54, y=204)
pyautogui.click(x=1334, y=512)
pyautogui.write("thisemaildoesnotexist@gmail.com")
pyautogui.press("tab")
pyautogui.write("Olhe só a minha automação de e-mail!")
pyautogui.press("tab")
pyautogui.write("Disponível em: https://github.com/guilhermerek/RPA")
pyautogui.click(x=1299, y=1006) #ao clicar irá enviar o e-mail quase instantaneamente, cuidado!

exit