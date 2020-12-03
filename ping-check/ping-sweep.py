import subprocess # This opens processes

import tkinter as tk # Used for generating windows
from tkinter import simpledialog

WINDOW = tk.Tk() # Makes window variable

WINDOW.withdraw() # Withdraw method disappears window after input

# the input dialog
host = simpledialog.askstring(title="Computer Name",
                                  prompt="Input computer name: ")

search_value = "TTL=" # TTL= is a nice unique string to search for that should only appear if we successfully 
ping_requests ='1' # Set threshhold of how many times to ping. Too high and your program takes too long. Too low and one random timeout and the computer is accidentally declared offline. Either set it to 1 or 2. 2 For reliability but 1 should work fine.

arg = ["ping",host,"-n",ping_requests,"-4"] # list of our parameters

ping = subprocess.Popen(
    arg,
    stdout = subprocess.PIPE, 
    stderr = subprocess.PIPE
    # Makes ping variable representing our subprocess call. Stdout and Stderr are output from the command in byte type representing the output of the process as well as if it generates an error. We then take the output and convert byte to string and search it for signs of a successful ping. 
)

machine_status = 'Offline'
out, error = ping.communicate()

out = out.decode("utf-8") #convert string
print(out)

# Search string looking for "TTL=". Returns -1 if not found and the index element of the first letter if found. So we make a conditional statement asking if the return is equal to -1 or not.
if out.find(search_value) != -1: 
    machine_status = 'Online'
print(f'Current Status for {host}: {machine_status}')