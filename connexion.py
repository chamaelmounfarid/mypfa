from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql 

def login():
    a=admin_name.get()
    m=mdp.get()
    if m=='' or a=='':
        messagebox.showerror('ERREUR','Champs vides')
    else:
        try:
            con= pymysql.connect(host='localhost',user='root',password='123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('ERREUR','Echec de connexion')
            return
        query='use projet'
        mycursor.execute(query)
        query='select * from Utilisateur where nomUtilisateur=%s and mdpUtilisateur=%s'#requete mysql
        mycursor.execute(query,(admin_name.get(),mdp.get()))
        row=mycursor.fetchone() #permet de rechercher la 1ere ligne de la table sql(utilisateur)
        if row==None:
            messagebox.showerror('ERREUR','Admin introuvable,verifierle nom ou mot de passe')
        else:
            login_window.destroy() #quitter la page de creation avant de rediriger vers celle de creation acc
            import menu
        

#REDIRECTION VERS LA PAGE SIGN UP
def creation():
    login_window.destroy() #quitter la page de creation avant de rediriger vers celle de creation acc
    import creation


#VISIBILITE DU MOT DE PASSE ****
def hide():
    mdp.config(show='*')
    eyeButton.config(command=show) 
def show():
    mdp.config(show='')
    eyeButton.config(command=hide)
    
      
#VISIBILITE DU LABEL USER
def admin_enter(event):  #hide the label when cursor on 
    if admin_name.get()=='Enter username':
        admin_name.delete(0,END)
def admin_leave(event):  #show the label when cursor of
    if admin_name.get()=='':
        admin_name.insert(0,'Enter username')


#VISIBILITE DU LABEL PASSWD
def mdp_enter(event):  #event hide the label whe cursor on 
    if mdp.get()=='Enter password':
        mdp.delete(0,END)
def mdp_leave(event):  #show the label when cursor of
    if mdp.get()=='':
        mdp.insert(0,'Enter username')

login_window=Tk()

login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('LOGIN PAGE')

img=ImageTk.PhotoImage(Image.open("ccc.PNG"))
label=Label(login_window,image=img,width=450,height=400)
label.pack()
label.place(x=5,y=110)



#BORDERLINE
border_frame1 = Frame(login_window, highlightbackground="DodgerBlue4", bg=('LightSkyBlue2'),highlightthickness=5,width=400, height=400, bd= 0)
border_frame1.pack()
border_frame1.place(x=500,y=100)


#GRAND TITRE
HEADER=Label(login_window,text='Login',font=('Micrososft Yahei UI Light',23,'bold'),bg='LightSkyBlue2',fg='DodgerBlue4' )
HEADER.pack()
HEADER.place(x=637,y=120)


#USER INPUT
admin_name=Entry(login_window,width=25,font=('Micrososft Yahei UI Light',11),bd=0)
admin_name.place(x=580,y=200) 
admin_name.insert(0,'Enter username')
admin_name.bind('<FocusIn>',admin_enter)
admin_name.bind('<FocusOut>',admin_leave)

frame1=Frame(login_window,width=200,height=5,bg='DodgerBlue4')
frame1.place(x=580,y=222)



#PSWD INPUT
mdp=Entry(login_window,width=25,font=('Micrososft Yahei UI Light',11),bd=0)
mdp.place(x=580,y=260) 
mdp.insert(0,'Enter password')
mdp.bind('<FocusIn>',mdp_enter)
mdp.bind('<FocusOut>',mdp_leave)

frame2=Frame(login_window,width=200,height=5,bg='DodgerBlue4')
frame2.place(x=580,y=282)
mdp.bind(hide)
eyeButton=Button(login_window,text='hide pswd',bd=0,bg='DodgerBlue4',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)



#LOGIN BUTTON 
login_buton=Button(login_window,text='Login',font=('Micrososft Yahei UI Light',16,'bold'),fg='black',bg='DodgerBlue4',activeforeground='white',activebackground='LightSkyBlue2',cursor='hand2',bd=0,width=19,command=login)
login_buton.place(x=578,y=350)



#OPTION CREATION DE COMPTE(SIGN UP)
newacc_buton=Button(login_window,text='Dont have an account?',font=('Micrososft Yahei UI Light',9,'bold'),command=creation,bg='LightSkyBlue2',fg='DodgerBlue4',cursor='hand2',bd=0)
newacc_buton.place(x=583,y=400)


login_window.mainloop()  