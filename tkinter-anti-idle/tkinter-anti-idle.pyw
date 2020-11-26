import tkinter as tk # This is the prefered way to call tkinter, don't use wildcards. 
import pyautogui # This allows mouse stuff
import time # This allows sleep commands

my_ui_window = tk.Tk() # make tk.Tk() into just a single object.
my_ui_window.title('Anti-Idle 1.0')
v = tk.IntVar() # This becomes the index of sorts for our radio elements.
v.set(1)  # initializing radio button to off

on_or_off = [ # Creates an array to represent the radio buttons needed.
    ("Enabled"),
    ("Disabled")
]

def every_20_seconds(): # Calls this function which clicks if the radio button is set to index 0. It then tells my_ui_window to wait 20 seconds using the .after method before calling itself again. In the meantime, it gives control back to the mainloop() which is always searching for an event change on the UI.
    if v.get() == 0:
        pyautogui.click()
    my_ui_window.after(20000, every_20_seconds)


for val, i in enumerate(on_or_off): # This builds the UI for us.
    tk.Radiobutton(my_ui_window, 
                  text=i,
                  borderwidth = 2,
                  indicatoron= 0,
                  width = 20,
                  padx = 50, 
                  variable=v, 
                  value=val).pack(anchor=tk.W)


every_20_seconds()
my_ui_window.mainloop()