from cProfile import label
from site import venv
from tkinter import*
from math import sqrt

ventana=Tk()
ventana.title("Ecuación de segundo grado ")
ventana.config(width=800,height=500)
ventana.resizable(0,0)
ventana.config(bg='slate blue')

a = StringVar()
b = StringVar()
c = StringVar()
discriminante=IntVar
x1=IntVar
x2=IntVar

def calcular ():
    discriminante= int(b.get()) * int(b.get()) - 4 * int(a.get()) * int(c.get())
    if discriminante < 0: 
        t_resultados.insert(INSERT,'La ecuación no tiene soluciones reales.')
    else:
        raiz = sqrt(discriminante)     
        x1 = (-int(b.get()) + raiz) / (2 * int(a.get()))     
        if discriminante != 0:          
            x2 = (-int(b.get()) - raiz) / (2 * int(a.get())) 
            t_resultados.insert(INSERT,'Las soluciones son '+str(x1) +' y' + str(x2)) 
        else:
            t_resultados.insert(INSERT,'La única solución es x =' + str(x1) )



frame_titulo=Frame(ventana)
frame_titulo.config(bg="sky blue", width=200, height=290)
frame_titulo.place(x=300,y=0)

frame_resultado=Frame(ventana)
frame_resultado.config(bg='purple3', width=800,height=250)
frame_resultado.place(x=0,y=290)


titulo = Label(frame_titulo, text="ECUACIONES DE")
titulo.config(bg="dark slate blue", fg="sky blue", font=("Arial", 16))
titulo.place(x=10,y=20)

titulo2=Label(frame_titulo,text='SEGUNDO GRADO')
titulo2.config(bg='dark slate blue', fg='sky blue',font=('Arial',16))
titulo2.place(x=2,y=60)

A=Label(ventana,text='A =')
A.config(bg='Mediumpurple1',fg='purple4',font=('Arial',25))
A.place(x=10,y=40)

B=Label(ventana,text='B =')
B.config(bg='Mediumpurple1',fg='purple4',font=('Arial',25))
B.place(x=10,y=100)

C=Label(ventana,text='C =')
C.config(bg='Mediumpurple1',fg='purple4',font=('Arial',25))
C.place(x=10,y=160)

entry_a = Entry(ventana, width=4, textvariable=a)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=70,y=43)

entry_b = Entry(ventana, width=4, textvariable=b)
entry_b.config(font=("Arial", 20), justify=CENTER)
entry_b.focus_set()
entry_b.place(x=70,y=103)

entry_c = Entry(ventana, width=4, textvariable=c)
entry_c.config(font=("Arial", 20), justify=CENTER)
entry_c.focus_set()
entry_c.place(x=70,y=163)


boton=Button(ventana,text='CALCULAR',command= calcular)
boton.config(bg='medium purple',fg= 'purple4',font=('Arial',25))
boton.place(x=550,y=90)

t_resultados = Text(frame_resultado, width=48, height=3)
t_resultados.config(bg="pink", fg="white", font=("Courier", 20))
t_resultados.place(x=10,y=50)


ventana.mainloop()