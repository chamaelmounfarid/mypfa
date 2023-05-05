from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql 

#REDIRECTION 
def menu():
    delete_window.destroy() #quitter la page ADD avant de rediriger vers MENU
    import menu
def add():
    delete_window.destroy() #quitter la page MENU avant de rediriger vers ADD
    import add
def search():
    delete_window.destroy() #quitter la page MENU avant de rediriger vers DELETE
    import search
def update():
    delete_window.destroy() #quitter la page MENU avant de rediriger vers DELETE
    import update
    
    
    
def sup():
    
    con= pymysql.connect(host='localhost',user='root',password='123')
    mycursor=con.cursor()
      
    mycursor.execute('use projet')
        
    query='delete from Produits where numSerie=%s'
    mycursor.execute(query,(numserie.get()))
    con.commit()
    con.close()
    messagebox.showinfo('success','Produit supprimé')
    clear()    


delete_window=Tk()
delete_window.title('Sportswear Stock Management')
delete_window.geometry('990x660+50+50')
delete_window.resizable(0,0)



#BORDERLINE
border_frame1 = Frame(delete_window, highlightbackground="DodgerBlue4", bg=('LightSkyBlue2'),highlightthickness=5,width=800, height=300, bd= 0)
border_frame1.pack()
border_frame1.place(x=100,y=100)

#HEARDER
HEADER=Label(delete_window,text='Supprimer produits',font=('Micrososft Yahei UI Light',23,'bold'),bg='LightSkyBlue2',fg='DodgerBlue4' )
HEADER.pack()
HEADER.place(x=380,y=120)

label_ns=Label(delete_window,text='Numero de serie :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_ns.place(x=200,y=260)
numserie=Entry(delete_window,width=40,font=('Micrososft Yahei UI Light',11),bd=0)
numserie.place(x=350,y=260) 



sup_buton=Button(delete_window,text='Supprimer',font=('Micrososft Yahei UI Light',16,'bold'),command=sup,fg='black',bg='DodgerBlue4',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
sup_buton.place(x=700,y=300)



menu_buton=Button(delete_window,text='<= Menu',font=('Micrososft Yahei UI Light',8,'bold'),command=menu,fg='DodgerBlue4',bg='LightSkyBlue2',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
menu_buton.place(x=120,y=110)

UP_buton=Button(delete_window,text='   <= Modifier',font=('Micrososft Yahei UI Light',8,'bold'),command=update,fg='DodgerBlue4',bg='LightSkyBlue2',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
UP_buton.place(x=120,y=125)

search_buton=Button(delete_window,text='   <=Recherche',font=('Micrososft Yahei UI Light',8,'bold'),command=search,fg='DodgerBlue4',bg='LightSkyBlue2',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
search_buton.place(x=120,y=140)

add_buton=Button(delete_window,text='   <=Suprimer',font=('Micrososft Yahei UI Light',8,'bold'),command=add,fg='DodgerBlue4',bg='LightSkyBlue2',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
add_buton.place(x=120,y=155)



delete_window=mainloop()