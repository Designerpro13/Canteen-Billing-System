from tkinter import *
import random
import time
import math
import sqlite3 as mc
#import mysql.connector as mc
from datetime import date,datetime
from tkinter import messagebox
from functools import partial
import sys

'''
mysql_config={'host':'localhost','user':'root','password':'1234','port':3309,'database':"ngp"}
con=mc.connect(**mysql_config)
cur=con.cursor()
'''
con=mc.connect('ngp.db') #main database
cur=con.cursor() #main cursor

a='create table if not exists login(username varchar(32) primary key, password varchar(29) not null)'
cur.execute(a)
con.commit()
qry='create table if not exists PL(FF float,Lunch float,Burger float,pizza float,CB float,drinks float)'
cur.execute(qry)
con.commit()

def update_cost():
    def get_all():
        q=int(f.get())
        r=int(l.get())
        s=int(b.get())
        t=int(p.get())
        u=int(c.get())
        v=int(d.get())
        qry="update pl set FF={},lunch={},burger={},pizza={},cb={},drinks={};".format(q,r,s,t,u,v)
        cur.execute(qry)
        con.commit()
        cur.execute('select * from pl;')
        for i in range(2):
            q=cur.fetchone()
            print(q)
        messagebox.showinfo('Sussecs','Items updated')
        roo.destroy()
    roo = Tk()
    roo.geometry("400x420+0+0")
    roo.title("update")
    roo['bg']='pink'
    Label(roo,text="enter the price to be updated for french fries:").grid(row=1,column=1,padx=5,pady=5,columnspan=1)
    Label(roo,text="enter the price to be updated for lunch:").grid(row=2,column=1,padx=5,pady=5,columnspan=1)
    Label(roo,text="enter the price to be updated for burger:").grid(row=3,column=1,padx=5,pady=5,columnspan=1)
    Label(roo,text="enter the prize to be updated for pizza:").grid(row=4,column=1,padx=5,pady=5,columnspan=1)
    Label(roo,text="enter the amount to be updated for cb:").grid(row=5,column=1,padx=5,pady=5,columnspan=1)
    Label(roo,text="enter the amount to be updated for drinks:").grid(row=6,column=1,padx=5,pady=5,columnspan=1)
    f=Entry(roo,width=10)
    f.grid(row=1,column=2,padx=5,pady=5)
    l=Entry(roo,width=10)
    l.grid(row=2,column=2,padx=5,pady=5)
    b=Entry(roo,width=10)
    b.grid(row=3,column=2,padx=5,pady=5)
    p=Entry(roo,width=10)
    p.grid(row=4,column=2,padx=5,pady=5)
    c=Entry(roo,width=10)
    c.grid(row=5,column=2,padx=5,pady=5)
    d=Entry(roo,width=10)
    d.grid(row=6,column=2,padx=5,pady=5)
    Button(roo,text='Update Prices',command=get_all).grid(row=7,column=1,columnspan=2)


