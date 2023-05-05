from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql 

def clear():
    admin_name.delete(0,END)
    mdp.delete(0,END)
    confirm_mdp.delete(0,END)


#REDIRECTION VERS LA PAGE DE CONNEXION (LOGIN)
def connexion():
    signup_window.destroy() #quitter la page de creation avant de rediriger vers celle de cnx
    import connexion
    
  
#VISIBILITE DU LABEL USER  
def admin_enter(event):  #event hide the label whe cursor on 
    if admin_name.get()=='Username':
        admin_name.delete(0,END)
def admin_leave(event):  #show the label when cursor of
    if admin_name.get()=='':
        admin_name.insert(0,'Username')
        


#VISIBILITE DU LABEL PASSWD
def mdp_enter(event):  #event hide the label whe cursor on 
    if mdp.get()=='Password':
        mdp.delete(0,END)
def mdp_leave(event):  #show the label when cursor of
    if mdp.get()=='':
        mdp.insert(0,'Password')
        


#VISIBILITE DU LABEL CONFIRM PASSWD
def confirm_mdp_enter(event):  #event hide the label whe cursor on 
    if confirm_mdp.get()=='Confirmpassword':
        confirm_mdp.delete(0,END)
def confirm_mdp_leave(event):  #show the label when cursor of
    if confirm_mdp.get()=='':
        confirm_mdp.insert(0,'Confirmpassword')



#VISIBILITE DU MOT DE PAsSE ****
def hide():
    mdp.config(show='*')
    eyeButton.config(command=show)
def show():
    mdp.config(show='')
    eyeButton.config(command=hide)


#VISIBILITE CONFIRMATION DU PASSE ****
def hide2():
    confirm_mdp.config(show='*')
    eyeButton.config(command=show2)   
def show2():
    confirm_mdp.config(show='')
    eyeButton.config(command=hide2)


#LIAISON PYTHON ET BASE DE DONNEES MYSQL
def signup_db():
    Username=admin_name.get()
    Password=mdp.get()
    Confirmpassword=confirm_mdp.get()

    if Password!=Confirmpassword:
            messagebox.showerror('ERREUR','Verifier la confirmation de votre mot de passe')
    else:
        try:
            con= pymysql.connect(host='localhost',user='root',password='123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('ERREUR',"erreue de connexion ")
            return
        
    try:
        query='create database projet'
        mycursor.execute(query)
        query='use projet'
        mycursor.execute(query)
        query='create table Utilisateur(idUtilisateur int NOT NULL AUTO_INCREMENT primary key,nomUtilisateur varchar(20) NOT NULL ,mdpUtilisateur varchar(20) NOT NULL)'
        mycursor.execute(query)
        query='create table Produits (numSerie int NOT NULL primary key,nomProduit varchar(30) NOT NULL,descProduit varchar(300),prixU double,qntProduit int,seuilAlerteProduit int,date_entree date,date_sortie date,imageProduit longblob)'
        mycursor.execute(query)
    except:
        mycursor.execute('use projet')
        
    query='insert into Utilisateur(nomUtilisateur,mdpUtilisateur) values(%s,%s)'
    mycursor.execute(query,(admin_name.get(),mdp.get()))
    con.commit()
    con.close()
    messagebox.showinfo('success','felicitations votre compte a bien été cree')
    clear()
    
 #FORMULAIRE SIGN UP   
signup_window=Tk()
signup_window.title('Sign Up Page')
signup_window.geometry('990x660+50+50')
signup_window.resizable(0,0)



img=ImageTk.PhotoImage(Image.open("ccc.PNG"))
label=Label(signup_window,image=img,width=450,height=400,bg='white')
label.pack()
label.place(x=5,y=110)

#BORDERLINE
border_frame1 = Frame(signup_window, highlightbackground="DodgerBlue4", bg=('LightSkyBlue2'),highlightthickness=5,width=400, height=400, bd= 0)
border_frame1.pack()
border_frame1.place(x=500,y=100)


#HEARDER
HEADER=Label(signup_window,text='Sign Up',font=('Micrososft Yahei UI Light',23,'bold'),bg='LightSkyBlue2',fg='DodgerBlue4' )
HEADER.pack()
HEADER.place(x=637,y=120)

#USER INPUT
admin_name=Entry(signup_window,width=25,font=('Micrososft Yahei UI Light',11),bd=0)
admin_name.place(x=580,y=200) 
admin_name.insert(0,'Username')
admin_name.bind('<FocusIn>',admin_enter)
admin_name.bind('<FocusOut>',admin_leave)

frame1=Frame(signup_window,width=200,height=5,bg='DodgerBlue4')
frame1.place(x=580,y=222)



#PSWD INPUT
mdp=Entry(signup_window,width=25,font=('Micrososft Yahei UI Light',11),bd=0)
mdp.place(x=580,y=260) 
mdp.insert(0,'Password')
mdp.bind('<FocusIn>',mdp_enter)
mdp.bind('<FocusOut>',mdp_leave)

frame2=Frame(signup_window,width=200,height=5,bg='DodgerBlue4')
frame2.place(x=580,y=282)
eyeButton=Button(signup_window,text='hide pswd',bd=0,bg='DodgerBlue4',cursor='hand2',command=hide)
eyeButton.place(x=800,y=260)



#CONFIRM PSWD INPUT
confirm_mdp=Entry(signup_window,width=25,font=('Micrososft Yahei UI Light',11),bd=0)
confirm_mdp.place(x=580,y=320) 
confirm_mdp.insert(0,'Confirmpassword')
confirm_mdp.bind('<FocusIn>',confirm_mdp_enter)
confirm_mdp.bind('<FocusOut>',confirm_mdp_leave)

frame2=Frame(signup_window,width=200,height=5,bg='DodgerBlue4')
frame2.place(x=580,y=342)
eyeButton=Button(signup_window,text='hide pswd',bd=0,bg='DodgerBlue4',cursor='hand2',command=hide2)
eyeButton.place(x=800,y=320)



#SIGN UP BUTTON 
signup_buton=Button(signup_window,text='Create Account',font=('Micrososft Yahei UI Light',16,'bold'),command=signup_db,fg='black',bg='DodgerBlue4',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=19)
signup_buton.place(x=578,y=360)



#OR ALREADY HAVE AN ACC
already_buton=Button(signup_window,text='Already Have An Account?',font=('Micrososft Yahei UI Light',9,'bold'),command=connexion,bg='LightSkyBlue2',fg='DodgerBlue4',cursor='hand2',bd=0)
already_buton.place(x=583,y=400)


signup_window=mainloop()