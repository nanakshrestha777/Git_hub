
import tkinter
class BMI:
    def __init__(self) :
        self.mw = tkinter.Tk()
        self.label1 = tkinter.Label(self.mw, text="height")
        # adding grid
        self.label1.grid (row = 0, column = 0)

        self.entry1 = tkinter.Entry(self.mw, width=10)

        self.entry1.grid (row = 0, column = 1)

        self.label2 = tkinter.Label(self.mw, text="weight")

        self.label2.grid(row = 1, column = 0)

        self.entry2 = tkinter.Entry(self.mw, width=10)

        self.entry2.grid(row = 1, column = 1)

        self.label3 = tkinter.Label(self.mw, text="")

        self.label3.grid(row = 2 , column = 2)
        self.buttom1 = tkinter.Button(self.mw , text="calculate Bmi", command = self.function1)
        self.buttom1.grid(row = 3, column = 3)

       
        tkinter.mainloop()

    def function1(self):
        height = float(self.entry1.get())
        weight = float(self.entry2.get())
        bmi = weight / (height * height)
        self.label3.config(text="the Bmi is {:.2f}.".format(bmi))
        

user = BMI()     

        