def Bill_me():
    def Ref():
        cof =float(Fries.get())
        colfries= float(Largefries.get())
        cob= float(Burger.get())
        cofi= float(Filet.get())
        cochee= float(Cheese_burger.get())
        codr= float(Drinks.get())
        t = date.today()
        now=datetime.now()
        x=int(str(t.month)+str(t.day)+str(now.hour)+str(now.minute)+str(now.second))
        costoffries = cof*25
        costoflargefries = colfries*40
        costofburger = cob*35
        costoffilet = cofi*50
        costofcheeseburger = cochee*30
        costofdrinks = codr*35
        
        costofmeal = "₹",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
        PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.01)
        Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
        OverAllCost="₹",str( PayTax + Totalcost )
        PaidTax="₹",str('%.2f'% PayTax)
        
                   
        if  not cof.isnumeric():
            cof=0.0
        else:
            cof=float(cof)
        if not colfries.isnumeric():
            colfries=0.0
        else:
            colfries=float(colfries)
        if not cob.isnumeric():
            cob=0.0
        else:
            cob=float(cob)
            
        if not cofi.isnumeric():        
            cofi=0.0
        else:
            cofi=float(cofi)
        if not cochee.isnumeric():
            cochee=0.0
        else:
            cochee=float(cochee)
        if not codr.isnumeric():
            codr=0.0
        else:
            codr=float(codr)
    
        costoffries = cof*25
        costoflargefries = colfries*40
        costofburger = cob*35
        costoffilet = cofi*50
        costofcheeseburger = cochee*30
        costofdrinks= codr*35
        
        costofmeal = "₹",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
        PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.01)
        
        Totalcost=math.ceil((costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks))
    
        
        OverAllCost="₹",str(math.ceil( PayTax + Totalcost ))
        PaidTax="₹",str('%.2f'% PayTax)
    
        cost.set(costofmeal)
        Tax.set(PaidTax)
        Subtotal.set(costofmeal)
        Total.set(OverAllCost)
        cost.set(costofmeal)
        Tax.set(PaidTax)
        Subtotal.set(costofmeal)
        Total.set(OverAllCost)
        MsgBox = messagebox.askquestion ('Paid or not ','Got Paid',icon = 'warning')
        if MsgBox == 'yes':
            today = date.today()
        if Totalcost>0:
            a='insert into bill values({},"{}","{}")'.format(x,math.ceil(Totalcost+PayTax),today)
            cur.execute(a)
            con.commit()  
        else:
            m='Please \n Enter minimum 1 Quantity'
            messagebox.showinfo('Warning',m)
    
        
    '''    IDK THE STRUCTURE OF TABLE - BILL - WHICH HAS NEVER BEEN CREATED
    def call():
        a='select * from bill'
        cur.execute(a)
        result=cur.fetchall()
        for i in result:
            print(i)
        t = date.today()
        t=str(t)
        sale='select sum(total) from bill where billdate="{}"'.format(t)
        cur.execute(sale)
        
        result=cur.fetchall()
        
        for i in result:
            for j in i:
                pass
        return(j)'''
    
    
    
    def qexit():
        #messagebox.showinfo("Today's Sale", str(call()))
        root.destroy()      
        
    
    def reset():
        rand.set("")
        Fries.set("")
        Largefries.set("")
        Burger.set("")
        Filet.set("")
        Subtotal.set("")
        Total.set("")
        Drinks.set("")
        Tax.set("")
        cost.set("")
        Cheese_burger.set("")
    
           
    def price():
        roo = Toplevel()
        roo.geometry("400x420+0+0")
        roo.title("Price List")
        qry='create table if not exists PL(FF float,Lunch float,Burger float,pizza float,CB float,drinks float)'
        cur.execute(qry)
        con.commit()
        cur.execute('select * from pl')
        q=cur.fetchall()
        if q==[]:
            cur.execute('insert into pl values(0.0,0.0,0.0,0.0,0.0,0.0)')
            con.commit()
        qry='select FF from PL'
        cur.execute(qry)
        p=cur.fetchone()
        a=p[0]
        
        qry='select lunch from PL'
        cur.execute(qry)
        q=cur.fetchone()
        b=q[0]
    
        qry='select burger from PL'
        cur.execute(qry)
        r=cur.fetchone()
        c=r[0]
    
        qry='select pizza from PL'
        cur.execute(qry)
        s=cur.fetchone()
        d=s[0]
    
        qry='select cb from PL'
        cur.execute(qry)
        t=cur.fetchone()
        e=t[0]
    
        qry='select drinks from PL'
        cur.execute(qry)
        u=cur.fetchone()
        f=u[0]
        
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
        lblinfo.grid(row=0, column=2)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
        lblinfo.grid(row=0, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="French Fries", fg="steel blue", anchor=W)
        lblinfo.grid(row=1, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text=str(a), fg="steel blue", anchor=W)
        lblinfo.grid(row=1, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch ", fg="steel blue", anchor=W)
        lblinfo.grid(row=2, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text=str(b), fg="steel blue", anchor=W)
        lblinfo.grid(row=2, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger ", fg="steel blue", anchor=W)
        lblinfo.grid(row=3, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text=str(c), fg="steel blue", anchor=W)
        lblinfo.grid(row=3, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza ", fg="steel blue", anchor=W)
        lblinfo.grid(row=4, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text=str(d), fg="steel blue", anchor=W)
        lblinfo.grid(row=4, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
        lblinfo.grid(row=5, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text=str(e), fg="steel blue", anchor=W)
        lblinfo.grid(row=5, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
        lblinfo.grid(row=6, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text=str(f), fg="steel blue", anchor=W)
        lblinfo.grid(row=6, column=3)
    
    
    #------------------TIME--------------
    localtime=time.asctime(time.localtime(time.time()))
    #-----------------INFO TOP------------
    root = Tk()
    root.geometry("890x580")
    root.title("CANTEEN BILLING SYSTEM")
    Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
    Tops.pack(side=TOP)
    f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
    f1.pack(side=LEFT)
    f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
    f2.pack(side=RIGHT)
    btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="red",command=price)
    btnprice.grid(row=8, column=0)
    lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="CANTEEN BILLING SYSTEM",fg="Black",bd=10,anchor='w')
    lblinfo.grid(row=0,column=0)
    lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
    lblinfo.grid(row=1,column=0)
    #-------------------BILL PAGE LOOK-----------------
    rand = StringVar()
    Fries = StringVar()
    Largefries = StringVar()
    Burger = StringVar()
    Filet = StringVar()
    Subtotal = StringVar()
    Total = StringVar()
    Drinks = StringVar()
    Tax = StringVar()
    cost = StringVar()
    Cheese_burger = StringVar()
    
    
    lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="brown",bd=20,anchor='w')
    lblreference.grid(row=0,column=0)
    txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=6,bg="yellow" ,justify='right')
    txtreference.grid(row=0,column=1)
    
    lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text=" French Fries ",fg="blue",bd=10,anchor='w')
    lblfries.grid(row=2,column=0)
    txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="green" ,justify='right')
    txtfries.grid(row=2,column=1)
    
    lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch ",fg="blue",bd=10,anchor='w')
    lblLargefries.grid(row=3,column=0)
    txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="green" ,justify='right')
    txtLargefries.grid(row=3,column=1)
    
    
    lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger ",fg="blue",bd=10,anchor='w')
    lblburger.grid(row=4,column=0)
    txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="green" ,justify='right')
    txtburger.grid(row=4,column=1)
    
    lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza ",fg="blue",bd=10,anchor='w')
    lblFilet.grid(row=5,column=0)
    txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="green" ,justify='right')
    txtFilet.grid(row=5,column=1)
    
    lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="blue",bd=10,anchor='w')
    lblCheese_burger.grid(row=6,column=0)
    txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="green" ,justify='right')
    txtCheese_burger.grid(row=6,column=1)
    
    #--------------------------------------------------------------------------------------
    lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="blue",bd=10,anchor='w')
    lblDrinks.grid(row=1,column=0)
    txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="green" ,justify='right')
    txtDrinks.grid(row=1,column=1)
    
    lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="black",bd=10,anchor='w')
    lblcost.grid(row=2,column=2)
    txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='right')
    txtcost.grid(row=2,column=3)
    
    
    
    lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bd=10,anchor='w')
    lblTax.grid(row=3,column=2)
    txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="white" ,justify='right')
    txtTax.grid(row=3,column=3)
    
    lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="black",bd=10,anchor='w')
    lblSubtotal.grid(row=4,column=2)
    txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="white" ,justify='right')
    txtSubtotal.grid(row= 4,column=3)
    
    lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="green",bd=10,anchor='w')
    lblTotal.grid(row=5,column=2)
    txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="grey" ,justify='right')
    txtTotal.grid(row=5,column=3)
    
    #-----------------------------------------buttons------------------------------------------
    lblTotal = Label(f1,text="---------------------",fg="black")
    lblTotal.grid(row=7,columnspan=3)
    
    btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="red",command=Ref)
    btnTotal.grid(row=8, column=1)
    
    btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="red",command=reset)
    btnreset.grid(row=8, column=2)
    
    btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=qexit)
    btnexit.grid(row=8, column=3)
    root.mainloop()
