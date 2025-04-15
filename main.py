import tkinter as tk
import time
from threading import Thread

def start_countdown():
    def countdown():
        for i in range(10, 0, -1):
            label.config(text=str(i))
            time.sleep(1)
        label.config(text="🎉 Happy New Year! 🎉")
    
    Thread(target=countdown).start()

root = tk.Tk()
root.title("Countdown")

label = tk.Label(root, text="Click to Start Countdown", font=("Helvetica", 32), fg="black")
label.pack(pady=40)

button = tk.Button(root, text="Start", font=("Helvetica", 20), command=start_countdown)
button.pack(pady=20)

root.mainloop()



