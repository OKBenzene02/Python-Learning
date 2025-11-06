import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def saving_fileas():
    filelocation = asksaveasfilename(defaultextension="txt", filetypes=[("Text file", "*.txt"), ("All files", "*.*")])

    if not filelocation:
        return

    with open(filelocation, 'w') as file_output:
        text = text_editing.get(1.0, tk.END)
        file_output.write(text)
    window.title(f"TKnotepad - {filelocation}")

def opening_file():
    filelocation = askopenfilename(filetypes=[("Text file", "*.txt"), ("All files", "*.*")])

    if not filelocation:
        return

    text_editing.delete(1.0, tk.END)
    with open(filelocation, 'r') as file_input:
        text = file_input.read()
        text_editing.insert(tk.END, text)
    window.title(f"Tknotepad - {filelocation}")

def saving_file():
    filelocation = asksaveasfilename(defaultextension="txt")
    if not filelocation:
        return

    with open(filelocation, 'a') as file_input_save:
        text = text_editing.get(1.0, tk.END)
        file_input_save.write(text)
    window.title(f"Tknotepad - {filelocation}")

def help():
    with open("help.txt", 'r') as help_file:
        text = help_file.read()
        text_editing.insert(tk.END, text)
    window.title(f"Tknotepad - Help")



window = tk.Tk()
window.title("TKnotepad")
window.rowconfigure(0, minsize=500)
window.columnconfigure(1, minsize=650)

text_editing = tk.Text(window)
text_editing.grid(row=0, column=1, sticky="nsew")

button_frame = tk.Frame(window, relief=tk.RIDGE, bd=2)
button_frame.grid(row=0, column=0, sticky="ns")

button_open = tk.Button(button_frame, text="Open", command=opening_file)
button_open.grid(row=0, column=0, padx=5, pady=5)

button_save = tk.Button(button_frame, text="Save", command=saving_file)
button_save.grid(row=1, column=0, padx=5, pady=5)

button_saveas = tk.Button(button_frame, text="Save As", command=saving_fileas)
button_saveas.grid(row=2, column=0, padx=5, pady=5)

button_Help = tk.Button(button_frame, text="Help", command=help)
button_Help.grid(row=3, column=0, padx=5, pady=5)


window.mainloop()