#_________NAvigation console_________
def main_page():
    def bye():
        main.destroy()
    main=Tk()
    main['bg']='coral'
    main.geometry('240x220')
    main.title('Main_Menu_Console')
    Label(main,text='Main Menu',font='calibre 12',fg='#ff3146',width=10,height=1,bg='#C7F0DC').pack(anchor='center',padx=10,pady=10)
    Button(main,text='Bill_Items',height=2,width=12,command=Bill_me).pack(anchor='center',padx=10,pady=10)
    Button(main,text='Update Prices',height=2,width=12,command=update_cost).pack(anchor='center',padx=10,pady=10)
    Button(main,text='Exit_console',height=2,width=12,bg='Black',fg='white',command=bye).pack(anchor='center',padx=10,pady=10)
    main.mainloop()
#________LOGIN FORMALITIES_______
def new_user():
    def create():
        q=u.get()
        p=v.get()
        m='insert into Login values({},{})'
        a=m.format('\''+q+'\'',p)
        if q=='' or p=='':
            messagebox.showerror("Input logic error", "Enter all feilds")
        else:
            cur.execute(a)
            con.commit()
            messagebox.showinfo("Success",'New user created-Re-run programe')
            r.destroy()
    def bye():
        new.destroy()
    
    new=Toplevel()
    new.title('New_user registration')
    new.geometry('350x200')
    Label(new,text='NEW USER REGISTRATION',font='Times 12 bold').grid(row=1,column=1,columnspan=2,padx=5,pady=5)
    Label(new,text='Enter the User_name',font='Monotype_Corsiva 12 bold').grid(row=2,column=1,padx=5,pady=5)
    Label(new,text='Enter password',font='Monotype_Corsiva 12 bold').grid(row=3,column=1,padx=5,pady=5)
    u=Entry(new)
    u.grid(row=2,column=2,padx=5,pady=5)
    v=Entry(new)
    v.grid(row=3,column=2,padx=5,pady=5)
    Button(new,text='Create user',font='Broadway 10 italic',command=create).grid(row=4,column=1,columnspan=2,padx=5,pady=5)
