from tkinter import *
from PIL import ImageTk,Image

def add():
    menu_window.destroy() #quitter la page MENU avant de rediriger vers ADD
    import add

def search():
    menu_window.destroy() #quitter la page MENU avant de rediriger vers SEARCH
    import search
    
def deleete():
    menu_window.destroy() #quitter la page MENU avant de rediriger vers DELETE
    import delete

def update():
    menu_window.destroy() #quitter la page MENU avant de rediriger vers DELETE
    import update




menu_window=Tk()
menu_window.title('Sportswear Stock Management')
menu_window.geometry('990x660+50+50')
menu_window.resizable(0,0)



img=ImageTk.PhotoImage(Image.open("ccc.PNG"))
label=Label(menu_window,image=img,width=450,height=400,bg='white')
label.pack()
label.place(x=5,y=110)

#BORDERLINE
border_frame1 = Frame(menu_window, highlightbackground="DodgerBlue4", bg=('LightSkyBlue2'),highlightthickness=5,width=400, height=400, bd= 0)
border_frame1.pack()
border_frame1.place(x=500,y=100)

#HEARDER
HEADER=Label(menu_window,text='Menu',font=('Micrososft Yahei UI Light',23,'bold'),bg='LightSkyBlue2',fg='DodgerBlue4' )
HEADER.pack()
HEADER.place(x=650,y=120)

ajout_buton=Button(menu_window,text='Ajouter produit',font=('Micrososft Yahei UI Light',16,'bold'),command=add,fg='black',bg='DodgerBlue4',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=19)
ajout_buton.place(x=580,y=222)

recherche_buton=Button(menu_window,text='Rechercher produit',font=('Micrososft Yahei UI Light',16,'bold'),command=search,fg='black',bg='DodgerBlue4',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=19)
recherche_buton.place(x=580,y=290)

supp_buton=Button(menu_window,text='Supprimer produit',font=('Micrososft Yahei UI Light',16,'bold'),command=deleete,fg='black',bg='DodgerBlue4',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=19)
supp_buton.place(x=578,y=360)

search_buton=Button(menu_window,text='Modifier produit',font=('Micrososft Yahei UI Light',16,'bold'),command=update,fg='black',bg='DodgerBlue4',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=19)
search_buton.place(x=578,y=430)

menu_window=mainloop()
