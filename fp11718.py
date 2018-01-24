#Jhamni Young-Shinnick
#January 17th,2018
#Planner
#fp11718.py
import Tkinter as tk
import time as Time
root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=300, borderwidth=0, highlightthickness=0, bg="white")
canvas.grid() #Fills background white and creates a larger Canvas
left = canvas.create_line(500, 300, 500, 0, fill='green', tags=('left'))
time = Time.gmtime(Time.time())
timeObject = canvas.create_text(500,250,text=str(time),fill='#000000')

def tick():
    global time, timeObject
    time = Time.gmtime(Time.time())
    canvas.itemconfig(timeObject, text=str(time))
    canvas.after(1,tick)

tick()


from datetime import date
today = str(date.today())
canvas.create_text(50,25,text=str(today),fill='#000000')
root.mainloop()# Event loop