def submitact():
    def logintodb(user, passw):
        def log_108():
            r.destroy()
            main_page()
            return
        try:
            qry = "select * from login"
            cur.execute(qry)
            myresult = cur.fetchall()
            if str(user)=='panda' and int(passw)==0000:   #Emergency log_in option
                q=int(random.random()*1000000)
                messagebox.showinfo("Emergency_Login", "Sucessfully_Logged_in-Access.Code=x0x"+str(q))
                log_108()
            else:
                for x in myresult:
                    if x[0]==user and x[1]==passw:
                        messagebox.showinfo("Login", "Sucessfull")
                        r.destroy()
                        main_page()
                        return
                else:
                    messagebox.showinfo("Try Again!!!!", "Unsucessfull")
                    sys.exit()
                    r.destroy()
        except:
            r.destroy()
            sys.exit()
    user = Username.get()
    passw = password.get()
    logintodb(user, passw)

def bye():
    r.destroy()
    

r = Tk()
r.geometry("300x300")
r.title("Canteen Login Page")
r['bg']='pink'
lblfrstrow = Label(r, text ="Username -")
lblfrstrow.grid(row=1,column=1,padx=5,pady=5)
Username = Entry(r, width = 35)
Username.grid(row=1,column=2,padx=5,pady=5)
lblsecrow =Label(r, text ="Password -")
lblsecrow.grid(row=2,column=1,padx=5,pady=5)
password = Entry(r, width = 35)
password.grid(row=2,column=2,padx=5,pady=5)
submitbtn = Button(r, text ="Login",bg ='yellow', command = submitact)
submitbtn.grid(row=3,column=1,columnspan=2,padx=5,pady=5)
Button(r,text='EXIT',command=bye).grid(row=4,column=1,columnspan=2,padx=5,pady=5)
Button(r,text='Create new',command=new_user).grid(row=3,column=2,columnspan=2,padx=25,pady=5)
r.mainloop()
