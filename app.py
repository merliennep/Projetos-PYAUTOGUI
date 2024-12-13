import pyautogui

#posição algo - use o mouseinfo
#fazer algo com essas posição
#https://www.crazygames.com/game/doge-miner-2

pyautogui.moveTo(660,883,duration=2)
pyautogui.move(0,934,duration=1)
pyautogui.click(duration=1)
pyautogui.write('https://www.crazygames.com/game/doge-miner-2', interval=0.2)
pyautogui.press('enter')
pyautogui.move(-87,-361,duration=1)
pyautogui.click(duration=2)
pyautogui.move(0,-128,duration=3)
pyautogui.click(duration=1)
pyautogui.move(-141,0,duration=3)
pyautogui.click(clicks=100, interval=0.25)



