from tkinter import *

from tkinter import ttk 
window = Tk()
window.geometry("300x350")
window.title('calculator')
style= ttk.Style()
style.configure("C.TLabel", foreground="white",padding=4,background="black",anchor=CENTER)
style.configure("D.TLabel", foreground="white",padding=4,background="blue",anchor=CENTER)
style.configure("E.TLabel", foreground="white",padding=4,background="orange",anchor=CENTER)

# style.map("C.TButton",
#     foreground=[('pressed', 'white'), ('active', 'white')],
#     background=[('pressed', 'black'), ('active', 'black')]
#     )
style.map('C.TLabel',
    foreground = [('pressed','red'),('active','blue')],
    background = [('pressed','!disabled','black'),('active','white')],
    relief=[('pressed', 'sunken'),
            ('!pressed', 'raised')]
)
# window.configure(background='gold')
text=""
def show(buttonValue):
    global text
    text += buttonValue
    label.configure(text=text)
def calc():
    global text
    res=eval(text)
    label.configure(text=res)
    text=''
    text+=str(res)
    
def clear():
    global text
    text=" "
    label.configure(text=text)
def sqr():
    global text
    val = int(text[-1])**2
    p=text[-1]
    rplace= text.replace(p,str(val),1)
    text = rplace
    label.configure(text=rplace)



label = ttk.Label(window,text="",width=15,font=('arial',16,"bold"))
label.pack()
ttk.Button(window,text="C",style="D.TLabel",width=7,command=lambda:clear()).place(x=10,y=100)
ttk.Button(window,text="%",style="C.TLabel",width=7,command=lambda:show("%")).place(x=80,y=100)
ttk.Button(window,text="/",style="C.TLabel",width=7,command=lambda:show("/")).place(x=150,y=100)
ttk.Button(window,text="*",style="C.TLabel",width=7,command=lambda:show("*")).place(x=230,y=100)

ttk.Button(window,text="7",style="C.TLabel",width=7,command=lambda:show("7")).place(x=10,y=150)
ttk.Button(window,text="8",style="C.TLabel",width=7,command=lambda:show("8")).place(x=80,y=150)
ttk.Button(window,text="9",style="C.TLabel",width=7,command=lambda:show("9")).place(x=150,y=150)
ttk.Button(window,text="-",style="C.TLabel",width=7,command=lambda:show("-")).place(x=230,y=150)

ttk.Button(window,text="4",style="C.TLabel",width=7,command=lambda:show("4")).place(x=10,y=200)
ttk.Button(window,text="5",style="C.TLabel",width=7,command=lambda:show("5")).place(x=80,y=200)
ttk.Button(window,text="6",style="C.TLabel",width=7,command=lambda:show("6")).place(x=150,y=200)
ttk.Button(window,text="+",style="C.TLabel",width=7,command=lambda:show("+")).place(x=230,y=200)

ttk.Button(window,text="1",style="C.TLabel",width=7,command=lambda:show("1")).place(x=10,y=250)
ttk.Button(window,text="2",style="C.TLabel",width=7,command=lambda:show("2")).place(x=80,y=250)
ttk.Button(window,text="3",style="C.TLabel",width=7,command=lambda:show("3")).place(x=150,y=250)
ttk.Button(window,text="sqr",style="C.TLabel",width=7,command=lambda:sqr()).place(x=230,y=250)

ttk.Button(window,text="0",style="C.TLabel",width=7,command=lambda:show("0")).place(x=10,y=300)
ttk.Button(window,text=".",style="C.TLabel",width=7,command=lambda:show(".")).place(x=80,y=300)
ttk.Button(window,text="=",style="E.TLabel",width=8,command=lambda:calc()).place(x=150,y=300)


# image = PhotoImage(file="Screenshot (58).PNG")
# img = Label(window, image=image)
# img.place(x=150,y=300)

window.mainloop()