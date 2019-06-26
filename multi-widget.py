import tkinter

def convert():
    kgs_to_grams()
    kgs_to_pounds()
    kgs_to_ounces()

def kgs_to_grams():
    miles = float(entry1_value.get()) * 1000
    text1.delete("@0,0", tkinter.END)
    text1.insert(tkinter.CURRENT, miles)

def kgs_to_pounds():
    miles = float(entry1_value.get()) * 2.20462
    text2.delete("@0,0", tkinter.END)
    text2.insert(tkinter.CURRENT, miles)

def kgs_to_ounces():
    miles = float(entry1_value.get()) * 35.274
    text3.delete("@0,0", tkinter.END)
    text3.insert(tkinter.CURRENT, miles)

window = tkinter.Tk()

label1 = tkinter.Label(window, text="Kg")
label1.grid(row=0, column=0)

entry1_value = tkinter.StringVar()
entry1 = tkinter.Entry(window, textvariable=entry1_value)
entry1.grid(row=0, column=1)

button1 = tkinter.Button(window, text="Convert", command=convert)
button1.grid(row=0, column=2)

text1 = tkinter.Text(window, height=1, width=20)
text1.grid(row=1, column=0)
text2 = tkinter.Text(window, height=1, width=20)
text2.grid(row=1, column=1)
text3 = tkinter.Text(window, height=1, width=20)
text3.grid(row=1, column=2)

window.mainloop()