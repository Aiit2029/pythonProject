import pyautogui

# print(pyautogui.size())
# print(pyautogui.position())

x,y = pyautogui.position()
while True:
    x1,y1 = pyautogui.position()
    if x1 != x or y1 != y:
        print(x1,y1)
        x,y = x1,y1
        print(x,y)


