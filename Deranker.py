import pyautogui #Allows for program to input
import random #To avoid ban, or to an extent
import time #As Time before being kicked for idle is 30, and a new action is required or idle ban occurs

inputs = ['q','e','a','d','t', 'm'] #Change Boost and Jump to T and M, Python is weird with mouse buttons ig
i = 0 #For looper
ballviewed = True

looper = True

while looper == True:
    time_delay1 = random.randint(1,8) #First delay, so selected button pressed.. it will be held for between 1 and 8 seconds
    time_delay2 = random.randint(8,10) # it will wait 8 to 10 seconds before selecting another button to press, lower seems too frequent and higher risks idle ban

    time.sleep(time_delay2) #Waits before choosing another button

    buttontobepressed = random.choice(inputs) #Selects another button
    pyautogui.press('Tab') #Check Score and chat
    pyautogui.rightClick() 
    pyautogui.keyDown('right') 
    pyautogui.keyUp('right')
    pyautogui.keyDown('w')
    pyautogui.keyDown(buttontobepressed)
    time.sleep(time_delay1)
    pyautogui.keyUp(buttontobepressed)
    pyautogui.keyUp('w')
    i = i + 1 #Counter goes up, this counter is shown as part of banner
    
    print(
            f"""\n\n\n\n\n                                    
    ██████╗ ███████╗██████╗  █████╗ ███╗   ██╗██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝██╔════╝██╔══██╗
    ██║  ██║█████╗  ██████╔╝███████║██╔██╗ ██║█████╔╝ █████╗  ██████╔╝
    ██║  ██║██╔══╝  ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██████╔╝███████╗██║  ██║██║  ██║██║ ╚████║██║  ██╗███████╗██║  ██║
    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                 
    ----------------------------------------------------------------
    {buttontobepressed} pressed for {time_delay1} seconds, waiting for {time_delay2} seconds until next loop..
    Currently {i}





        """)
