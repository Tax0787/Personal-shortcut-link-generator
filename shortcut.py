import tkinter as tk

# The global variables
title = ""
name = ""
url = ""

# The Main Window
window = tk.Tk()
window.geometry("800x150")
window.title('HTML Shortcut generator')

# Title Label
title_label = tk.Label(window, text = 'Shortcut title')
title_label.pack()

# Title Input
title_inp = tk.Entry(window)
title_inp.pack()

# Name Label
name_label = tk.Label(window, text = 'Name of the shortcut')
name_label.pack()

# Name Input
name_inp = tk.Entry(window)
name_inp.pack()

# URL Label
url_label = tk.Label(window, text = 'URL')
url_label.pack()

# URL Input
url_inp = tk.Entry(window)
url_inp.pack()

# Define the third button click listener
def url_btn_listener():
    global url
    url = url_inp.get()
    global title
    title = title_inp.get()
    global name
    name = name_inp.get()

    with open(name,'w') as f:
        f.write('<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>{}</title></head><body><meta http-equiv="refresh" content="0;url={}"></body>'.format(title, url))

# The third button
url_btn = tk.Button(window, text = '확인',command = url_btn_listener)
url_btn.pack()

# Finish!
window.mainloop()