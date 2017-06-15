import csv as csv
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import math
from scipy.optimize import leastsq
import numpy as np
from matplotlib import rc
rc('text', usetex=True)
import papuaEx as ex 

import tkinter as tk


class SimpleTableInput(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)

        self._entry = {}
        self.rows = rows
        self.columns = columns

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")

        # create the table of widgets
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self, validate="key", validatecommand=vcmd, width=6)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        '''Return a list of lists, containing the data in the table'''
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result

    def _validate(self, P):
        '''Perform input validation. 

        Allow only an empty value, or a value that can be converted to a float
        '''
        if P.strip() == "":
            return True

        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        #self.table = SimpleTableInput(self, self.numRows, self.numCols)
        #self.submit = tk.Button(self, text="Submit", command=self.on_submit)
        #self.table.pack(side="top", fill="both", expand=True)
        #self.submit.pack(side="bottom")

    def on_submit(self):
        print(self.table.get())

    def set_matrix(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.table = SimpleTableInput(self, self.numRows, self.numCols)
        #self.submit = tk.Button(self, text="Submit", command=self.on_submit)
        self.table.pack(side="top", fill="both", expand=True)
        #self.submit.pack(side="bottom")


root = tk.Tk()
root.geometry('900x600')

def set_times_matrix(num):
    dataTkFrame = tk.Frame(width=850, height=300, bg='')
    dataTkFrame.grid(row=2, column=0, sticky='nsew', padx=2, pady=2)
    tk.Label(dataTkFrame, text="Time points:", font=("Helvetica", 12)).grid(row=1, column=0, sticky='e', padx=2, pady=2)
    times = Example(dataTkFrame)
    times.set_matrix(1, num)
    times.grid(row=1, column=1, sticky='w', padx=2, pady=2)
    iaa = Example(dataTkFrame)
    iaa.set_matrix(1, num)
    ibb = Example(dataTkFrame)
    ibb.set_matrix(1, num)
    iab = Example(dataTkFrame)
    iab.set_matrix(1, num)
    iba = Example(dataTkFrame)
    iba.set_matrix(1, num)
    tk.Label(dataTkFrame, text="IAA:", font=("Helvetica", 12)).grid(row=3, column=0, sticky='e', padx=2, pady=2)
    tk.Label(dataTkFrame, text="IBB:", font=("Helvetica", 12)).grid(row=4, column=0, sticky='e', padx=2, pady=2)
    tk.Label(dataTkFrame, text="IAB:", font=("Helvetica", 12)).grid(row=5, column=0, sticky='e', padx=2, pady=2)
    tk.Label(dataTkFrame, text="IBA:", font=("Helvetica", 12)).grid(row=6, column=0, sticky='e', padx=2, pady=2)
    iaa.grid(row=3, column=1, sticky='w', padx=2, pady=2)
    ibb.grid(row=4, column=1, sticky='w', padx=2, pady=2)
    iab.grid(row=5, column=1, sticky='w', padx=2, pady=2)
    iba.grid(row=6, column=1, sticky='w', padx=2, pady=2)
    

def data_file_entry():
    print("clicked in seq file entry box")
    seq_file_path = tk.filedialog.askopenfilename()
    data_file.delete(0, tk.END)
    data_file.insert(0, seq_file_path)
    data_file.xview(tk.END)




timeDataFileTkFrame = tk.Frame(height=20, bg='')
timeDataFileTkFrame.grid(row=0, column=0, sticky='w', padx=2, pady=2)

tk.Label(timeDataFileTkFrame, text="Number of time points:", font=("Helvetica", 12)).grid(row=0, column=0, sticky='e', padx=2, pady=2)
numVal = tk.StringVar()
numTimes = tk.Entry(timeDataFileTkFrame, width=2, textvariable=numVal).grid(row=0, column=1, sticky='w', padx=2, pady=2)
numVal.set('5')
numTimes_button = tk.Button(timeDataFileTkFrame, text="Submit", command= lambda: set_times_matrix(int(numVal.get()))).grid(row=0, column=2, sticky='ew', padx=2, pady=2)
tk.Label(timeDataFileTkFrame, text="Data File:", font=("Helvetica", 12)).grid(row=0, column=3, sticky='e', padx=2, pady=2)
data_file =  tk.Entry(timeDataFileTkFrame, width=16)
data_file.grid(row=0, column=4, sticky='ew', padx=2, pady=2)
data_file_button = tk.Button(timeDataFileTkFrame, text="Load Data", command=data_file_entry).grid(row=0, column=5, sticky='ew', padx=2, pady=2)


set_times_matrix(1)

root.mainloop()
