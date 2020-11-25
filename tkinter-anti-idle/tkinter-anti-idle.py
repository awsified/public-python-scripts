import tkinter as tk,pyautogui,time # This is the prefered way to call tkinter, don't use wildcards. 

my_ui_window = tk.Tk() # TK
my_ui_window.title('Radio Button Example')
v = tk.IntVar()
v.set(1)  # initializing the choice

on_or_off = [
    ("Enabled"),
    ("Disabled")
]

def every_20_seconds():
    if v.get() == 0:
        pyautogui.click()
    my_ui_window.after(20000, every_20_seconds)


for val, i in enumerate(on_or_off):
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