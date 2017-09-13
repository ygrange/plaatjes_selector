#!/usr/bin/env python2.7
#############################################################################
#  Copyright 2017 ASTRON (Netherlands Institute for Radio Astronomy)
#  P.O. Box 2, 7990 AA Dwingeloo, The Netherlands
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#############################################################################

import Tkinter as Tk
import os
import errno

from PIL import ImageTk, Image

class GUI(object):
    def __init__(self, bronpad, bewaardoelpad):
        self.bronpad = bronpad
        self.bewaardoelpad = bewaardoelpad
        self.bestandslijst = os.listdir(bronpad)
        self.plaatje = None
        try:
            os.makedirs(bewaardoelpad)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        self.scherm = Tk.Tk()
        self.vul_scherm()
        self.volgende()
        self.scherm.mainloop()

    def vul_scherm(self):
        self.scherm.configure(background='lightblue')
        self.scherm.title("Image mover")
        self.scherm.geometry("1000x800")
        self.plaatje_container = Tk.Label(self.scherm)
        self.plaatje_container.pack(side = "top", fill = "none", expand = "yes")
        self.knop_bewaar = Tk.Button(self.scherm, text = 'bewaar', command = self.bewaar)
        self.knop_bewaar_niet = Tk.Button(self.scherm, text = 'bewaar niet', command = self.bewaar_niet)
        self.knop_bewaar.pack(side=Tk.LEFT)
        self.knop_bewaar_niet.pack(side=Tk.RIGHT)
        self.scherm.bind("j", self.bewaar)
        self.scherm.bind("n", self.bewaar_niet)


    def volgende(self):
        try:
            plaatje_bestand = self.bestandslijst.pop(0)
        except IndexError:
            self.plaatje_container.img=''
            self.plaatje_container.configure(image='')
            self.plaatje_container.configure(text="Klaar hoor!")
            self.knop_bewaar.configure(state=Tk.DISABLED)
            self.knop_bewaar_niet.configure(state=Tk.DISABLED)
            self.scherm.unbind("j")
            self.scherm.unbind("n")
            return
        plaatje_pad = os.path.join(self.bronpad, plaatje_bestand)
        self.plaatje = os.path.abspath(plaatje_pad)
        plaatje_imob = Image.open(self.plaatje)
        plaatje_imob.thumbnail((800,700), Image.ANTIALIAS)
        plaatje_object = ImageTk.PhotoImage(plaatje_imob)
        self.plaatje_container.img = plaatje_object
        self.plaatje_container.configure(image=plaatje_object)
        
        self.scherm.mainloop()


    def bewaar(self, event=None):
        bestandsnaam = os.path.basename(self.plaatje)
        doelbestand = os.path.join(self.bewaardoelpad, bestandsnaam)
        print "Bewaar %s"%self.plaatje
        os.rename(self.plaatje, doelbestand)
        self.volgende()

    def bewaar_niet(self, event=None):
        print "Bewaar %s niet"%self.plaatje
        self.volgende()


bronpad = "./test_fotos"
bewaardoelpad = "./test_fotos_bewaar"

run_gui = GUI(bronpad, bewaardoelpad)

