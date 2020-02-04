from tkinter import *
from tkinter import messagebox

list=[]
def add():
    '''data=Lb.get(ACTIVE)'''
    tb.insert(END,"\n %s"%(prodname.get() ))
    tb.insert(END, "\t %d" %(MRP.get()))
    tb.insert(END, "X%d" % (qnt.get()))
    list.append(MRP.get()*qnt.get())
    tp = MRP.get()*qnt.get()
    nm = prodname.get()
    pname.append(nm)
    pprice.append(tp)
    e2.delete(0,END)
    e3.delete(0, END)
    e4.delete(0, END)

def total():
    top = Toplevel();
    Label(top, text='TOTAL BILL', font='Helvetica 18 bold').grid(row=0, column=0)
    Label(top, text="Item", font='Roboto 14 bold').grid(row=1, column=0)
    Label(top, text="Price", font='Roboto 14 bold').grid(row=1, column=1)
    i = 1
    for x in range(len(pname)):
        Label(top, text=pname[x],font='Arial 12 bold').grid(row=i + 1, column=0)
        Label(top, text=pprice[x],font='Arial 12 bold').grid(row=i + 1, column=1)
        i+=1
    Label(top, text='', font='Roboto 10 bold').grid(row=i + 1, column=0)
    Label(top, text='THANKS FOR SHOPPING WITH US %s !!'%(nameinfo.get()), font='Roboto 10 bold').grid(row=i+2, column=0)
    Label(top, text='KINDLY PAY TOTAL : ', font='Roboto 10 bold').grid(row=i+3, column=0)
    Label(top, text='%d'%(sum(pprice)), font='Roboto 10 bold').grid(row=i + 3, column=1)
    Button(top, text='Print Bill', width=12, bd=3, command=top.quit).grid(row=i + 4, column=1)



def clr():
    tb.delete(1.0,END)
    list.clear()
    pname.clear()
    price.clear()
    
f=Tk()
f.title("Billing")

nameinfo=StringVar()
prodname=StringVar()
data=IntVar()
qnt=IntVar()
MRP=IntVar()
pname = []
pprice = []

tle=Label(f,text='BILLING SYSTEM', font='Helvetica 18 bold')
name=Label(f,text='Name :')
e1=Entry(f,width=15,bd=3,textvariable=nameinfo)

prod=Label(f,text='Product :',bd=3)
e3=Entry(f,width=15,bd=3,textvariable=prodname)
mrp=Label(f,text='Price :',bd=3)
e4=Entry(f,width=15,bd=3,textvariable=MRP)

quan=Label(f,text='Quantity :')
e2=Entry(f,width=15,bd=3,textvariable=qnt)

b1=Button(f,text='Add Items',width=12,bd=3,command=add)

tb=Text(f,width=30,bd=3)

b3=Button(f,text='Clear Items',width=12,bd=3,command=clr)

b2=Button(f,text='Total',width=12,bd=3,command=total)
tle.grid(row=0,padx=5,pady=5)
name.grid(row=1,column=0,padx=5,pady=5)
e1.grid(row=1,column=1,padx=5,pady=5)
prod.grid(row=2,column=0,padx=5,pady=5)
e3.grid(row=2,column=1,padx=5,pady=5)
mrp.grid(row=3,column=0,padx=5,pady=5)
e4.grid(row=3,column=1,padx=5,pady=5)
quan.grid(row=4,column=0,padx=5,pady=5)
e2.grid(row=4,column=1,padx=5,pady=5)
b1.grid(row=5,column=1,padx=5,pady=5)
tb.grid(row=6,columnspan=2,padx=5,pady=5)
b3.grid(row=7,column=0,padx=5,pady=5)
b2.grid(row=7,column=1,padx=5,pady=5)

f.mainloop()
