#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import time
import threading

def fun_timer():
    print('Hello, world!')
    global timer
    timer = threading.Timer(.5, fun_timer)
    timer.start()

if __name__ == "__main__":
    root = Tk()

    li = ['C', 'Python', 'php', 'html', 'SQL', 'java']
    movie = ['CSS', 'jQuery', 'Bootstrap']
    listb = Listbox(root)
    listb2 = Listbox(root)
    lableb = Label(root, text="2018年10月14日 00:00:15", font = ("Arial, 20"))


    for item in movie:
        listb2.insert(0, item)

    for item in li:
        listb.insert(0, item)

    lableb.grid()
    time.sleep(2)
    lableb = Label(root, text=1, font = ("Arial, 20"))
    lableb.grid()
    listb.grid()
    listb2.grid()
    root.mainloop()

    timer = threading.Timer(1, fun_timer)
    timer.start()

    time.sleep(15)
    timer.cancel()