#Jhamni Young-Shinnick
#January 17th,2018
#Planner
#fp11718.py
import Tkinter as tk
import time as Time
root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=300, borderwidth=0, highlightthickness=0, bg="white")
canvas.grid() #Fills background white and creates a larger Canvas

time = Time.gmtime(Time.time())
timeObject = canvas.create_text(500,250,text=str(time),fill='#000000')

def tick():
    global time, timeObject
    time = Time.gmtime(Time.time())
    canvas.itemconfig(timeObject, text=str(time))
    canvas.after(1,tick)

tick()

root.mainloop()# Event loop