try:
    import tkinter
except ImportError: # python 2 error for tkinter
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("hello world")
mainWindow.geometry("640x480+30+50")

label = tkinter.Label(mainWindow, text="hello world")
label.pack(side='top')

leftframe = tkinter.Frame(mainWindow)
leftframe.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(mainWindow, relief="raised", borderwidth=3)
# canvas.pack(side="top", fill=tkinter.BOTH, expand=True)
canvas.pack(side="top")

rightframe = tkinter.Frame(mainWindow)
rightframe.pack(side="right", anchor="s", fill=tkinter.Y, expand=False)

button1 = tkinter.Button(mainWindow, text='Help')
button2 = tkinter.Button(mainWindow, text='Help 1')
button3 = tkinter.Button(mainWindow, text='Help 2')
button4 = tkinter.Button(mainWindow, text='Help 3')
button1.pack(side="left", anchor="n")
button2.pack(side="left", anchor="s")        # Anchor is a compass needle positions of Nor, Sou, Eas, Wes
button3.pack(side="left", anchor="e")
button4.pack(side="left", anchor="w")


mainWindow.mainloop()


