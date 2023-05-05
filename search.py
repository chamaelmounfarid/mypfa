from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql 

def add():
    search_window.destroy() #quitter la page MENU avant de rediriger vers ADD
    import add
def deleete():
    search_window.destroy() #quitter la page MENU avant de rediriger vers DELETE
    import delete
def update():
    search_window.destroy() #quitter la page MENU avant de rediriger vers DELETE
    import update


#REDIRECTION 
def menu():
    search_window.destroy() #quitter la page ADD avant de rediriger vers MENU
    import menu

def reset():
     e1.delete(0,END)
     e2.delete(0,END)
     e3.delete(0,END)
     e4.delete(0,END)
     e5.delete(0,END)
     e6.delete(0,END)
     e7.delete(0,END)
     e8.delete(0,END)
     e9.delete(0,END)
    
    
def search():
    
    global myresult
    numserie=e1.get()
    nomProduit=e2.get()
    description=e3.get()
    prixUnitaire=e4.get()
    quantite=e5.get()
    seuilAlerte=e6.get()
    dde=e7.get()
    dds=e8.get()
    pImage=e9.get()
    

    con= pymysql.connect(host='localhost',user='root',password='123')
    mycursor=con.cursor()
    mycursor.execute('use projet')
    
    try:
        if e4.get()=='' and e5.get()=='' and e8.get()=='':
            query='select * from produits where nomProduit=%s  '
            mycursor.execute(query,(e2.get()))
        elif e2.get()=='' and e5.get()=='' and e8.get()=='':
            query='select * from produits where prixU=%s  '
            mycursor.execute(query,(e4.get()))
        elif e2.get()=='' and e4.get()=='' and e8.get()=='':
            query='select * from produits where qntProduit=%s  '
            mycursor.execute(query,(e5.get()))
        elif e2.get()=='' and e4.get()=='' and e5.get()=='':
            query='select * from produits where date_sortiet=%s  '
            mycursor.execute(query,(e8.get()))
            
    
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
        e1.delete(0,END)
        e1.insert(END,x[0])
        e2.delete(0,END)
        e2.insert(END,x[1])
        e3.delete(0,END)
        e3.insert(END,x[2])
        e4.delete(0,END)
        e4.insert(END,x[3])
        e5.delete(0,END)
        e5.insert(END,x[4])
        e6.delete(0,END)
        e6.insert(END,x[5])
        e7.delete(0,END)
        e7.insert(END,x[6])
        e8.delete(0,END)
        e8.insert(END,x[7])
        e9.delete(0,END)
        e9.insert(END,x[8])
        
        
            
    except Exception as e:
       print(e)
       con.rollback()
       con.close()

search_window=Tk()
search_window.title('Sportswear Stock Management')
search_window.geometry('990x660+50+50')
search_window.resizable(0,0)



#BORDERLINE
border_frame1 = Frame(search_window, highlightbackground="DodgerBlue4", bg=('LightSkyBlue2'),highlightthickness=5,width=800, height=500, bd= 0)
border_frame1.pack()
border_frame1.place(x=90,y=90)

#HEARDER
HEADER=Label(search_window,text='Recherche',font=('Micrososft Yahei UI Light',23,'bold'),bg='LightSkyBlue2',fg='DodgerBlue4' )
HEADER.pack()
HEADER.place(x=380,y=120)



label_numserie=Label(search_window,text='Numero de série :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_numserie.place(x=120,y=260)
e1=Entry(search_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
e1.place(x=120,y=300) 



label_nomP=Label(search_window,text='Nom produit :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_nomP.place(x=120,y=330)
e2=Entry(search_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
e2.place(x=120,y=370) 


label_description=Label(search_window,text='Description :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_description.place(x=120,y=400)
e3=Entry(search_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
e3.place(x=120,y=440) 

label_prixU=Label(search_window,text='Prix unitaire :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_prixU.place(x=120,y=470)
e4=Entry(search_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
e4.place(x=120,y=510) 

label_img=Label(search_window,text='Image :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_img.place(x=400,y=470)
e9=Entry(search_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
e9.place(x=400,y=510) 


###############################################""


label_qnt=Label(search_window,text='Quantité :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_qnt.place(x=700,y=260)
e5=Entry(search_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
e5.place(x=700,y=300) 



label_seuil=Label(search_window,text='Seuil alerte :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_seuil.place(x=700,y=330)
e6=Entry(search_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
e6.place(x=700,y=370) 


label_dde=Label(search_window,text='Date entrée :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_dde.place(x=700,y=400)
e7=Entry(search_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
e7.place(x=700,y=440) 

label_dds=Label(search_window,text='Date sortie :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_dds.place(x=700,y=470)
e8=Entry(search_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
e8.place(x=700,y=510) 

menu_buton=Button(search_window,text='<= Menu',font=('Micrososft Yahei UI Light',8,'bold'),command=menu,fg='DodgerBlue4',bg='LightSkyBlue2',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
menu_buton.place(x=120,y=110)

ADD_buton=Button(search_window,text='   <= Ajouter',font=('Micrososft Yahei UI Light',8,'bold'),command=add,fg='DodgerBlue4',bg='LightSkyBlue2',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
ADD_buton.place(x=120,y=125)

DEL_buton=Button(search_window,text='        <= Supprimer',font=('Micrososft Yahei UI Light',8,'bold'),command=deleete,fg='DodgerBlue4',bg='LightSkyBlue2',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
DEL_buton.place(x=120,y=140)

UP_buton=Button(search_window,text='   <= Modifier',font=('Micrososft Yahei UI Light',8,'bold'),command=update,fg='DodgerBlue4',bg='LightSkyBlue2',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
UP_buton.place(x=120,y=155)

search_buton=Button(search_window,text='recherche',font=('Micrososft Yahei UI Light',10,'bold'),command=search,fg='LightSkyBlue2',bg='DodgerBlue4',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
search_buton.place(x=790,y=110)

reset_buton=Button(search_window,text='reset',font=('Micrososft Yahei UI Light',10,'bold'),command=reset,fg='LightSkyBlue2',bg='DodgerBlue4',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
reset_buton.place(x=790,y=137)




search_window=mainloop()