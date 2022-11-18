from tkinter import*
from tkinter import ttk 
from PIL import ImageTk 
from tkinter import messagebox

class Login_window:
    def __init__(self,root):
       self.root=root
       self.root.title('Login')
       self.root.geometry('1500x750+300+200')
       self.root.configure(bg='#fefbe9') 
      #  self.root.resizable(False,False)
       
       self.bg=ImageTk.PhotoImage(file="lpu.png")
       
       lbl_bg=Label(self.root,image=self.bg,bg="#fefbe9")
       lbl_bg.place(x=475,y=50)
       
 
       frame=Frame(self.root,bg="#fefbe9",width=350,height=350)
       frame.place(x=600,y=380)
    #    bms
       get_bms=Label(frame,text="Login",font=('cl',25,'bold'),fg="black",bg="#fefbe9")
       get_bms.place(x=125,y=0)

    # user name 
       username=lbl=Label(frame,text="Username  :",font=('Arial Narrow',25),fg="black",bg="#fefbe9")
       username.place(x=4,y=75)
       self.txtuser=Entry(frame,font=('Arial Narrow',22,'bold'),border=0,bg="#fefbe9")
       self.txtuser.place(x=200,y=75)
       Frame(frame,width=295,height=2,bg='black').place(x=200,y=110)
   # password
       password=lbl=Label(frame,text="Password  :",font=('Arial Narrow',25),fg="black",bg="#fefbe9")
       password.place(x=4,y=150)     
       
       self.txtpass=Entry(frame,font=('Arial Narrow',22,'bold'),border=0,bg="#fefbe9",show=".")
       self.txtpass.place(x=200,y=150)
       Frame(frame,width=295,height=2,bg='black').place(x=200,y=185)
    #    sign btn
    
       loginbtn=Button(frame,command=self.login,width=16,pady=7,text='Sign in',bg='red',fg='white',border=0,cursor='hand2')
       loginbtn.place(x=70,y=250)
       
    #    new user btn
    
       newbtn=Button(frame,command=self.register_window,width=16,pady=7,text='New User',bg='red',fg='white',border=0,cursor='hand2')
       newbtn.place(x=190,y=250)
       
   #   forgot password
       newbtn1=Button(frame,command=self.forgot_window,width=16,pady=7,text='Forgot Password?',bg='#fefbe9',fg='red',border=0,cursor='hand2')
       newbtn1.place(x=130,y=290)

       
   

    def register_window(self):
       self.new_window=Toplevel(self.root)
       self.app=Register(self.new_window)
    
    def forgot_window(self):
       self.new_window=Toplevel(self.root)
       self.app=Forgot(self.new_window)       
   #  after login
    def login(self):
           if self.txtuser.get()=="" and self.txtpass.get()=="":
              messagebox.showerror("Error","Enter all the fields")     
           else:
 
                 open_main=messagebox.askyesno("YesNo","Confirm to login")
                 if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Bms(self.new_window)
                 else:
                    if not open_main:
                       return


