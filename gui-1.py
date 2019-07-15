from tkinter import *
import tkinter.messagebox as messagebox

class apption(Frame):
       def __init__(self,master=None):
              Frame.__init__(self,master)
              self.pack()
              self.createWidgets()

       def createWidgets(self):
              self.nameInput = Entry(self)
              self.nameInput.pack()
              self.alertButton = Button(self,text='hello',command=self.hello)
              self.alertButton.pack()

       def hello(self):
              name = self.nameInput.get() or 'World'
              messagebox.showinfo('Message','hello, %s' %name)

app = apption()

app.master.title('hello world')

app.mainloop()
