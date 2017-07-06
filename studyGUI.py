#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx

class Frame1(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, parent = superior, title = 'Hello World in wxPython')
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1 = wx.TextCtrl(panel, value = 'Hello, World!', size = (200, 180), style = wx.TE_MULTILINE)
        sizer.Add(self.text1, 0, wx.ALIGN_TOP | wx.EXPAND)
        button = wx.Button(panel, label = 'Click Me')
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)
        panel.Layout()
        self.Bind(wx.EVT_BUTTON, self.OnClick, button)
    def OnClick(self, text):
        self.text1.AppendText('\nHello, World!')

class Animal(object):
    def __init__(self, name):
        self.name = name
    def getInfo(self):
        print("This animal's name: %s" %self.name)
    def sound(self):
        print('The sound of this animal gose?')

class Dog(Animal):
    def __init__(self, name, size):
        self.name = name
        self.__size = size

    def getInfo(self):
        print("this dog's name: %s" %self.name)
        print("this dog's size: %s" %self.__size)

class Cat(Animal):
    def sound(self):
        print("The sound of cat goes meow ~")

if __name__ == '__main__':
    word = 'Python'
    print(word[-1])
