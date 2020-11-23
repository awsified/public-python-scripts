import webbrowser, sys, pyperclip # import using pip if necessary
if len(sys.argv) > 1:
    # Get address from command line. (>>file.py type out address like this)
    address = ' '.join(sys.argv[1:])
else: # OR ALTERNATIVELY...
    # Get address from clipboard.
    address = pyperclip.paste()

c = webbrowser.get('C:/Program Files/Mozilla Firefox/firefox.exe %s') 
c.open('https://www.google.com/maps/place/' + address)