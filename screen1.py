from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


import _thread
from tkinter import messagebox as mb

import db
import restclient


class Clockify:
    def __init__(self,master):
        start_button=''
        # master = Tk()
        self.view=False
        self.master=master
        self.master.title("Handling Network Easy")
        self.master.geometry("450x500")

        """Block for pinging starts from here"""
        ttk.Label(self.master, text = "Network Automation tool",
                  background = 'grey', foreground ="white",
                  font = ("Times New Roman", 15)).grid(row = 0, column = 1)

        ttk.Label(self.master, text="Select Device to Ping:",
                  font=("Times New Roman", 10)).grid(column=0,
                                                     row=5, padx=10, pady=30)

        n = StringVar(self.master)
        device_choosen = ttk.Combobox(self.master, width=27, textvariable=n)
        device_list=db.get_device_list()
        print(device_list)
        device_choosen['values'] = tuple(device_list)
        device_choosen.grid(column=1, row=5)
        device_choosen.current(0)

        def pingCombo():
            sel = device_choosen.get()
            print("This is printCombo section: ",sel)
            result=restclient.pinging(sel)
            pingMsg(result)

        ping_button = Button(self.master, text="ping", command=pingCombo)
        ping_button.grid(column=2, row=5)

        def pingMsg(status):
            mb.showinfo(title="Status",message=status)
        """Block for pinging ends here"""




        """Block for startup starts here"""

        ttk.Label(self.master, text="Select Device to start:",
                  font=("Times New Roman", 10)).grid(column=0,
                                                     row=7, padx=10, pady=30)

        n = StringVar(self.master)
        start_device_choosen = ttk.Combobox(self.master, width=27, textvariable=n)
        start_device_list = db.get_device_list()
        print(start_device_list)
        start_device_choosen['values'] = tuple(start_device_list)
        start_device_choosen.grid(column=1, row=7)
        start_device_choosen.current(0)

        def startCombo():
            sel = start_device_choosen.get()
            print("This is printCombo section: ",sel)
            result=restclient.startup(sel)
            pingMsg(result)

        start_button = Button(self.master, text="Start", command=startCombo)
        start_button.grid(column=2, row=7)



mainWindow = Tk()
app = Clockify(mainWindow)
mainWindow.mainloop()