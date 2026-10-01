import keyboard
import time
import pydirectinput


print("your auto clicker is ready")
print("press s to start and t to stop")


while True:
    if keyboard.is_pressed("s"):
        pydirectinput.click()
    if keyboard.is_pressed("t"):
        break

       