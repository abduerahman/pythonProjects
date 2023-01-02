import psutil
from tkinter import *

window = Tk()
battery = psutil.sensors_battery()
  
if battery.percent >= 99:
    window.eval('tk::PlaceWindow . center')
    window.geometry("600x250")
    window.title('Battry Charged')
    label = Label(text="The Batary Charged Remove the charger", padx=100,pady=80,font=('Helvetica bold',15)).grid(column=5,row=1)
    window.mainloop()