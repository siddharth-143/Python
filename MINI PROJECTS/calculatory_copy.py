from tkinter import *

root = Tk()
root.title('calculator')
root.resizable(0,0)
root.geometry('300x290+12+12')

# entry box
entry_box=Entry(root,width=19,borderwidth=2,font=('helvetica',20),justify=RIGHT)
entry_box.insert(0,'0')
entry_box.grid(row=0,column=0,columnspan=5,padx=5,pady=20)

def click_me(num):
    if entry_box.get()=='0':
        entry_box.delete(0)
        entry_box.insert(0,num)
    else:
        length=len(entry_box.get())
        entry_box.insert(length,str(num))

# delete the sigle num
def click_delete():
    length = len(entry_box.get())
    entry_box.delete(length-1)

# clear the output
def click_clear():
    entry_box.delete(0,END)

# buttons
button_mc=Button(root,text='MC',padx=5,pady=5,width=5,command=lambda: click_me())
button_mr=Button(root,text='MR',padx=5,pady=5,width=5,command=lambda: click_me())
button_ms=Button(root,text='MS',padx=5,pady=5,width=5,command=lambda: click_me())
button_mp=Button(root,text='M+',padx=5,pady=5,width=5,command=lambda: click_me())
button_mn=Button(root,text='M-',padx=5,pady=5,width=5,command=lambda: click_me())

button_arrow=Button(root,text='<-',padx=5,pady=5,width=5,command=lambda: click_me())
button_ce=Button(root,text='CE',padx=5,pady=5,width=5,command=lambda: click_delete())
button_c=Button(root,text='C',padx=5,pady=5,width=5,command=lambda: click_clear())
button_ps=Button(root,text='+-',padx=5,pady=5,width=5,command=lambda: click_me())
button_root=Button(root,text='\\',padx=5,pady=5,width=5,command=lambda: click_me())

button_7=Button(root,text='7',padx=5,pady=5,width=5,command=lambda: click_me(7))
button_8=Button(root,text='8',padx=5,pady=5,width=5,command=lambda: click_me(8))
button_9=Button(root,text='9',padx=5,pady=5,width=5,command=lambda: click_me(9))
button_division=Button(root,text='/',padx=5,pady=5,width=5,command=lambda: click_me())
button_per=Button(root,text='%',padx=5,pady=5,width=5,command=lambda: click_me())

button_4=Button(root,text='4',padx=5,pady=5,width=5,command=lambda: click_me(4))
button_5=Button(root,text='5',padx=5,pady=5,width=5,command=lambda: click_me(5))
button_6=Button(root,text='6',padx=5,pady=5,width=5,command=lambda: click_me(6))
button_multiplication=Button(root,text='*',padx=5,pady=5,width=5,command=lambda: click_me)
button_1_x=Button(root,text='1/x',padx=5,pady=5,width=5,command=lambda: click_me)

button_1=Button(root,text='1',padx=5,pady=5,width=5,command=lambda : click_me(1))
button_2=Button(root,text='2',padx=5,pady=5,width=5,command=lambda: click_me(2))
button_3=Button(root,text='3',padx=5,pady=5,width=5,command=lambda: click_me(3))
button_substraction=Button(root,text='-',padx=5,pady=5,width=5,command=lambda: click_me())
button_eql=Button(root,text='=',padx=5,pady=22,width=5,command=lambda: click_me())

button_0=Button(root,text='0',padx=35,pady=5,width=5,command=lambda: click_me(0))
button_point=Button(root,text='.',padx=5,pady=5,width=5,command=lambda: click_me('.'))
button_pls=Button(root,text='+',padx=5,pady=5,width=5,command=lambda: click_me())


# display button
button_mc.grid(row=1,column=0)
button_mr.grid(row=1,column=1)
button_ms.grid(row=1,column=2)
button_mn.grid(row=1,column=3)
button_mp.grid(row=1,column=4)

button_arrow.grid(row=2,column=0)
button_ce.grid(row=2,column=1)
button_c.grid(row=2,column=2)
button_ps.grid(row=2,column=3)
button_root.grid(row=2,column=4)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_division.grid(row=3,column=3)
button_per.grid(row=3,column=4)

button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)
button_multiplication.grid(row=4,column=3)
button_1_x.grid(row=4,column=4)

button_1.grid(row=5,column=0)
button_2.grid(row=5,column=1)
button_3.grid(row=5,column=2)
button_substraction.grid(row=5,column=3)
button_eql.grid(row=5,column=4,rowspan=2)

button_0.grid(row=6,column=0,columnspan=2)
button_point.grid(row=6,column=2)
button_pls.grid(row=6,column=3)


root.mainloop()