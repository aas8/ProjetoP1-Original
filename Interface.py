# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:58:44 2018

@author: aas8
"""

import tkinter as tk

janela = tk.Tk()

frame = tk.Frame(janela)
frame.pack()
buttonOK = tk.Button(frame, text = "OK")
buttonOK.pack()