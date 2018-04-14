#!/usr/bin/env/python3

import tkinter as tk
from tkinter import ttk
from tkinter import*

from ttkthemes import themed_tk as tkt

import math
from math import *
import cmath

import matplotlib.pyplot as plt

import numpy as np
from numpy.linalg import inv

import subprocess

import sys

g=9.806652 # Gravitaional acceleration
RadToDeg = 180.0/3.14159
DegToRad = 3.14159/180.0
theta=45

#Theme chooser
global P
bg1="purple"
bg2="dimgrey"
bg3="black"
fg3="snow"
fg4="dimgrey"

themel=["arc","black","blue","aquativo","kroc","radiance","keramik","clearlooks","classic","winxpblue","plastik"]
bg1l=["gainsboro","grey","skyblue","#8313a6","orange","red","gainsboro","linen","dimgray","orange","silver"]
bg2l=["silver","dimgrey","midnightblue","#3056b3","orange","#d00001","gainsboro","linen","gainsboro","orange","lightgrey"]
fg3l=["dimgrey","dimgrey","midnightblue","#0976b3","orange","#d00001","dimgrey","brown", "grey","brown","black"]
Pl=["arc","black","blue","aquativo","kroc","radiance","keramik","clearlooks","plastik","kroc","plastik"]

theme="aquativo"
z=2
p="/Path/to/the/folder/Templates"
Px=p+"hw"
P="/home/eshita/Desktop/Eshita/12th/computer/python/GUI/hwplastik.png"

root1=tkt.ThemedTk()
root1.get_themes()
root1.set_theme("aquativo")

def g(z):
	root1.set_theme("black")
	global theme
	global bg1
	global bg2
	global bg3
	global fg3
	global fg4
	global P
	theme=themel[z]
	bg1=bg1l[z]
	bg2=bg2l[z]
	bg3="snow"
	fg3="dimgrey"
	fg4=fg3l[z]
	print ("fg4",fg4)
	P=Px+Pl[z]+".png"
	root1.set_theme(theme)
	root1.config(bg=bg3)
	l1.config(fg=fg3,bg=bg3)
	print(theme)

l1=Label(root1,text="""Click on any of the following to choose a Theme. Then, quit the window.
		Please wait a little after clicking submit""")
l1.grid()

b1=ttk.Button(root1,text="       black      ", command=lambda: g(1))
b1.grid()
b1=ttk.Button(root1,text="        arc          ", command=lambda: g(0))
b1.grid()
b1=ttk.Button(text="   aquativo  ", command=lambda: g(3))
b1.grid()
b1=ttk.Button(text="        blue       ", command=lambda: g(2))
b1.grid()
b1=ttk.Button(text="         kroc      ", command=lambda: g(4))
b1.grid()
b1=ttk.Button(text=" clearlooks  ", command=lambda: g(7))
b1.grid()
b1=ttk.Button(text="   radiance   ", command=lambda: g(5))
b1.grid()
b1=ttk.Button(text="    keramik   ", command=lambda: g(6))
b1.grid()
b1=ttk.Button(text="     classic      ", command=lambda: g(8))
b1.grid()
b1=ttk.Button(text="  winxpblue ", command=lambda: g(9))
b1.grid()
b1=ttk.Button(text="      plastik     ", command=lambda: g(10))
b1.grid()
bp=Button(root1, text="Submit",command=lambda: root1.destroy())
bp.grid()

print(theme)

root1.mainloop()

global constant1
constant1=0


