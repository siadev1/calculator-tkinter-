from tkinter import *
window = Tk()
window.geometry("300x350")
window.title('calculator')
# window.configure(bg='gold')
text=""
def show(buttonValue):
    global text
    text+= buttonValue
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


label = Label(window,text="",fg="black",height=3,relief="solid",width=25,font=('arial',16,"bold"))
label.pack()
Button(window,text="C",bg="blue",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:clear()).place(x=10,y=100)
Button(window,text="%",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("%")).place(x=80,y=100)
Button(window,text="/",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("/")).place(x=150,y=100)
Button(window,text="*",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("*")).place(x=230,y=100)

Button(window,text="7",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("7")).place(x=10,y=150)
Button(window,text="8",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("8")).place(x=80,y=150)
Button(window,text="9",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("9")).place(x=150,y=150)
Button(window,text="-",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("-")).place(x=230,y=150)

Button(window,text="4",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("4")).place(x=10,y=200)
Button(window,text="5",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("5")).place(x=80,y=200)
Button(window,text="6",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("6")).place(x=150,y=200)
Button(window,text="+",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("+")).place(x=230,y=200)

Button(window,text="1",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("1")).place(x=10,y=250)
Button(window,text="2",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("2")).place(x=80,y=250)
Button(window,text="3",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show("3")).place(x=150,y=250)

Button(window,text="0",bg="black",fg="white",width=9,relief="solid",font=('arial',16,"bold"),command=lambda:show("0")).place(x=10,y=300)
Button(window,text=".",bg="black",fg="white",width=3,relief="solid",font=('arial',16,"bold"),command=lambda:show(".")).place(x=150,y=300)
Button(window,text="=",bg="orange",fg="white",width=3,height=3,relief="solid",font=('arial',16,"bold"),command=lambda:calc()).place(x=230,y=250)



window.mainloop()