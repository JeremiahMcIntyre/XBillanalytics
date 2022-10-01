from tkinter import *
from tkinter import filedialog
from csv import *
from matplotlib import pyplot as plt
import numpy as np

class GUI:
    """
    A class for the GUI of the widget
    """


    def __init__(self, window) -> None:
        """
            Constructor to create the initial state of a widget
            :return None
        """
        self.window = window

        self.frame_file = Frame(self.window)
        self.label_file = Label(self.frame_file, text='File')
        self.entry_file = Entry(self.frame_file, width=100)
        self.label_file.pack(padx=5, side='left')
        self.entry_file.pack(padx=5, side='left')
        self.frame_file.pack(anchor='w', pady=10)

        self.frame_submit = Frame(self.window)
        self.button_submit = Button(self.frame_submit, text='Select File', command=self.get_file)
        self.button_submit.pack()
        self.frame_submit.pack()

        self.frame_gettotal = Frame(self.window)
        self.button_gettotal = Button(self.frame_gettotal, text='Process', command=self.process_file)
        self.button_gettotal.pack()
        self.frame_gettotal.pack(side='bottom')


    def get_file(self) ->None:
        """
        Method that opens a file dialog window.
        :retun None
        """
        self.filepath = filedialog.askopenfilename(filetypes = (('csv files', '*.csv'),))
        self.entry_file.insert(0, self.filepath)

    def process_file(self):
        """
        Method that opens a csv file.  Extracts premium tax owed data from every field matching the dropdown menu
        calculates a total and displays it. Has exception handling incase someone tries to run without selecting a valid
        file.
        :return None
        """
        self.total = 0.0
        self.companies_dict = {}
        with open(self.entry_file.get(), 'r', ) as file:
            csv_file = reader(file)
            for row in csv_file:
                if row[4] not in self.companies_dict:
                    if row[4] != 'AB_Invoice ID':
                        self.companies_dict[row[4]] = float(row[5])
                else:
                    self.companies_dict[row[4]] += float(row[5])
        self.companies = list(self.companies_dict.keys())
        self.tax_liability = list(self.companies_dict.values())
        self.total = sum(self.tax_liability)
        self.percent = [((x/self.total) * 100) for x in self.tax_liability]
        self.array = np.array(self.percent)
        self.fig2 = []
        for i in range(len(self.companies)):
            self.fig2.append([self.companies[i], round(self.tax_liability[i],2)])
        fig1 = plt.figure("Figure 1")
        plt.pie(self.array, labels = self.companies)
        plt.legend()
        fig2 = plt.figure("Figure 2")
        plt.axis('off')
        self.collabel = ("Company Name", "Tax Liability")
        plt.table(cellText=self.fig2,colLabels=self.collabel,loc='center')
        plt.show()









