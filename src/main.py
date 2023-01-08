import pyautogui as pag

def RickRoll():
    pag.hotkey('win','r')
    pag.write("www.youtube.com/watch?v=dQw4w9WgXcQ")
    pag.press('enter')
    pag.press('tab', presses=2, interval=1.25)
    pag.press("enter")
    pag.press('volumeup', presses=50)

def main():
    RickRoll()
 
if __name__ == "__main__":
    main()