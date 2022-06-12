from tkinter import *

def Convert():
    in_Kg=float(e1_value.get())
    in_Gram=in_Kg*1000
    in_Pounds=in_Kg*2.20462
    in_Ouns=in_Kg*35.274
    t1.insert(END,in_Gram)
    t2.insert(END,in_Pounds)
    t3.insert(END,in_Ouns)

def Clear():
    t1.delete("1.0","end")
    t2.delete("1.0", "end")
    t3.delete("1.0", "end")
    e1_value.set("")

wn=Tk()
wn.title("Weight Converter")
wn.config(bg="skyblue")

e1_value=StringVar()
e1=Entry(wn,font=("Arial",15),width=23,bg="white",text=e1_value,bd=2)
e1.grid(row=1,column=1)

button1=Button(wn,text="Convert",font=("Arial",10),width=8,bg="yellow",padx=10,pady=10,command=Convert)
button1.grid(row=1,column=2)

button2=Button(wn,text="Clear",font=("Arial",10),width=8,bg="yellow",padx=10,pady=10,command=Clear)
button2.grid(row=1,column=3)

label1=Label(wn,text="KG",font=("Arial",10),bg="skyblue",fg="black",padx=10,pady=10)
label1.grid(row=1,column=0)
label2=Label(wn,text="Enter weight bellow",font=("Arial",10),bg="skyblue",fg="black",padx=10,pady=10)
label2.grid(row=0,column=1)
label3=Label(wn,text="In grams",font=("Arial",10),bg="skyblue",fg="black",padx=10,pady=10)
label3.grid(row=2,column=1)
label4=Label(wn,text="In pounds",font=("Arial",10),bg="skyblue",fg="black",padx=10,pady=10)
label4.grid(row=2,column=2)
label5=Label(wn,text="In ounes",font=("Arial",10),bg="skyblue",fg="black",padx=10,pady=10)
label5.grid(row=2,column=3)

t1=Text(wn,height=1,width=20,bg="white",fg="black",font=("Arial",10))
t1.grid(row=3,column=1)
t2=Text(wn,height=1,width=18,bg="white",fg="black",font=("Arial",10),padx=10)
t2.grid(row=3,column=2)
t3=Text(wn,height=1,width=18,bg="white",fg="black",font=("Arial",10),padx=10)
t3.grid(row=3,column=3)
wn.mainloop()
