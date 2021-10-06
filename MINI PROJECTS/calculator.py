# a Python calculator
from tkinter import *


# the main class
class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = entry_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = int(text_box.get())

    def display(self, value):
        entry_box.delete(0, END)
        entry_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(entry_box.get()))
        self.display(self.current)


sum1 = Calc()
root = Tk()
root.geometry('300x300')

# frame
calc = Frame(root)
calc.grid()

root.title("Calculator")
# root.wm_iconbitmap("apple.ico")

root.resizable(width=FALSE, height=FALSE)
# or root.resizeable(0,0)

# entry box
entry_box = Entry(calc, justify=RIGHT, bd=2, font=('halvetica',20),width=19)
entry_box.grid(row=0, column=0, columnspan=4,padx=5, pady=10)
entry_box.insert(0, "0")

# buttons
numbers = "789456123"
i = 0
bttn = []
for j in range(2,5):
    for k in range(3):
        bttn.append(Button(calc, text=numbers[i], width=6))
        bttn[i].grid(row=j, column=k, padx=1, pady=10)
        bttn[i]["command"] = lambda x=numbers[i]: sum1.num_press(x)
        i += 1

bttn_0 = Button(calc, text="0", width=6)
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row=5, column=0, padx=5, pady=10)

bttn_div = Button(calc, text=chr(247), width=6)
bttn_div["command"] = lambda: sum1.operation("divide")
bttn_div.grid(row=2, column=3, padx=5, pady=10)

bttn_off = Button(calc, text="OFF", width=6)
bttn_off["command"] = root.destroy
bttn_off.grid(row=1, column=0, padx=5, pady=10)

bttn_mult = Button(calc, text=chr(215), width=6)
bttn_mult["command"] = lambda: sum1.operation("times")
bttn_mult.grid(row=3, column=3, padx=5, pady=5)

bttn_minus = Button(calc, text="-", width=6)
bttn_minus["command"] = lambda: sum1.operation("minus")
bttn_minus.grid(row=4, column=3, padx=5, pady=10)

bttn_point = Button(calc, text=".", width=6)
bttn_point["command"] = lambda: sum1.num_press(".")
bttn_point.grid(row=5, column=1, padx=5, pady=10)

bttn_add = Button(calc, text="+", width=6)
bttn_add["command"] = lambda: sum1.operation("add")
bttn_add.grid(row=5, column=3, padx=5, pady=10)

bttn_neg = Button(calc, text=chr(177), width=6)
bttn_neg["command"] = lambda : sum1.sign()
bttn_neg.grid(row=1, column=1, padx=5, pady=10)

bttn_clear = Button(calc, text="C", width=6)
bttn_clear["command"] = lambda : sum1.cancel()
bttn_clear.grid(row=1, column=2, padx=5, pady=10)

all_clear = Button(calc, text="AC", width=6)
all_clear["command"] = lambda : sum1.all_cancel()
all_clear.grid(row=1, column=3, padx=5, pady=10)

bttn_equals = Button(calc, text="=", width=6)
bttn_equals["command"] = lambda : sum1.calc_total()
bttn_equals.grid(row=5, column=2, padx=5, pady=10)

root.mainloop()