class Register:
    def __init__(self,root):
       self.root=root
       self.root.title('Register')
       self.root.geometry("1500x750+300+200")
       self.root.configure(bg="white")
       
    #   variaables 
       self.var_name=StringVar()
       self.var_address=StringVar()
       self.var_gender=StringVar()
       self.var_mobile=StringVar()
       self.var_email=StringVar()
       self.var_pasw=StringVar()
       
    #    frame
       frame=Frame(self.root,bg="white")
       frame.place(x=425,y=100,width=700,height=650)
    #    registration label
       register_lbl=Label(frame,text="Register Here",font=("Arial Narrow",26,"bold"),bg="white",)
       register_lbl.place(x=250,y=0)
       
       name=Label(frame,text="Name*         :",font=('Arial Narrow',20,'bold'),bg="white")   
       name.place(x=60,y=100)              
       self.name_entry=ttk.Entry(frame,textvariable=self.var_name,font=('Tite',18))
       self.name_entry.place(x=240,y=100,width=325)
       
       address=Label(frame,text="Address*    :",font=('Arial Narrow',20,'bold'),bg="white")   
       address.place(x=60,y=160)           
       self.address_entry=ttk.Entry(frame,textvariable=self.var_address,font=('Tite',18))
       self.address_entry.place(x=240,y=160,width=325)
       
       gender=Label(frame,text="Gender       :",font=('Arial Narrow',20,'bold'),bg="white")
       gender.place(x=60,y=220)
       gen=StringVar()
       g1 = Radiobutton(frame, text="Male",variable=gen,value="Male",font=('Arial Narrow',18),bg="white")
       g1.place(x=240,y=220)
       
       g2 = Radiobutton(frame, text="Female",variable=gen,value="Female",font=('Arial Narrow',18),bg="white")
       g2.place(x=350,y=220)
       
       mobile=Label(frame,text="Mobile        :",font=('Arial Narrow',20,'bold'),bg="white")   
       mobile.place(x=60,y=280)       
       self.mobile=ttk.Entry(frame,textvariable=self.var_mobile,font=('Title',18))
       self.mobile.place(x=240,y=280,width=325)
       
       pasw=Label(frame,text="Password  :",font=('Arial Narrow',20,'bold'),bg="white")   
       pasw.place(x=60,y=340)       
       self.pasw=ttk.Entry(frame,textvariable=self.var_pasw,font=('title',18),show=".")
       self.pasw.place(x=240,y=340,width=325)
       

       

    #    button
       loginbtn=Button(frame,command=self.Register_data,width=26,pady=7,text='Submit',bg='blue',fg='white',border=0)
       loginbtn.place(x=190,y=450,width=325)
       
    
       
    def Register_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="" or self.var_mobile()=="" or self.var_pasw.get()=="":
            messagebox.showinfo("Success","Registered Successfully Go Back And Login",parent=self.root)
        else:
            messagebox.showinfo("Success","Registered Successfully Go Back And Login",parent=self.root)


       
    
       
    def Register_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="" or self.var_mobile()=="" or self.var_pasw.get()=="":
            messagebox.showinfo("Success","Registered Successfully Go Back And Login",parent=self.root)
        else:
            messagebox.showinfo("Success","Registered Successfully Go Back And Login",parent=self.root)

class Forgot:
    def __init__(self,root):
       self.root=root
       self.root.title('Register')
       self.root.geometry("1500x750+300+200")
       self.root.configure(bg="white")
       
    #   variables 
       self.var_name=StringVar()
       self.var_address=StringVar()
       self.var_gender=StringVar()
       self.var_mobile=StringVar()
       self.var_email=StringVar()
       self.var_pasw=StringVar()
       
    #    frame
       frame=Frame(self.root,bg="white")
       frame.place(x=425,y=100,width=700,height=650)
    #    registration lable
       register_lbl=Label(frame,text="Reset Password Here",font=("Arial Narrow",26,"bold"),bg="white",)
       register_lbl.place(x=170,y=0)
       
       name=Label(frame,text="Name*         :",font=('Arial Narrow',20,'bold'),bg="white")   
       name.place(x=60,y=100)              
       self.name_entry=ttk.Entry(frame,textvariable=self.var_name,font=('Tite',18))
       self.name_entry.place(x=240,y=100,width=325)
       
       address=Label(frame,text="Address*    :",font=('Arial Narrow',20,'bold'),bg="white")   
       address.place(x=60,y=160)           
       self.address_entry=ttk.Entry(frame,textvariable=self.var_address,font=('Tite',18))
       self.address_entry.place(x=240,y=160,width=325)
       
       gender=Label(frame,text="Gender       :",font=('Arial Narrow',20,'bold'),bg="white")
       gender.place(x=60,y=220)
       gen=StringVar()
       g1 = Radiobutton(frame, text="Male",variable=gen,value="Male",font=('Arial Narrow',18),bg="white")
       g1.place(x=240,y=220)
       
       g2 = Radiobutton(frame, text="Female",variable=gen,value="Female",font=('Arial Narrow',18),bg="white")
       g2.place(x=350,y=220)
       
       mobile=Label(frame,text="Mobile        :",font=('Arial Narrow',20,'bold'),bg="white")   
       mobile.place(x=60,y=280)       
       self.mobile=ttk.Entry(frame,textvariable=self.var_mobile,font=('Title',18))
       self.mobile.place(x=240,y=280,width=325)
       
       pasw=Label(frame,text="Password  :",font=('Arial Narrow',20,'bold'),bg="white")   
       pasw.place(x=60,y=340)       
       self.pasw=ttk.Entry(frame,textvariable=self.var_pasw,font=('title',18),show=".")
       self.pasw.place(x=240,y=340,width=325)
       

       

    #    button
       loginbtn=Button(frame,command=self.Register_data,width=26,pady=7,text='Submit',bg='blue',fg='white',border=0)
       loginbtn.place(x=190,y=450,width=325)
       
    
       
    def Register_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="" or self.var_mobile()=="" or self.var_pasw.get()=="":
            messagebox.showinfo("Success","Registered Successfully Go Back And Login",parent=self.root)
        else:
            messagebox.showinfo("Success","Registered Successfully Go Back And Login",parent=self.root)


       
    
       
    def Register_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="" or self.var_mobile()=="" or self.var_pasw.get()=="":
            messagebox.showinfo("Success","Registered Successfully Go Back And Login",parent=self.root)
        else:
            messagebox.showinfo("Success","Registered Successfully Go Back And Login",parent=self.root)




    
