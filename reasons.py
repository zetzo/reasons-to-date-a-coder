from tkinter import*
import math
from math import sqrt

def solver (a):
    A=a
    text=0
    if a==1:
        text="We can take you to the cloud"
    else:
        if a==2:
            text="We make thiings simpler, not complicated"
        else:
            if a==3:
                text="We have sailed the seas(Cs)"
            else:
                if a==4:
                    text="We can create a cookie for you"
                else:
                    if a==5:
                        text="We are not even afraid of Pythons"
    return text
def inserter(value):
     output.delete("0.0","end")
     output.insert("0.0",value)    

def clear(event):
     caller=event.widget
     caller.delete("0", "end")

def handler():
     try:
          a_val=int(a.get())
          inserter(solver(a_val))
     except ValueError:
        inserter("Проверьте введенные данные еще раз")

root=Tk()
root.title("The reasons for date a programmer. Made by zetzo")
root.minsize(200,230)
root.resizable(width=False, height=False)


frame=Frame(root)
frame.grid()

a =Entry(frame, width=3)
a.grid(row=1,column=1,padx=(10,0))
a.bind("<FocusIn>", clear)
a_lab= Label(frame, text="-number of a reason(from1-5)").grid(row=1,column=2)

but = Button(frame, text="Показать Результат", command=handler).grid(row=1, column=7, padx=(10,0))

output = Text(frame, bg="white", font="cocolas 12", width=50, height=10)
output.grid(row=2, columnspan=8)

root.mainloop()

    
    
    