class Main(tkt.ThemedTk,tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tkt.ThemedTk.__init__(self)   ##
        self.get_themes()             ##
        self.set_theme(theme)      ##
        photo=PhotoImage(file=P)

        f=Frame(width=500,height=30)
        f.place(height=50, width=0, x=0, y=0)
        f.pack(side="bottom",fill="both",expand=True)

        f.grid_rowconfigure(1)
        f.grid_columnconfigure(1)
        f.config(bg=bg1)

        f1=Frame(width=500,height=30)
        f1.place(height=50, width=0, x=0, y=0)
        f1.pack(side="bottom",fill="both",expand=True)


        f1.grid_rowconfigure(1)
        f1.grid_columnconfigure(1)
        f1.config(bg=bg2)

        q=ttk.Button(f1,text="Quit",command=lambda:sys.exit())
        q.pack()

        self.menu=Menu(self,background=fg4,foreground=bg3)
        self.config(menu=self.menu)
        self.submenu=Menu(self.menu,foreground=bg3,background=fg4)

        def g(z):
	        global theme
	        global bg1
	        global bg2
	        global bg3
	        global fg3
	        global P
	        theme=themel[z]
	        bg1=bg1l[z]
	        bg2=bg2l[z]
	        fg4=fg3l[z]
	        bg3="snow"
	        fg3="dimgrey"
	        P=Px+Pl[z]+".png"
	        f.config(bg=bg1)


	        f1.config(bg=bg2)
	        print(theme)
	        self.set_theme(theme)
	        f.config(bg=bg1)
	        f1.config(bg=bg2)
	        self.menu.config(background=fg4,foreground="white")
	        global constant1
	        constant1=1
	        print (constant1)


        self.submenu2=Menu(self.menu)

        self.menu.add_cascade(label="file",menu=self.submenu)
        self.menu.add_cascade(label="Choose Theme",menu=self.submenu2)

        b1=self.submenu2.add_command(label="     black     ", command=lambda: g(1))
        b1=self.submenu2.add_command(label="       arc     ", command=lambda: g(0))
        b1=self.submenu2.add_command(label="   aquativo  ", command=lambda: g(3))
        b1=self.submenu2.add_command(label="      blue     ", command=lambda: g(2))
        b1=self.submenu2.add_command(label="      kroc     ", command=lambda: g(4))
        b1=self.submenu2.add_command(label=" clearlooks  ", command=lambda: g(7))
        b1=self.submenu2.add_command(label="   radiance ", command=lambda: g(5))
        b1=self.submenu2.add_command(label="   keramik  ", command=lambda: g(6))
        b1=self.submenu2.add_command(label="     classic    ", command=lambda: g(8))
        b1=self.submenu2.add_command(label=" winxpblue ", command=lambda: g(9))
        b1=self.submenu2.add_command(label="    plastik    ", command=lambda: g(10))


        F1=tk.Frame(self)
        F1=tk.Frame(self,width=400,height=450)
        F1.place(height=7000, width=4000, x=100, y=100)
        F1.config()

        a=self.submenu.add_command(label="developer info",command=lambda:print("""
		****************************************************************************
		Developer: Eshita Shukla
		Date of creation: September 24, 2013
		Last modified: September 17, 2017
		****************************************************************************
		"""))
        b=self.submenu.add_command(label="contact us",command=lambda:print("""
		****************************************************************************
	       email: abcd@gmail.com
	       contact: @#$%^&*!^$

	    ****************************************************************************
	     """))
        c=self.submenu.add_command(label="Donate/ Hire",command=lambda:print("""
	    ***************************************************************************
	    email:abhbh@gmail.com
	     contact:  $@#$%^&*!^
	    ***************************************************************************
        """))

        F1.pack(fill="both",expand=True)

        F1.grid_rowconfigure(0,weight=1)
        F1.grid_columnconfigure(0,weight=1)
        F1.config()

        self.frames={}

        for F in (start1,start,P1,P2):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")

        for F in (start1,start,P1,P3):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")

        for F in (start1,start,P1,P4):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")


        for F in (start1,start,P1,P5,P6):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")

        for F in (start1,start,P1,P5,P7):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")

        for F in (start1,start,P1,P5,P8):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")

        for F in (start1,start,P1,P5,P9):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")

        for F in (start1,start,P1,P11,P13):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")

        for F in (start1,start,P1,P11,P12):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")


        for F in (start1,start,P1,P14,P16):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")

        for F in (start1,start,P1,P14,P15):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")

        for F in (start1,start,P17,P18,P19):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")

        for F in (start1,start,P17,P18,P20):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")


        self.show_frame(start1)

    def enter_show_frame(self,cont,event=None):
        frame=self.frames[cont]
        frame.tkraise()

    def show_frame(self,cont):

        frame=self.frames[cont]
        frame.config(bg=bg3)
        frame.tkraise()

print(constant1)

#Home Page

class start1(tk.Frame):                     # Home Page

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        photo=PhotoImage(file=P)
        label = Label(self,image =photo)
        label.image = photo # keep a reference!
        label.grid(row=0,column=0,columnspan=11,rowspan=11)



        print(constant1, " jj")


        b=ttk.Button(self,text="Start",command=lambda:controller.show_frame(start))
        b.grid(row=8,column=5)



class start(tk.Frame):                     # Home Page

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        x="""Mathematics"""
        label = Label(self,text=x,font="cmmi10 50",fg=fg3,bg=bg3)
        label.pack()

        y="""Mthematics is a powerful calculation tool

It is more than just a claculator.

Plot graphs and trajectories.
Perform complex calculations.
perform matrix operations.
Calculate the sum of a sequence or its nth term.
Solve equations.

"""
        label = Label(self,text=y,font="cmmi 20",fg=fg3,bg=bg3)
        label.pack()

        b=ttk.Button(self,text="Let's begin!!!",command=lambda:controller.show_frame(P1))
        b.pack()

class P1(tk.Frame):                     # Home Page

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)


        label=tk.Label(self,text="How can i help you?",font="forte 25",fg=fg3,bg=bg3)
        label.pack(pady=10,padx=100)

        l0=tk.Label(self,text="",font="forte 25",fg=fg3,bg=bg3)
        l0.pack()

        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 12))


        trajectory=ttk.Button(self,text="Find Trajectory",command=lambda:controller.show_frame(P3))
        trajectory.pack()

        calculator=ttk.Button(self,text="     Calculator     ",command=lambda:controller.show_frame(P2))
        calculator.pack()

        plotting=ttk.Button(self,text="     Plot graph     ",command=lambda:controller.show_frame(P4))
        plotting.pack()

        sequence=ttk.Button(self,text="     Sequence      ",command=lambda:controller.show_frame(P5))
        sequence.pack()

        matrix=ttk.Button(self,text="         Matrix        ",command=lambda:controller.show_frame(P11))
        matrix.pack()

        Rect_Pol =ttk.Button(self,text="      Complex       ",command=lambda:controller.show_frame(P16))
        Rect_Pol.pack()

        Solve_Eqn=ttk.Button(self,text="Solve Equation",command=lambda:controller.show_frame(P17))
        Solve_Eqn.pack()


        s=ttk.Button(self,text="       read info      ",command=lambda:controller.show_frame(start1))
        s.pack()


