from tkinter import *
from tkinter import messagebox
import pymysql 


#REDIRECTION 
def menu():
    add_window.destroy() #quitter la page ADD avant de rediriger vers MENU
    import menu



#MYSQL INSERT INTO 
def add():
    
    con= pymysql.connect(host='localhost',user='root',password='123')
    mycursor=con.cursor()
    mycursor.execute('use projet')   
    query='insert into Produits (numSerie,nomProduit,descProduit,prixU,qntProduit,seuilAlerteProduit,date_entree,date_sortie,imageProduit) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    mycursor.execute(query,(numserie.get(),nomProduit.get(),description.get(),prixUnitaire.get(),quantite.get(),seuilAlerte.get(),dde.get(),dds.get(),pImage.get()))
    con.commit()
    con.close()
    messagebox.showinfo('success','Produit ajouté')
    clear()
    


add_window=Tk()
add_window.title('Stock Management Page')
add_window.geometry('990x660+50+50')
add_window.resizable(0,0)



#BORDERLINE
border_frame1 = Frame(add_window, highlightbackground="DodgerBlue4", bg=('LightSkyBlue2'),highlightthickness=5,width=800, height=480, bd= 0)
border_frame1.pack()
border_frame1.place(x=100,y=100)

#HEARDER
HEADER=Label(add_window,text='Ajouter produits',font=('Micrososft Yahei UI Light',23,'bold'),bg='LightSkyBlue2',fg='DodgerBlue4' )
HEADER.pack()
HEADER.place(x=380,y=120)



label_numserie=Label(add_window,text='Numero de série :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_numserie.place(x=120,y=180)
numserie=Entry(add_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
numserie.place(x=120,y=220) 



label_nomP=Label(add_window,text='Nom produit :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_nomP.place(x=120,y=250)
nomProduit=Entry(add_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
nomProduit.place(x=120,y=290) 


label_description=Label(add_window,text='Description :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_description.place(x=120,y=320)
description=Entry(add_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
description.place(x=120,y=360) 

label_prixU=Label(add_window,text='Prix unitaire :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_prixU.place(x=120,y=390)
prixUnitaire=Entry(add_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
prixUnitaire.place(x=120,y=430) 

label_img=Label(add_window,text='Image :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_img.place(x=120,y=460)
pImage=Entry(add_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
pImage.place(x=120,y=500) 


###############################################""


label_qnt=Label(add_window,text='Quantité :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_qnt.place(x=700,y=180)
quantite=Entry(add_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
quantite.place(x=700,y=220) 



label_seuil=Label(add_window,text='Seuil alerte :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_seuil.place(x=700,y=250)
seuilAlerte=Entry(add_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
seuilAlerte.place(x=700,y=290) 


label_dde=Label(add_window,text='Date entrée :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_dde.place(x=700,y=320)
dde=Entry(add_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
dde.place(x=700,y=360) 

label_dds=Label(add_window,text='Date sortie :',font=('Micrososft Yahei UI Light',11,'bold'),fg='DodgerBlue4',bg='LightSkyBlue2')
label_dds.place(x=700,y=390)
dds=Entry(add_window,width=20,font=('Micrososft Yahei UI Light',11),bd=0)
dds.place(x=700,y=430) 

add_buton=Button(add_window,text='Ajouter',font=('Micrososft Yahei UI Light',16,'bold'),command=add,fg='black',bg='DodgerBlue4',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
add_buton.place(x=700,y=490)

menu_buton=Button(add_window,text='<= Menu',font=('Micrososft Yahei UI Light',10,'bold'),command=menu,fg='DodgerBlue4',bg='LightSkyBlue2',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=10)
menu_buton.place(x=120,y=110)

add_window.mainloop()  