class Bms:
   def __init__(self,root):
       self.root=root
       self.root.title('main')
       self.root.geometry("1500x750+0+0")

       frame=Frame(self.root,bg="#643e46")
       frame.place(x=4,y=2,width=1500,height=50)
      
       bms=lbl=Label(frame,text="Book Management System",font=('Times New Roman',25,'bold'),fg="black",bg="#643e46")
       bms.place(x=550,y=4)
       

       box1=Frame(self.root,bg="black")
       box1.place(x=380,y=220,height=60,width=260)
       main=lbl=Label(box1,text="Main page",font=('Times New Roman',22,'bold'),fg="white",bg="black")
       main.place(x=60,y=15)         
       
       box=Frame(self.root,bg="#643e46")
       box.place(x=380,y=280,height=300,width=750)
             
       req_btn=Button(box,command=self.request,width=26,pady=7,text='Request Book',bg='#ba0020',fg='white',border=0,cursor='hand2',font=('Times New Roman',16,'bold'))
       req_btn.place(x=180,y=70,width=390)
       
       sub_btn=Button(box,command=self.submit,width=26,pady=7,text='Submit Book',bg='#ba0020',fg='white',border=0,cursor='hand2',font=('Times New Roman',16,'bold'))
       sub_btn.place(x=180,y=180,width=390)
       

   #  subimt book page call
   def submit(self):      
      open_main=messagebox.askyesno("Confirmation","Confirm submit",parent=self.root)      
      if open_main>0:
         
         self.new_window=Toplevel(self.root)
         self.app=submit_page(self.new_window)
         
      else:
         if not open_main:
            return

# request page call
   def request(self):      
      open_main=messagebox.askyesno("YesNo","conform request",parent=self.root)      
      if open_main>0:
         
         self.new_window=Toplevel(self.root)
         self.app=request_page(self.new_window)
         
      else:
         if not open_main:
            return

         

         # submit page created
class submit_page:
   def __init__(self,root):
       self.root=root
       self.root.title('main')
       self.root.geometry("1500x750+0+0")
       frame=Frame(self.root,bg="#643e46")
       frame.place(x=4,y=2,width=1520,height=50)
      
       bms=lbl=Label(frame,text="Book Management System",font=('Times New Roman',25,'bold'),fg="black",bg="#643e46")
       bms.place(x=0,y=4)

    #    separate frame for login
       
       box1=Frame(self.root,bg="black")
       box1.place(x=390,y=230,height=60,width=260)
       main=lbl=Label(box1,text="Submit Book",font=('Times New Roman',22,'bold'),fg="white",bg="black")
       main.place(x=60,y=10)         
       
       box=Frame(self.root,bg="#643e46")
       box.place(x=390,y=285,height=380,width=700)
       
    #    sub=Label(box,text="Submit Book",fg="black",bg="#643e46",font=('Times New Roman',20))
    #    sub.place(x=115,y=20)      
    #    Frame(box,width=405,height=2,bg='black').place(x=0,y=65)
       
    #    username=lbl=Label(box,text="Username   :User",font=('Times New Roman',22,'bold'),fg="black",bg="#643e46")
    #    username.place(x=20,y=80)       
    #    id=lbl=Label(box,text="Id Numbeer :121xx0",font=('Times New Roman',20,'bold'),fg="black",bg="#643e46")
    #    id.place(x=20,y=120) 
    #    Frame(box,width=405,height=2,bg='black').place(x=0,y=170)
       
       ur_name=Label(box,text="User Name :",font=('Times New Roman',22),fg="black",bg="#643e46").place(x=60,y=60)
       user = Entry(box,width=25,fg='black',border=0,bg='white',font=('Times New Roman',22))
       user.place(x=280,y=60)
       
       bk_name=Label(box,text="Book Name :",font=('Times New Roman',22),fg="black",bg="#643e46").place(x=60,y=140)
       book = Entry(box,width=25,fg='black',border=0,bg='white',font=('Times New Roman',22))
       book.place(x=280,y=140)
       
       pr=Label(box,text="Price:",font=('Times New Roman',22),fg="black",bg="#643e46").place(x=60,y=220)
       price = Entry(box,width=25,fg='black',border=0,bg='white',font=('Times New Roman',22))
       price.place(x=280,y=220)

                      
       sub_btn=Button(box,command=self.submitted ,width=26,pady=7,text='Submit Book',bg='white',fg='#643e46',border=0,cursor='hand2',font=('Times New Roman',16,'bold'))
       sub_btn.place(x=160,y=300,width=390)
   
   def submitted(self):
      
      open_main= messagebox.askyesno("YesNo","conform Submit",parent=self.root)      
      
      if open_main>0:
         
         messagebox.showinfo("success","submited",parent=self.root)       

         
      else:
        
         messagebox.showerror("error","not submitted",parent=self.root)

         