#Trajectory

class P3(tk.Frame,Main):                              #stationary

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        L=Label(self,text="Trajectory",font="forte 25",fg=fg3,bg=bg3)
        L.grid(row=0,column=1, columnspan=3)

        velocity=StringVar()
        distance=StringVar()
        l=Label(self,text="                        ",font="forte",bg=bg3)
        l.grid(row=2,column=0)


        L2=Label(self,text="Weapon's Muzzle Velocity",font="forte",fg=fg3,bg=bg3)
        L2.grid(row=2,column=1)

        L3=Label(self,text="Distance",font="forte",fg=fg3,bg=bg3)
        L3.grid(row=3,column=1)

        v_weapon= Entry(self,bd=10,textvariable=velocity)
        v_weapon.grid(row=2,column=2)

        distance_weapon= Entry(self,bd=10,textvariable=distance)
        distance_weapon.grid(row=3,column=2)


        def calculation():
            v_text=velocity.get()
            d_text=distance.get()
            try:
                vtext=int(v_text)
                dtext=int(d_text)

                velocity_stat(vtext,dtext)
            except:
                pass


        def velocity_stat(v,d):

            RadToDeg = 180.0/3.14159
            DegToRad = 3.14159/180.0
            theta=45
            R=(v**2)/g

            if R<d:
                l1=tk.Label(self,text="Max range of the weapon is less that the given distance.",font="forte",fg="white",bg=bg3)
                l2=tk.Label(self,text="Change the input or go to home page",font="forte",fg=fg3,bg=bg3)

                l1.grid(columnspan=3)
                l2.grid(columnspan=3)

            else:
                x11=(g*d)/(v**2)
                theta = (math.asin(x11)/2)
                l3=Label(self,text="angle [in degrees]",font="forte",fg=fg3,bg=bg3)
                l4=Label(self,text=str(theta*RadToDeg),font="forte",fg=fg3,bg=bg3)
                #angle=str(CalTheta(thi, u, v, d, step).pack()
                #l5=Label(self,text=str(theta*RadToDeg),font="forte",fg="white",bg="black")
                l3.grid(column=0,columnspan=2)
                l4.grid(column=0,columnspan=2)
                #l5.grid()


        def CalTheta(thi, u, v, d, step):                  #f2
            ffi = f(thi, u, v, d)
            if(ffi ==0):
                return thi*RadToDeg
            if(ffi>0):
                th=thi
                while(th<=45*DegToRad):
                    ff = f(th, u, v, d)
                    if(ff <0) :
                        return th*RadToDeg
                    th=th-step
            if(ffi<0):
                th=thi
                while(th<=45*DegToRad):
                    ff = f(th, u, v, d)
                    if(ff >0) :
                        return th*RadToDeg
                    th=th-step
            return thi*RadToDeg


        submit3=ttk.Button(self,text="submit",command=calculation)
        submit3.grid(column=1)

        home=ttk.Button(self,text="home",command=lambda:controller.show_frame(P1))
        home.grid(column=1)

#Calculator

class P2(tk.Frame):                              #calculator#

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        Expression=StringVar()

        L=Label(self,text="Calculator",font="forte 25",fg=fg3,bg=bg3)
        L.grid(row=0, column=1, columnspan=5)

        L2=Label(self,text="""To use complex no.s represent the imaginary term i with a 'j'""",font="forte",fg=fg3,bg=bg3)
        L2.grid(row=1,column=1,columnspan=10)
        L3=Label(self,text="""For trignometric calculations, use sin(),cos(),tan()
 constants: pi,e """,font="forte",fg=fg3,bg=bg3)
        L3.grid(row=2, column=1, columnspan=5)

        l2=Label(self, text="",bg=bg3)
        l2.grid()

        Exp=Entry(self,bd=10,textvariable=Expression,font="Ubuntu 15")
        Exp.grid(row=4,column=3)

        global A
        A=0
        self.xyz=8

        def Evaluating(A):
            P=3.14159
            e=2.71828
            print(A)
            def sin(a):
                return np.sin(radians(a))
            def cos(a):
                return np.cos(radians(a))
            def tan(a):
                return np.sin(radians(a))/np.cos(radians(a))
            Val=Expression.get()
            value=eval(Val)
            A=value
            Exp.delete(0,END)
            Exp.insert(END,str(value))
            l1=Label(self,text="value of the given expression is:",font="forte",fg=fg3,bg=bg3)
            l2=Label(self,text="               "+str(value)+"             ",font="forte",fg=fg3,bg=bg3)
            if self.xyz<=14:
                l1.grid(row=self.xyz)
                l2.grid(row=self.xyz+1)
                self.xyz=self.xyz+2
            else:
                l1.grid(row=self.xyz)
                l2.grid(row=self.xyz+1)
                self.xyz=self.xyz%14+6


        l1=Label(self,text="Enter the expression directly: ",font="forte",fg=fg3,bg=bg3)
        l1.grid(row=1,column=0)
        l2=Label(self, text="",bg=bg3)
        l2.grid()

        submit3=ttk.Button(self,text="submit",command=lambda:Evaluating(A))
        submit3.grid()

        home=ttk.Button(self,text="  home ",command=lambda:controller.show_frame(P1))
        home.grid()

