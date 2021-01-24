# Libaries Imported
from tkinter import *

#Main Configurations
root = Tk()
root.geometry("400x440")
root.configure(bg="grey")
root.title("Kunal Calculator")
root.iconbitmap("calc.ico")
root.resizable(False, False)

#Functions to Run

def press(event):
    global varname1
    text = event.widget.cget("text")
    if text == "=":
        if varname1.get().isdigit():
            value = int(varname1.get())
        else:
            value = eval(mainbox.get())

        varname1.set(value)
        mainbox.update()
    elif text == "C":
        varname1.set("")
        mainbox.update()
    else:
        varname1.set(varname1.get() + text)
        mainbox.update()
# Main Box
varname1 = StringVar()
mainbox = Entry(root, width="17", textvar=varname1, state="readonly", font=('ubuntu', 30, 'bold'))
mainbox.place(x=10, y=2)

# Buttons to Add 

btn9 = Button(root, text="9",padx=13, bg="pink", fg="white", font=('ubuntu', 20, 'bold'),)
btn9.place(x=15, y=60)
btn9.bind("<Button-1>",  press)

btn8 = Button(root, text="8",padx=13, bg="pink", fg="white", font=('ubuntu', 20, 'bold'))
btn8.place(x=115, y=60)
btn8.bind("<Button-1>",  press)

btn7 = Button(root, text="7",padx=13, bg="pink", fg="white", font=('ubuntu', 20, 'bold'))
btn7.place(x=215, y=60)
btn7.bind("<Button-1>",  press)

btn6 = Button(root, text="6",padx=13, bg="pink", fg="white", font=('ubuntu', 20, 'bold'))
btn6.place(x=15, y=150)
btn6.bind("<Button-1>",  press)

btn5 = Button(root, text="5",padx=13, bg="pink", fg="white", font=('ubuntu', 20, 'bold'))
btn5.place(x=115, y=150)
btn5.bind("<Button-1>",  press)

btn4 = Button(root, text="4",padx=13, bg="pink", fg="white", font=('ubuntu', 20, 'bold'))
btn4.place(x=215, y=150)
btn4.bind("<Button-1>",  press)

btn3 = Button(root, text="3",padx=13, bg="pink", fg="white", font=('ubuntu', 20, 'bold'))
btn3.place(x=15, y=240)
btn3.bind("<Button-1>",  press)

btn2 = Button(root, text="2",padx=13, bg="pink", fg="white", font=('ubuntu', 20, 'bold'))
btn2.place(x=115, y=240)
btn2.bind("<Button-1>",  press)

btn1 = Button(root, text="1",padx=13, bg="pink", fg="white", font=('ubuntu', 20, 'bold'))
btn1.place(x=215, y=240)
btn1.bind("<Button-1>",  press)

btnstar = Button(root, text="*",padx=15, bg="pink", fg="white", font=('ubuntu', 20, 'bold'))
btnstar.place(x=115, y=330)
btnstar.bind("<Button-1>",  press)

btnslash = Button(root, text="/",padx=17, bg="pink", fg="white", font=('ubuntu', 20, 'bold'))
btnslash.place(x=215, y=330)
btnslash.bind("<Button-1>",  press)

btnadd = Button(root, text="+",padx=13, bg="pink", fg="white", font=('ubuntu', 20, 'bold'))
btnadd.place(x=15, y=330)
btnadd.bind("<Button-1>",  press)

btnminus = Button(root, text="-",padx=15, bg="pink", fg="white",  font=('ubuntu', 20, 'bold'))
btnminus.place(x=315, y=330)
btnminus.bind("<Button-1>",  press)

btnC = Button(root, text="C",padx=9, pady=15, bg="red", fg="white", font=('ubuntu', 20, 'bold'))
btnC.place(x=315, y=230)
btnC.bind("<Button-1>",  press)

btnequal = Button(root, text="=",padx=11, pady=48, bg="blue", fg="white", font=('ubuntu', 20, 'bold'))
btnequal.place(x=315, y=60)
btnequal.bind("<Button-1>",  press)

Label1 = Label(root, text="Designed and Developed By Kunal Gupta", fg="yellow", bg="grey", font=('ubuntu', 15, 'bold'))
Label1.place(x=3, y=400)



root.mainloop()