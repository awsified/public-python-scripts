## This script is designed for Windows only


import tkinter
from tkinter import ttk
import subprocess


def check_if_ready(ping):
    
    if ping.poll() is None: # ping process still running = true
        root.after(200, check_if_ready,ping)
    else:
        out = ping.stdout.read().decode("utf-8")
        if "TTL=" in out:
            machine_status = 'Online'
        else:
            machine_status = 'Offline'
        status_label['text'] = f"Machine Status: {machine_status}"


def start_doing_slow_stuff():
     
    ping_requests ='1' 
    arg = ["ping",hostname.get(),"-n",ping_requests,"-4"]

    ping = subprocess.Popen(
            arg,
            stdout = subprocess.PIPE, 
        )
    
    root.after(200, check_if_ready,ping)


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

ttk.Button(big_frame, text="Start", command=start_doing_slow_stuff).pack()
status_label = ttk.Label(big_frame,text='Machine Status: N/A')
status_label.pack()
hostname = ttk.Entry(big_frame)
hostname.pack()
root.mainloop()