#Plot Graph

class P4(tk.Frame):                              #plotting graph

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        xlist=[]
        ylist=[]

        Expression=StringVar()
        x_1=IntVar()
        x_2=StringVar()
        st=StringVar()
        co=StringVar()

        l0=Label(self,text="Plot a Graph",font="forte 25",fg=fg3,bg=bg3)
        l0.grid()

        l1=Label(self,text="Enter the expression (in terms of x only):",font="forte",fg=fg3,bg=bg3)
        l1.grid(row=1,column=0)

        Exp= Entry(self,bd=10,textvariable=Expression)
        Exp.grid(row=1,column=1)

        l2=Label(self,text="Enter the starting value:",font="forte",fg=fg3,bg=bg3)
        l2.grid(row=3,column=0)

        first=Entry(self,bd=10,textvariable=x_1)
        first.grid(row=3,column=1)

        l3=Label(self,text="Enter the ending value:",font="forte",fg=fg3,bg=bg3)
        l3.grid(row=4,column=0)

        second=Entry(self,bd=10,textvariable=x_2)
        second.grid(row=4,column=1)

        l0=Label(self,text="",font="forte",fg=fg3,bg=bg3)
        l0.grid(row=5,column=0)

        l3=Label(self,text="color(r/g/s):",font="forte",fg=fg3,bg=bg3)
        l3.grid(row=6,column=0)

        colo=Entry(self,bd=10,textvariable=co)
        colo.grid(row=6,column=1)

        l0=Label(self,text="",font="forte",fg=fg3,bg=bg3)
        l0.grid(row=7,column=0)

        l3=Label(self,text='''Graph Type:
("^"=Triangular)
("s"=square)
("o"=circle)
("--"=dottted)  ''',font="forte",fg=fg3,bg=bg3)
        l3.grid(row=8,column=0)

        sty=Entry(self,bd=10,textvariable=st)
        sty.grid(row=8,column=1)

        def making_lists():
            x1i=x_1.get()
            x2i=x_2.get()

            x1=int(x1i)
            x2=int(x2i)
            e=2.303

            d=(x1-x2)/20
            try:
                for i in range(x1*20,x2*20,1):
                    x=i
                    Val=Expression.get()
                    Val2=""
                    for i in range(len(Val)):
                        if Val[i]=="x":
                            Val2=Val2+"(x/20)"
                        else:
                            Val2=Val2+Val[i]
                    value=eval(Val2)
                    y=value
                    xlist.append(x/20)
                    ylist.append(y)

                return xlist
                return ylist
                return Val
            except:
                l3=Label(self,text="wrong input",font="forte",fg=fg3,bg=bg3)
                l3.grid(row=7,column=0)

        def plotting1():
            making_lists()
            c=colo.get()
            s=sty.get()
            M=c+s
            if len(xlist)!=0:
                plt.style.use("ggplot")
                plt.plot(xlist, ylist,M)
                plt.show()

        def plotting2():
            making_lists()
            c=colo.get()
            s=sty.get()
            M=c+s
            if len(xlist)!=0:
                plt.style.use('seaborn-deep')
                plt.plot(xlist, ylist,M)
                plt.show()

        l0=Label(self,text="",font="forte",fg=fg3,bg=bg3)
        l0.grid(row=7,column=0)

        submit1=ttk.Button(self,text="Plot: seaborn-deep",command=plotting2)
        submit1.grid()

        #submit2=ttk.Button(self,text="plot without marker",command=plotting("dark_background"))
        #submit2.grid()

        #submit3=ttk.Button(self,text="plot without marker",command=plotting("seaborn-notebook"))
        #submit3.grid()

        submit4=ttk.Button(self,text="       Plot: ggplot       ",command=plotting1)
        submit4.grid()

        home=ttk.Button(self,text="home",command=lambda:controller.show_frame(P1))
        home.grid()

#Sequence

