import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pandas as pd

##### create the root window
root = tk.Tk()
root.title('Read Excel')
root.resizable(False, False)
root.geometry('750x150')

lbl1 = tk.Label(root, text="Input Excel File")
lbl1.grid(column=0,row=0)

def select_file():
    filetypes = (('All files', '*.xlsx'),('text files', '*.txt'))
    filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    showinfo(title='Selected File',message=filename)
    lbl2['text']=(filename)
    print(filename)
    xlsx = pd.ExcelFile(filename)
    read_excelr(xlsx)
    
def read_excelr(xlsx):
    df=pd.read_excel(xlsx)
    print(df)
##### open button
open_button = ttk.Button(root,text='Open a File',command=select_file)
open_button.grid(column=1, row=0)
##### Text edit
lbl2 = tk.Label(root, text='None')
lbl2.grid(column=2,row=0)

##### run the application
root.mainloop()