class request_page:
   def __init__(self,root):
       self.root=root
       self.root.title('main')
       self.root.geometry("1500x750+0+0")

       frame=Frame(self.root,bg="#643e46")
       frame.place(x=4,y=2,width=1520,height=50)
      
       bms=lbl=Label(frame,text="Book Management System",font=('Times New Roman',25,'bold'),fg="black",bg="#643e46")
       bms.place(x=0,y=4)
       
       box1=Frame(self.root,bg="black")
       box1.place(x=390,y=170,height=60,width=260)
       main=lbl=Label(box1,text="Request Book",font=('Times New Roman',22,'bold'),fg="white",bg="black")
       main.place(x=60,y=10)         
       

    #    saparate frame for login
       box=Frame(self.root,bg="#643e46")
       box.place(x=390,y=230,height=400,width=700)
       
    #    sub=Label(box,text="Request Book",fg="black",bg="#643e46",font=('Times New Roman',20,"bold"))
    #    sub.place(x=110,y=20)      
    #    Frame(box,width=800,height=2,bg='black').place(x=0,y=65)
       
    #    username=lbl=Label(box,text="Username   :User",font=('Times New Roman',22,'bold'),fg="black",bg="#643e46")
    #    username.place(x=20,y=80)       
    #    id=lbl=Label(box,text="Id Numbeer :121xx0",font=('Times New Roman',20,'bold'),fg="black",bg="#643e46")
    #    id.place(x=20,y=120) 
    #    Frame(box,width=405,height=2,bg='black').place(x=0,y=170)
       
       ur_name=Label(box,text="User Name :",font=('Times New Roman',22),fg="black",bg="#643e46").place(x=60,y=60)
       user = Entry(box,width=25,fg='black',border=0,bg='white',font=('Times New Roman',22))
       user.place(x=280,y=60)
       
       bk_name=Label(box,text="Avalable Books :",font=('Times New Roman',22),fg="black",bg="#643e46").place(x=60,y=140)
       clicked= StringVar()
       drop = OptionMenu(box, clicked,"A Little Life","Volume One","The Tipping Point","Darkmans","The Siege","Visitation","Bad Blood","b2","b2")
       drop.pack()
       drop.place(x=280,y=140,width=350,height=35)

       
       pr=Label(box,text="Price:",font=('Times New Roman',22),fg="black",bg="#643e46").place(x=60,y=220)
       price = Entry(box,width=25,fg='black',border=0,bg='white',font=('Times New Roman',22))
       price.place(x=280,y=220)


                      
       sub_btn=Button(box,command=self.submitted ,width=26,pady=7,text='Order Book',bg='white',fg='#643e46',border=0,cursor='hand2',font=('Times New Roman',16,'bold'))
       sub_btn.place(x=170,y=300,width=390)
   
   def submitted(self):
      open_main=messagebox.askyesno("YesNo","confirm Order",parent=self.root)      
      if open_main>0:
         messagebox.showinfo("Success","Orderded successfully",parent=self.root)
      else:
         messagebox.showerror("Error","not Orderded",parent=self.root)
    

     
   
           


if __name__=="__main__":
    root=Tk()
    app=Login_window(root)
    root.mainloop()
    