from tkinter import *
from tkinter import messagebox

def get_height():
    return float(ENTRY_HEIGHT.get())

def get_weight():
    return float(ENTRY_WEIGHT.get())

def calculate_bmi():
    try:
        height = get_height() / 100
        weight = get_weight()
        bmi = weight / (height ** 2)

        if height < 0 or weight < 0 :
            messagebox.showinfo("Error :", "Negative height or weight !")

        else :
            messagebox.showinfo("Your BMI calculated is : ", bmi)

    except ValueError:
        messagebox.showinfo("Error :", "Please enter valid data !")

if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>", calculate_bmi)
    TOP.geometry("400x400")
    TOP.configure(background="#8c52ff")
    TOP.title("BMI Calculator by Disk_MTH")
    TOP.resizable(width=False, height=False)

    # --------------------Labels--------------------#

    LABEL_TITLE = Label(TOP, bg="#8c52ff", fg="#ffffff", text="Welcome to BMI Calculator",
                        font=("Helvetica", 15, "bold"), pady=10)
    LABEL_TITLE.place(x=55, y=0)

    LABEL_SIZE = Label(TOP, bg="#ffffff", text="Enter Height (in cm):", bd=6, font=("Helvetica", 10, "bold"), pady=5)
    LABEL_SIZE.place(x=55, y=60)

    LABEL_WEIGHT = Label(TOP, bg="#ffffff", text="Enter Weight (in kg):", bd=6, font=("Helvetica", 10, "bold"), pady=5)
    LABEL_WEIGHT.place(x=55, y=121)

    # --------------------Entries--------------------#

    ENTRY_HEIGHT = Entry(TOP, bd=8, width=10, font="Roboto 11")
    ENTRY_HEIGHT.place(x=240, y=60)

    ENTRY_WEIGHT = Entry(TOP, bd=8, width=10, font="Roboto 11")
    ENTRY_WEIGHT.place(x=240, y=121)

    # --------------------Buttons--------------------#

    BUTTON = Button(bg="#000000", fg='#ffffff', bd=12, text="Calculate !", padx=33, pady=10, command=calculate_bmi,
                    font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=5, column=0, sticky=W)
    BUTTON.place(x=70, y=250)

    TOP.mainloop()