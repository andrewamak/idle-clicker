import pyautogui
import time
import random

#print(pyautogui.size())

#prints position of mouse

print('clicker(time,x coordinate, y coordiate, randomiztion (0 for off, 1 for on)')

#runs infinitely
#t = frequency(s); x coordinate, y coordinate, r = randomization on or off)
def clicker(t,x,y,r):

    
    
    if r == 0:
        print('Now clicking infinitely every ' + str(t) + ' seconds at location (' + str(x) + "," + str(y) + '). Randomization off.')
        while True:
            
            #how frequent to loop.
            time.sleep(t)
            og_mouse_position = (pyautogui.position())
            

            #position of double click
            pyautogui.click(x,y)
            pyautogui.click(x,y)
            print(pyautogui.position())

            #returns mouse to original position
            pyautogui.moveTo(og_mouse_position)

            

    elif r == 1:
        print('Now clicking infinitely every ' + str(t) + ' seconds at location (' + str(x) + "," + str(y) + '). Randomization on.')
        while True:
            
            #how frequent to loop.
            #generating small range of seconds for random selection
            s = t - (t/10)
            u = t + (t/10)

            #random.uniform returns a float number between s and u
            time.sleep(random.uniform(s,u))

            og_mouse_position = (pyautogui.position())

            #generating small range of coordinates for random selection
            minusx = x - 5
            minusy = y - 5
            plusx = x + 5
            plusy = y + 5
            
            #position of double click
            pyautogui.click(random.randrange(minusx,plusx),random.randrange(minusy,plusy))
            
            print(pyautogui.position())

            #returns mouse to original position
            pyautogui.moveTo(og_mouse_position)
            


