from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk         # pip install pillow
from tkinter import messagebox
from register import Register
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1600x900+0+0")

        # BG Image
        self.bg = ImageTk.PhotoImage(file=r"project-images\7.JPG")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"project-images\loginicon.JPG")
        img1 = img1.resize((100, 100))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Label 1
        username = lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Label 2
        password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)
        self.txtpassword = ttk.Entry(frame, show="*", font=("times new roman", 15, "bold"))
        self.txtpassword.place(x=40, y=250, width=270)

        # Icon Image
        img2 = Image.open(r"project-images\loginicon.jpg")
        img2 = img2.resize((25, 25))
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"project-images\lock icon.jpg")
        img3 = img3.resize((25, 25))
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="blue", borderwidth=0)
        lblimg1.place(x=650, y=393, width=25, height=25)

        # Login Button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3,relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register Button
        loginbtn = Button(frame, text="New User Register",command=self.register_window, font=("times new roman", 15, "bold"), borderwidth=0,fg="white", bg="black", activeforeground="white", activebackground="black")
        loginbtn.place(x=20, y=350, width=160)

        # Forget Button
        loginbtn = Button(frame, text="Forget Password",command=self.forgot_password_window, font=("times new roman", 15, "bold"), borderwidth=0,fg="white", bg="black", activeforeground="white", activebackground="black")
        loginbtn.place(x=10, y=380, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

     # Login Button Function
    def login(self):
        if self.txtuser.get() == "" or self.txtpassword.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "Bunny" and self.txtpassword.get() == "Raju":
            messagebox.showinfo("Success", "Welcome To My Earth ['_'] ")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Himadri@124",database="face_recognizer")
            my_cursor = conn.cursor()

        # Use hashing for passwords in a real application
            my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (
                                                                                    self.var_email.get(),
                                                                                    self.var_pass.get()
                                                                                ))

        row = my_cursor.fetchone()

        if row == None:
            messagebox.showerror("Error", "Invalid Username & Password")
        else:
            open_main = messagebox.askyesno("Yes No", "Access only Admin")
            if open_main > 0:
                self.new_window = Toplevel(self.new_window)
                # Instantiate your main application class here, assuming it has a constructor
                self.app = Face_Recognition_System(self.new_window) 
            else:
                if not open_main:
                    return

        conn.commit()
        conn.close()
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email Address to rest password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Himadri@124",database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                



class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_chek = IntVar()

        # Background Image
        self.bg = ImageTk.PhotoImage(r"project-images\7.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Left Image
        self.bg1 = ImageTk.PhotoImage(r"project-images\7.png")
        bg_lbl = Label(self.root, image=self.bg1)
        bg_lbl.place(x=50, y=100, width=470, height=550)

        # Main Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkblue", bg="white")
        register_lbl.place(x=20, y=20)  # x=285,y=20 is middle

        # Label & Entry
        # Row 1
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        # Row 2
        contact = Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # Row 3
        security_Q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Bestfriend name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        # Row 4
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, show="*", textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, show="*", textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # Check Button
        checkbutton = Checkbutton(frame, variable=self.var_chek, text="I Agree The Terms & Conditions", font=("times new roman", 12, "bold"),activeforeground="white", activebackground="grey", onvalue=1, offvalue=0)
        checkbutton.place(x=50, y=390)  # x=285,y=20 is middle

        # Register Now Button
        register_btn = Button(frame, command=self.register_data, text="Register Now", font=("times new roman", 15, "bold"), bd=3,relief=RIDGE, fg="white", bg="darkblue", activeforeground="white", activebackground="blue")
        register_btn.place(x=50, y=430, width=200)

        # Login Button
        login_btn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bd=3,relief=RIDGE, fg="white", bg="darkblue", activeforeground="white", activebackground="blue")
        login_btn.place(x=370, y=430, width=200)

    # Function Declaration
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be the same")
        elif self.var_chek.get() == 0:
            messagebox.showerror("Error", "Please agree  our terms & conditions")
        else:
           try:
            conn = mysql.connector.connect(host="localhost", user="root",password="Himadri@124",database="face_recognizer")
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s"
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row>0:
                messagebox.showerror("Error", "This email already exists. Please try another email")
            else:
                my_cursor.execute("Insert Into Register Values (%s, %s, %s, %s, %s, %s, %s)",(
                                                                                            self.var_fname.get(),
                                                                                            self.var_lname.get(),
                                                                                            self.var_contact.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_securityQ.get(),
                                                                                            self.var_securityA.get(),
                                                                                            self.var_pass.get()
                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Successful", "Registration successful")
           except Exception as es:
                messagebox.showerror("Error", f"Error during registration: {str(es)}")
            

# Object
if __name__ == "__main__":
    main()