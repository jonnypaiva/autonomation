import pyautogui as pygui
import time
import selenium
size_x, size_y = pygui.size()
print(f"Tamanho da Tela", size_x, size_y)
time.sleep(3)
position_x, position_y = pygui.position()
print(f"mouse position: X > {position_x} and Y > {position_y}")