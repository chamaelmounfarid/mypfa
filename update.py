from tkinter import *
from tkinter import messagebox
import pymysql 


#REDIRECTION 
def menu():
    update_window.destroy() #quitter la page ADD avant de rediriger vers MENU
    import menu
def deleete():
    update_window.destroy() #quitter la page MENU avant de rediriger vers DELETE
    import delete
def add():
    update_window.destroy() #quitter la page MENU avant de rediriger vers DELETE
    import add
def search():
    update_window.destroy() #quitter la page MENU avant de rediriger vers DELETE
    import search

def update():
        
    con= pymysql.connect(host='localhost',user='root',password='123')
    mycursor=con.cursor()
      
    mycursor.execute('use projet')

    query='update Produits set qntProduit=%s,prixU=%s where numSerie=%s'    
    mycursor.execute(query,(quantite.get(),prixUnitaire.get(),numSerie.get()))
    con.commit()
    con.close()
    messagebox.showinfo('success','Produit modifié')
    clear()  





update_window=Tk()
update_window.title('Sportswear Stock Management')
update_window.geometry('990x660+50+50')
update_window.resizable(0,0)



#BORDERLINE
border_frame1 = Frame(update_window, highlightbackground="DodgerBlue4", bg=('LightSkyBlue2'),highlightthickness=5,width=800, height=300, bd= 0)
border_frame1.pack()
border_frame1.place(x=100,y=100)

#HEARDER
HEADER=Label(update_window,text='Modifier produits',font=('Micrososft Yahei UI Light',23,'bold'),bg='LightSkyBlue2',fg='DodgerBlue4' )
HEADER.pack()
HEADER.place(x=380,y=120)

label_prixU=Label(update_window,text='Prix unitaire :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_prixU.place(x=120,y=180)
prixUnitaire=Entry(update_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
prixUnitaire.place(x=120,y=220) 

label_qnt=Label(update_window,text='Quantité :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_qnt.place(x=700,y=180)
quantite=Entry(update_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
quantite.place(x=700,y=220) 


label_numserie=Label(update_window,text='Numéro de série :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_numserie.place(x=500,y=290)
numSerie=Entry(update_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
numSerie.place(x=500,y=320) 



update_buton=Button(update_window,text='Modifier',font=('Micrososft Yahei UI Light',16,'bold'),command=update,fg='black',bg='DodgerBlue4',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
update_buton.place(x=700,y=300)

menu_buton=Button(update_window,text='<= Menu',font=('Micrososft Yahei UI Light',8,'bold'),command=menu,fg='DodgerBlue4',bg='LightSkyBlue2',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
menu_buton.place(x=120,y=110)

add_buton=Button(update_window,text='   <= Ajouter',font=('Micrososft Yahei UI Light',8,'bold'),command=add,fg='DodgerBlue4',bg='LightSkyBlue2',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
add_buton.place(x=120,y=125)

search_buton=Button(update_window,text='   <=Recherche',font=('Micrososft Yahei UI Light',8,'bold'),command=search,fg='DodgerBlue4',bg='LightSkyBlue2',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
search_buton.place(x=120,y=140)

DEL_buton=Button(update_window,text='   <=Suprimer',font=('Micrososft Yahei UI Light',8,'bold'),command=deleete,fg='DodgerBlue4',bg='LightSkyBlue2',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
DEL_buton.place(x=120,y=155)

update_window=mainloop()