class P5(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        rr=Label(self,text="Calculate the Sum or nth Term",font="forte 25",fg=fg3,bg=bg3)
        rr.pack()

        l=Label(self,text="What type of sequence is it?",font="forte 20",fg=fg3,bg=bg3)
        l.pack()

        lx=Label(self,text="",font="forte 25",fg=fg3,bg=bg3)
        lx.pack()


        AP=ttk.Button(self,text="       Arithematic Progression       ",command=lambda:controller.show_frame(P6))
        AP.pack()

        GP=ttk.Button(self,text="        Geometric Progression       ",command=lambda:controller.show_frame(P7))
        GP.pack()


        IGP=ttk.Button(self,text="Infinite Geometric Progression",command=lambda:controller.show_frame(P9))
        IGP.pack()

        oth=ttk.Button(self,text="                  other (custom)                 ",command=lambda:controller.show_frame(P8))
        oth.pack()

        lx=Label(self,text="",font="forte 25",fg=fg3,bg=bg3)
        lx.pack()

        home=ttk.Button(self,text="Home",command=lambda:controller.show_frame(P1))
        home.pack()

class P6(tk.Frame):                              #Arithmetic Progression

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        a_1=StringVar()
        n_1=StringVar()
        d_1=StringVar()

        l0=Label(self,text="Arithmatic Progression",font="forte 25",fg=fg3,bg=bg3)
        l0.grid(columnspan=2)

        l1=Label(self,text="first term",font="forte",fg=fg3,bg=bg3)
        l1.grid(row=1,column=0)

        a1=Entry(self,bd=10,textvariable=a_1)
        a1.grid(row=1,column=1)

        l2=Label(self,text="no. of terms",font="forte",fg=fg3,bg=bg3)
        l2.grid(row=2,column=0)

        n1=Entry(self,bd=10,textvariable=n_1)
        n1.grid(row=2,column=1)

        l3=Label(self,text="common difference",font="forte",fg=fg3,bg=bg3)
        l3.grid(row=3,column=0)

        d1=Entry(self,bd=10,textvariable=d_1)
        d1.grid(row=3,column=1)

        def calculation():
            ai=a1.get()
            ni=n1.get()
            di=d1.get()

            a=int(ai)
            n=int(ni)
            d=int(di)

            Sum=0
            L=[]
            for i in range(1,n+1):
                term=a+(i-1)*d
                L.append(term)
                Sum=Sum+term

            l4=Label(self,text="The series is:\n"+str(L),font="forte",fg=fg3,bg=bg3)
            l4.grid()
            l5=Label(self,text="The sum is:\n"+str(Sum),font="forte",fg=fg3,bg=bg3)
            l5.grid()

            return Sum


        submit4=ttk.Button(self,text="submit",command=calculation)
        submit4.grid(row=7,column=1)

        home=ttk.Button(self,text="home",command=lambda:controller.show_frame(P1))
        home.grid(row=8,column=1)

class P7(tk.Frame):                #geometric progression
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        a_1=StringVar()
        n_1=StringVar()
        r_1=StringVar()

        l0=Label(self,text="Geometric Progression",font="forte 25",fg=fg3,bg=bg3)
        l0.grid(columnspan=2)

        l1=Label(self,text="first term",font="forte",fg=fg3,bg=bg3)
        l1.grid(row=1,column=0)

        a1=Entry(self,bd=10,textvariable=a_1)
        a1.grid(row=1,column=1)

        l2=Label(self,text="no. of terms",font="forte",fg=fg3,bg=bg3)
        l2.grid(row=2,column=0)

        n1=Entry(self,bd=10,textvariable=n_1)
        n1.grid(row=2,column=1)

        l3=Label(self,text="common difference",font="forte",fg=fg3,bg=bg3)
        l3.grid(row=3,column=0)

        r1=Entry(self,bd=10,textvariable=r_1)
        r1.grid(row=3,column=1)

        def calculation():
            ai=a1.get()
            ni=n1.get()
            ri=r1.get()

            a=int(ai)
            n=int(ni)
            r=int(ri)

            Sum=0
            L=[]
            for i in range(0,n):
                term=a*(r**i)
                L.append(term)
                Sum=Sum+term

            l4=Label(self,text="The series is:\n"+str(L),font="forte",fg=fg3,bg=bg3)
            l4.grid(row=6,column=1)
            l5=Label(self,text="The sum is:\n"+str(Sum),font="forte",fg=fg3,bg=bg3)
            l5.grid(row=7,column=1)

            return Sum


        submit4=ttk.Button(self,text="submit",command=calculation)
        submit4.grid(column=1)

        home=ttk.Button(self,text="home",command=lambda:controller.show_frame(P1))
        home.grid(column=1)

class P8(tk.Frame):                       #other
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        n_1=StringVar()
        N_1=StringVar()

        l0=Label(self,text="Custom",font="forte 25",fg=fg3,bg=bg3)
        l0.grid()

        l2=Label(self,text="no. of terms",font="forte",fg=fg3,bg=bg3)
        l2.grid(row=2,column=0)

        n1=Entry(self,bd=10,textvariable=n_1)
        n1.grid(row=2,column=1)

        l3=Label(self,text="enter nth terms of the series(in terms of n)",font="forte",fg=fg3,bg=bg3)
        l3.grid(row=3,column=0)

        N1=Entry(self,bd=10,textvariable=N_1)
        N1.grid(row=3,column=1)

        def calculation():

            ni=n1.get()
            Ni=N1.get()

            nl=int(ni)

            Sum=0
            L=[]

            for i in range (1,nl+1):
                n=i
                term=eval(Ni)

                L.append(term)
                Sum=Sum+term

            l4=Label(self,text="The series is:\n"+str(L),font="forte",fg=fg3,bg=bg3)
            l4.grid(row=6,column=1)
            l5=Label(self,text="The sum is:\n"+str(Sum),font="forte",fg=fg3,bg=bg3)
            l5.grid(row=7,column=1)

            return Sum

        submit4=ttk.Button(self,text="Submit",command=calculation)
        submit4.grid(column=1)

        home=ttk.Button(self,text="Home",command=lambda:controller.show_frame(P1))
        home.grid(column=1)

class P9(tk.Frame):                # infinite geometric progression
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        a_1=StringVar()
        r_1=StringVar()

        l1=Label(self,text="first term",font="forte",fg=fg3,bg=bg3)
        l1.grid(row=1,column=0)

        a1=Entry(self,bd=10,textvariable=a_1)
        a1.grid(row=1,column=1)

        l3=Label(self,text="common ratio",font="forte",fg=fg3,bg=bg3)
        l3.grid(row=3,column=0)

        r1=Entry(self,bd=10,textvariable=r_1)
        r1.grid(row=3,column=1)

        def calculation():
            ai=a1.get()
            ri=r1.get()

            a=int(ai)
            r=float(ri)

            if r<1 and r>(-1):
                Sum=a/(1-r)
                l5=Label(self,text="The sum is:\n"+str(Sum),font="forte",fg=fg3,bg=bg3)
                l5.grid(row=7,column=1)
                return Sum

            else:
                l3=Label(self,text='''common ratio is more than infinity.
Thus,    Sum= INFINITY''',font="forte",fg=fg3,bg=bg3)
                l3.grid(row=4,column=0)
            home.__del__()

        submit4=ttk.Button(self,text="submit",command=calculation)
        submit4.grid(column=1)

        home=ttk.Button(self,text="home",command=lambda:controller.show_frame(P1))
        home.grid(column=1)

#Matrix

class P11(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        l1=Label(self,text="Matrix",font="forte 25",fg=fg3,bg=bg3)
        l1.pack()

        l0=Label(self,text="",font="forte 25",fg=fg3,bg=bg3)
        l0.pack()

        Multiply=ttk.Button(self,text="Multiply",command=lambda:controller.show_frame(P12))
        Multiply.pack()

        Inverse=ttk.Button(self,text="Inverse",command=lambda:controller.show_frame(P13))
        Inverse.pack()

        home=ttk.Button(self,text="Home",command=lambda:controller.show_frame(P1))
        home.pack()

class P12(tk.Frame):                       #Multiplication
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.x=10
        mat_1=StringVar()
        mat_2=StringVar()

        l1=Label(self,text="Matrix Multiplication (vector)",font="forte 1",fg=fg3,bg=bg3)
        l1.grid(row=1,column=2)

        l2=Label(self,text='''Seperate each row by a "  ;  " .
Seperate each element by a "  ,  " .

Esnclose everything in "  [  ]  "  . ''',font="forte",fg=fg3,bg=bg3)
        l2.grid(row=2,columnspan=3)



        l3=Label(self,text="Input 1st matrix",font="forte",fg=fg3,bg=bg3)
        l3.grid(row=3,column=0)

        mat1=Entry(self,bd=10,textvariable=mat_1,font="forte 30")
        mat1.grid(row=3,column=1,columnspan=2)

        l4=Label(self,text="Input 2nd matrix",font="forte",fg=fg3,bg=bg3)
        l4.grid(row=4,column=0)

        mat2=Entry(self,bd=10,textvariable=mat_2,font="forte 30")
        mat2.grid(row=4,column=1,columnspan=2)

        def Multiply():
            mati1=mat1.get()
            mati2=mat2.get()

            mat_x1=np.matrix(mati1)
            mat_x2=np.matrix(mati2)
            matx1=np.array(mat_x1)
            matx2=np.array(mat_x2)

            mat_multiply=np.matmul(matx1,matx2)

            l1=Label(self,text="Matrix:\n"+mati1,font="forte",fg=fg3,bg=bg3)
            l1.grid(row=self.x,column=0)

            l3=Label(self,text="Matrix:\n"+mati2,font="forte",fg=fg3,bg=bg3)
            l3.grid(row=self.x,column=1)


            l2=Label(self,text="Multiplication:\n"+str(mat_multiply),font="forte",fg=fg3,bg=bg3)
            l2.grid(row=self.x,column=2)

            self.x=self.x+1


        submit=ttk.Button(self,text="Submit",command=Multiply)
        submit.grid(column=1)

        lx=Label(self,text="",font="forte",fg=fg3,bg=bg3)
        lx.grid(column=1)

        back=ttk.Button(self,text="Back",command=lambda:controller.show_frame(P11))
        back.grid(column=1)


        home=ttk.Button(self,text="Home",command=lambda:controller.show_frame(P1))
        home.grid(column=1)


class P13(tk.Frame):                       #Inverse
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.x=6
        mat_1=StringVar()

        l1=Label(self,text="Matrix inverse",font="forte 1",fg=fg3,bg=bg3)
        l1.grid(row=1,column=2)

        l2=Label(self,text='''Seperate each row by a "  ;  " .
Seperate each element by a "  ,  " .

Esnclose everything in "  [  ]  "  . ''',font="forte",fg=fg3,bg=bg3)
        l2.grid(row=2,columnspan=3)



        l3=Label(self,text="Input matrix",font="forte",fg=fg3,bg=bg3)
        l3.grid(row=3,column=0)

        mat1=Entry(self,bd=10,textvariable=mat_1,font="forte 30")
        mat1.grid(row=3,column=1,columnspan=2)

        def Inverse():
            mati=mat1.get()

            mat_x=np.matrix(mati)
            mat=np.array(mat_x)

            mat_inverse=inv(mat)

            l1=Label(self,text="Matrix:       "+mati,font="forte",fg=fg3,bg=bg3)
            l1.grid(row=self.x,column=0)

            l3=Label(self,text="      ",font="forte",fg=fg3,bg=bg3)
            #l3.grid()


            l2=Label(self,text="Inverse:\n"+str(mat_inverse),font="forte",fg=fg3,bg=bg3)
            l2.grid(row=self.x,column=1)

            self.x=self.x+1


        submit=ttk.Button(self,text="Submit",command=Inverse)
        submit.grid(column=1)

        home=ttk.Button(self,text="Home",command=lambda:controller.show_frame(P1))
        home.grid(column=1)


#Complex

class P14(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        Rect_Pol =ttk.Button(self,text="Rectangular to Polar ",command=lambda:controller.show_frame(P16))
        Rect_Pol.pack()

        Pol_Rect =ttk.Button(self,text="Polar to Rectangular",command=lambda:controller.show_frame(P15))
        Pol_Rect.pack()

        Calc =ttk.Button(self,text="           Calculator            ",command=lambda:controller.show_frame(P2))
        Calc.pack()

        home=ttk.Button(self,text="Home",command=lambda:controller.show_frame(P1))
        home.pack()


class P15(tk.Frame):           # Polar to Rectangular
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        cosine=StringVar()
        sine=StringVar()

        l1=Label(self,text="Polar to Rectangular",font="forte 25",fg=fg3,bg=bg3)
        l1.grid(row=0,column=0)


        l1=Label(self,text="Input r",font="forte",fg=fg3,bg=bg3)
        l1.grid(row=1,column=0)

        r1=Entry(self,bd=10,textvariable=cosine)
        r1.grid(row=1,column=1,columnspan=2)

        l2=Label(self,text="Input theta(angle)",font="forte",fg=fg3,bg=bg3)
        l2.grid(row=2,column=0)

        th1=Entry(self,bd=10,textvariable=sine)
        th1.grid(row=2,column=1,columnspan=2)

        def pol_rect():
            ri=r1.get()
            thi=th1.get()

            r=eval(ri)
            th=eval(thi)

            c=complex(r,th)

           # Rect=cmath.rect(c)	#x=Rect[0]	#y=Rect[1]

            x=r*np.cos(radians(th))
            y=r*np.sin(radians(th))


            l1=Label(self,text="For complex(pol)= "+ri+"  ,  "+thi,font="forte",fg=fg3,bg=bg3)
            l1.grid()

            l2=Label(self,text="Polar form is:  x(cosine)="+str(x)+"  y(cosine)="+str(y),font="forte",fg=fg3,bg=bg3)
            l2.grid()

        submit=ttk.Button(self,text="Submit",command=pol_rect)
        submit.grid(column=1)

        back=ttk.Button(self,text="Back",command=lambda:controller.show_frame(P16))
        back.grid(column=1)

        home=ttk.Button(self,text="Home",command=lambda:controller.show_frame(P1))
        home.grid(column=1)


class P16(tk.Frame):               #Rectangular to polar
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        cosine=StringVar()
        sine=StringVar()

        l1=Label(self,text="Rectangular to Polar",font="forte 25",fg=fg3,bg=bg3)
        l1.grid(row=0,column=0)


        l1=Label(self,text="Input x(cosine)",font="forte",fg=fg3,bg=bg3)
        l1.grid(row=1,column=0)

        x1=Entry(self,bd=10,textvariable=cosine)
        x1.grid(row=1,column=1,columnspan=2)

        l2=Label(self,text="Input y(sine)",font="forte",fg=fg3,bg=bg3)
        l2.grid(row=2,column=0)

        y1=Entry(self,bd=10,textvariable=sine)
        y1.grid(row=2,column=1,columnspan=2)

        def rect_pol():

            xi=x1.get()
            yi=y1.get()

            x=eval(xi)
            y=eval(yi)

            c=complex(x,y)

            Pol=(cmath.polar(c))

            r=Pol[0]
            theta=Pol[1]

            l1=Label(self,text="For complex(rect)= "+xi+"+j"+yi,font="forte",fg=fg3,bg=bg3)
            l1.grid()

            l2=Label(self,text="Polar form is:  r="+str(r)+"  angle="+str(theta),font="forte",fg=fg3,bg=bg3)
            l2.grid()

        submit=ttk.Button(self,text="Submit",command=rect_pol)
        submit.grid(column=1)

        back=ttk.Button(self,text="Back",command=lambda:controller.show_frame(P14))
        back.grid(column=1)

        home=ttk.Button(self,text="Home",command=lambda:controller.show_frame(P1))
        home.grid(column=1)



#Solve Equations

class P17(tk.Frame):         #solve equations
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        rr=Label(self,text="Solve equation/s",font="forte 25",fg=fg3,bg=bg3)
        rr.pack()

        l=Label(self,text="How many variables does the equation have?",font="forte",fg=fg3,bg=bg3)
        l.pack()

        var_1=ttk.Button(self,text="1 variable (x)",command=lambda:controller.show_frame(P18))
        var_1.pack()

        home=ttk.Button(self,text="Home",command=lambda:controller.show_frame(P1))
        home.pack()


        '''var_2=ttk.Button(self,text="2 variables (x,y)",command=lambda:controller.show_frame(P7))
        var_2.pack()'''


class P18(tk.Frame):          #1 variable
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        rr=Label(self,text="1 variable",font="forte 25",fg=fg3,bg=bg3)
        rr.pack()

        Deg_2=ttk.Button(self,text="2 degree",command=lambda:controller.show_frame(P19))
        Deg_2.pack()

        Deg_3=ttk.Button(self,text="3 degree",command=lambda:controller.show_frame(P20))
        Deg_3.pack()

        rr=Label(self,text="",font="forte",fg=fg3,bg=bg3)
        rr.pack()

        back=ttk.Button(self,text="  Back ",command=lambda:controller.show_frame(P17))
        back.pack()

        home=ttk.Button(self,text=" Home ",command=lambda:controller.show_frame(P1))
        home.pack()

class P19(tk.Frame):          # 1 variable 2 degree
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        rr=Label(self,text="2 degree equation with 1 variable (x)",font="forte 25",fg=fg3,bg=bg3)
        rr.grid(row=0,column=0)

        a_1=StringVar()
        b_1=StringVar()
        c_1=StringVar()

        l1=Label(self,text="Coeff of x**2",font="forte",fg=fg3,bg=bg3)
        l1.grid(row=1,column=0)

        a1=Entry(self,bd=10,textvariable=a_1)
        a1.grid(row=1,column=1,columnspan=2)

        l2=Label(self,text="Coeff of x",font="forte",fg=fg3,bg=bg3)
        l2.grid(row=2,column=0)

        b1=Entry(self,bd=10,textvariable=b_1)
        b1.grid(row=2,column=1,columnspan=2)

        l3=Label(self,text="constant",font="forte",fg=fg3,bg=bg3)
        l3.grid(row=3,column=0)

        c1=Entry(self,bd=10,textvariable=c_1)
        c1.grid(row=3,column=1,columnspan=2)

        def roots():
            ai=a1.get()
            bi=b1.get()
            ci=c1.get()

            a=eval(ai)
            b=eval(bi)
            c=eval(ci)

            d = b**2-4*a*c # discriminant

            if d < 0:
                l4=Label(self,text="No solution",font="forte",fg=fg3,bg=bg3)
                l4.grid(row=6,column=0)

            elif d == 0:
                x = (-b+math.sqrt(b**2-4*a*c))/2*a
                l4=Label(self,text="One solution: "+str(x),font="forte",fg=fg3,bg=bg3)
                l4.grid(row=6,column=0)

            else:
                x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
                x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
                l4=Label(self,text="Two solutions:  x1= "+str(x1)+"x2= "+str(x2),font="forte",fg=fg3,bg=bg3)
                l4.grid(row=6,column=0)



        submit=ttk.Button(self,text="Submit",command=roots)
        submit.grid(column=1)

        back=ttk.Button(self,text="  Back  ",command=lambda:controller.show_frame(P16))
        back.grid(column=1)

        home=ttk.Button(self,text="Home",command=lambda:controller.show_frame(P1))
        home.grid(column=1)


'''     l2=Label(self,text="Input r",font="forte",fg="white",bg="black")
        l2.grid(row=0,column=0)

        r2=Entry(self,bd=10,textvariable=cosine)
        r2.grid(row=0,column=1,columnspan=2)                 '''


class P20(tk.Frame):          # 1 variable 3 degree
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        rr=Label(self,text="3 degree equation with 1 variable (x)",font="forte 25",fg=fg3,bg=bg3)
        rr.grid(row=0,column=0)

        a_1=IntVar()
        b_1=IntVar()
        c_1=IntVar()
        d_1=IntVar()

        l2=Label(self,text="a: ",font="forte",fg=fg3,bg=bg3)
        l2.grid(row=2,column=0)

        a1=Entry(self,bd=10,textvariable=a_1)
        a1.grid(row=2,column=1,columnspan=2)

        l3=Label(self,text="b: ",font="forte",fg=fg3,bg=bg3)
        l3.grid(row=3,column=0)

        b1=Entry(self,bd=10,textvariable=b_1)
        b1.grid(row=3,column=1,columnspan=2)

        l1=Label(self,text="c: ",font="forte",fg=fg3,bg=bg3)
        l1.grid(row=4,column=0)

        c1=Entry(self,bd=10,textvariable=c_1)
        c1.grid(row=4,column=1,columnspan=2)

        l4=Label(self,text="d: ",font="forte",fg=fg3,bg=bg3)
        l4.grid(row=5,column=0)

        d1=Entry(self,bd=10,textvariable=d_1)
        d1.grid(row=5,column=1,columnspan=2)

        def roots():
            ai=a1.get()
            bi=b1.get()
            ci=c1.get()
            di=d1.get()

            a=eval(ai)
            b=eval(bi)
            c=eval(ci)
            d=eval(di)

            '''p = -b/(3*a)
            q = p**3 + (b*c-3*a*d)/(6*a**2)
            r = c/(3*a)'''

            yi=18*a*b*c*d - 4*(b**3)*d + (b**2)*(c**2) - 4*a*(c**3) -27*(a**2)*(d**2)

            #x   = (q +   (q**2+ (r-p**2)**3 )**(1/2)  )**(1/3) + (q -  (q**2 + (r-p**2)**3 )**(1/2))**(1/3) + p

            y0= b**2-3*a*c
            y1=2*b**3-9*a*b*c+27*(a**2)*d

            if yi<0:
                yi=yi*(-1)

            x=((y1+yi**0.5)/2)**(1/3)
            l=Label(self,text=str(x))
            l.grid()

        submit=ttk.Button(self,text="Submit",command=roots)
        submit.grid(column=1)

        home=ttk.Button(self,text="Home",command=lambda:controller.show_frame(P1))
        home.grid(column=1)

# Create object
print(theme)
root=Main()
root.title("Mathematics")
colour=theme
def exit_function():
    # Put any cleanup here.
    sys.exit()
    root.destroy()

root.protocol('WM_DELETE_WINDOW', exit_function)


root.mainloop()
