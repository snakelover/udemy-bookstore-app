import tkinter

def kms_to_miles():
    miles = float(entry1_value.get()) * 1.6
    text1.delete("@0,0", tkinter.END)
    text1.insert(tkinter.CURRENT, miles)


window = tkinter.Tk()

button1 = tkinter.Button(window, text="Execute", command=kms_to_miles)
button1.grid(row=0, column=0)

entry1_value = tkinter.StringVar()
entry1 = tkinter.Entry(window, textvariable=entry1_value)
entry1.grid(row=0, column=1)

text1 = tkinter.Text(window, height=1, width=20)
text1.grid(row=0, column=2)
window.mainloop()