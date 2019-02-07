from tkinter import *
from tkinter import ttk

length1=0
length2=0
final_result=0
op1=0
operator_flag=0
operator=""
def entryinsert(n):
    global length1
    global length2
    global operator_flag
    if(operator_flag==0):
        operand1.insert('end', n)
        operator_flag=0
        length1 += 1
    else:
        operand2.insert('end', n)
        operator_flag=1
        length2 += 1
def backspace():
    global length1
    global length2
    global operator_flag
    if(operator_flag==0):
        operand1.delete(length1-1)
        length1 -= 1
    else:
        operand2.delete(length2-1)
        length2 -= 1
def operator_clicked(op):
    global final_result
    global op1
    global operator_flag
    global operator
    op1 = float(operand1.get())
    operator_flag=1
    if(op=='+'):
        op_label.configure(text="+")
        op_label.grid(row=1)
        operator="+"
    elif(op=='-'):
        op_label.configure(text="-")
        op_label.grid(row=1)
        operator = "-"
    elif (op == '*'):
        op_label.configure(text="*")
        op_label.grid(row=1)
        operator = "*"
    elif (op == '/'):
        op_label.configure(text="/")
        op_label.grid(row=1)
        operator = "/"
    result_label.configure(text='{}'.format(op1)+op)

def equal():
    global op1
    global final_result
    global operator
    global operator_flag
    global length1
    if(operator=='+'):
        final_result = op1 + float(operand2.get())
    elif(operator=='-'):
        final_result = op1 - float(operand2.get())
    elif (operator == '*'):
        final_result = op1 * float(operand2.get())
    elif (operator == '/'):
        final_result = op1 / float(operand2.get())
    operator_flag=0
    operand1.delete(0,'end')
    operand2.delete(0,'end')
    final_result_shrinked="{0:.2f}".format(final_result)
    final_result=float(final_result_shrinked)
    operand1.insert('end',final_result)
    length1=len(final_result_shrinked)
    op1=final_result
    op_label.grid_forget()
    result_label.configure(text=final_result)
def all_cancel():
    global operator_flag
    result_label.configure(text="")
    operand1.delete(0,'end')
    operand2.delete(0,'end')
    op_label.grid_forget()
    operator_flag=0

root=Tk()
root.resizable(False,False)
root.title("Calculator")

style=ttk.Style()
style.configure('Header.TLabel',font=('Arial',18,'bold'))

result_label=ttk.Label(root,style='Header.TLabel')
result_label.grid(row=0,column=3,stick='w')
operand1=ttk.Entry(root)
operand1.grid(row=0,columnspan=3,stick='w')
operand2=ttk.Entry(root)
operand2.grid(row=2,columnspan=3,stick='w')
op_label=ttk.Label()


ttk.Button(root,text="1",command=lambda :entryinsert("1")).grid(row=3,column=0)
ttk.Button(root,text="2",command=lambda :entryinsert("2")).grid(row=3,column=1)
ttk.Button(root,text="3",command=lambda :entryinsert("3")).grid(row=3,column=2)
ttk.Button(root,text="+",command=lambda :operator_clicked("+")).grid(row=7,column=0)


ttk.Button(root,text="4",command=lambda :entryinsert("4")).grid(row=4,column=0)
ttk.Button(root,text="5",command=lambda :entryinsert("5")).grid(row=4,column=1)
ttk.Button(root,text="6",command=lambda :entryinsert("6")).grid(row=4,column=2)
ttk.Button(root,text="-",command=lambda :operator_clicked("-")).grid(row=7,column=1)



ttk.Button(root,text="7",command=lambda :entryinsert("7")).grid(row=5,column=0)
ttk.Button(root,text="8",command=lambda :entryinsert("8")).grid(row=5,column=1)
ttk.Button(root,text="9",command=lambda :entryinsert("9")).grid(row=5,column=2)
ttk.Button(root,text="*",command=lambda :operator_clicked("*")).grid(row=7,column=2)



ttk.Button(root,text="0",command=lambda :entryinsert("0")).grid(row=6,column=1)
ttk.Button(root,text="del",command=backspace).grid(row=6,column=2)
ttk.Button(root,text="C",command=all_cancel).grid(row=6,column=0)
ttk.Button(root,text="/",command=lambda :operator_clicked("/")).grid(row=7,column=3)

ttk.Button(root,text="=",command=equal).grid(row=3,column=3,rowspan=4,stick='nsew')



for i in root.grid_slaves():
    i.grid(padx=5,pady=5)
root.mainloop()