#make a google meet attending bot

import pyautogui
import time
import webbrowser
import pyperclip

code = input('Enter the code: ')
pyautogui.FAILSAFE = False
link = 'https://meet.google.com/' + code + "?authuser=0" #change authuser to 1 if you want to join as the secondary account... change to 0 if using primary account

def join(link):
    webbrowser.open(link)
    time.sleep(5)
    pyautogui.click(x=551, y=846)
    pyautogui.click(x=656, y=842)
    pyautogui.click(x=1413, y=599)
    time.sleep(5)
    pyperclip.copy('PRESENT 10k')
    pyautogui.click(x=1697, y=930)
    pyautogui.click(x=1447, y=825)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(x=1822, y=805)
    pyautogui.click(x=1842, y=193)
    time.sleep(10)
    pyautogui.click(x=1157, y=931)

if __name__ == '__main__':
    join(link)