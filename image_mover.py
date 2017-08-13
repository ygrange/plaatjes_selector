#!/usr/bin/env python2.7

import Tkinter as Tk

from PIL import ImageTk, Image

def bewaar(aa):
    print "Bewaar %s"%aa

def bewaar_niet(aa):
    print "Bewaar %s niet"%aa


gui_window = Tk.Tk()
gui_window.configure(background='lightblue')
gui_window.title("Image mover")
gui_window.geometry("1200x600")

path = "test_fotos/DSC01299.jpg"

image = ImageTk.PhotoImage(Image.open(path))
image_content = Tk.Label(gui_window, image = image)
image_content.pack(side = "bottom", fill = "none", expand = "yes")

button_bewaar = Tk.Button(gui_window, text = 'bewaar', command = bewaar)
button_bewaar_niet = Tk.Button(gui_window, text = 'bewaar niet', command = bewaar_niet)

gui_window.mainloop()
