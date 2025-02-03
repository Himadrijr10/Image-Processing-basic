from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")#you can set your own monitor resolution
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",36,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1600,height=45)

        img_top=Image.open(r"project-images\17.jpg")#insert a image
        img_top=img_top.resize((1600,720))#resize((530,130),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1600,height=720)

    # Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"project-images\17.jpg")#insert a image
        img_top1=img_top1.resize((200,200))#resize((530,130),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

    # Developer info
        dev_label=Label(main_frame,text="Hello my name , Himadri",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am full stack developer",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=40)


        img2=Image.open(r"project-images\3.jpg")#insert a image
        img2=img2.resize((500,400))#resize((530,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=400)








if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()

