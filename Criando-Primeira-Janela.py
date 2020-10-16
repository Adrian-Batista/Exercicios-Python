Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.msg = Label(self, text='OláMundo')
		self.msg.pack()
		self.pack()

		
>>> app = Application()
>>> 