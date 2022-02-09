from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

def test():
    print("test")
root = Tk()
root.title(" this is a test and its working")

mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)
mainFrame["borderwidth"] = 10
mainFrame['relief'] = 'sunken'


feet = StringVar()
feet = StringVar()
feet_entry = ttk.Entry(mainFrame, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainFrame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainFrame, text="Calculate", command=calculate).grid(
    column=3, row=3, sticky=W)

ttk.Button(mainFrame, text="", command=test).grid(column=3, row=20, sticky=W)
ttk.Button(mainFrame, text="", command=test).grid(column=3, row=25, sticky=W)
ttk.Button(mainFrame, text="", command=test).grid(column=3, row=30, sticky=W)
ttk.Button(mainFrame, text="", command=test).grid(column=3, row=35, sticky=W)
ttk.Button(mainFrame, text="test", command=test).grid(column=3, row=40, sticky=W)

ttk.Label(mainFrame, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainFrame, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainFrame, text="meters").grid(column=3, row=2, sticky=W)

for child in mainFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>", calculate)


root.mainloop()