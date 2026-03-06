import tkinter as tk

root=tk.Tk()
root.title('First Calculator')
#root.geometry('200x200')
root.resizable(False,False)

def button_click(number):
    entry.insert(tk.END,number) #add the num to entry
        
def result():
    now=entry.get()    
    result=eval(now)
    entry.delete(0,tk.END)
    entry.insert(0,result)
    
def exception_handling():
    try:
        result()
    
    except ZeroDivisionError:
        entry.delete(0,tk.END)
        entry.insert(0,"Error Divide by Zero ")

    except SyntaxError:
        entry.delete(0,tk.END)
        entry.insert(0,"Invalid Syntax")

entry=tk.Entry(root ,borderwidth=3 ,width=20 )
entry.grid(row=0,column=0,columnspan=10,padx=10,pady=10)
entry.focus()

for i in range(9):
    btn_text=str(i+1)

    btn=tk.Button(root ,text=btn_text , borderwidth=1,width=5 ,height=2,
                   command=lambda val=btn_text: button_click(val))
    btn.grid(row=(i//3)+1,column=(i%3) ,padx=2,pady=2)


btn0=tk.Button(root ,text='0'  ,borderwidth=1,width=5,height=2,
                command= lambda: button_click(0))  .grid(row=4,column=1)


ButtonSum=tk.Button(root,text="-" ,borderwidth=1,background="lightblue",width=5,height=2,
                     command= lambda: button_click("-")).grid(row=3,column=3)

ButtonMinus=tk.Button(root,text="*" ,borderwidth=1,background="lightblue" ,width=5,height=2,
                       command= lambda: button_click("*")).grid(row=2,column=3)

ButtonMultiply=tk.Button(root,text="/" ,borderwidth=1 ,background="lightblue",width=5,height=2,
                          command= lambda: button_click("/")).grid(row=1,column=3)

ButtonDiv=tk.Button(root,text="+"  ,borderwidth=1,background="lightblue",width=5,height=2,
                     command= lambda: button_click("+")).grid(row=4,column=3)


ButtonResult=tk.Button(root,text= "=",borderwidth=1,background="lightgreen",width=5,height=2,
                        command= lambda: exception_handling()).grid(row=4,column=2)

ButtonClear=tk.Button(root,text="AC" ,borderwidth=1,width=5,height=2 ,background="yellow",
                      command=lambda : entry.delete(0,tk.END)) .grid(row=4,column=0)



root.mainloop()