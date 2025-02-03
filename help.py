from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")#you can set your own monitor resolution
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",36,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1600,height=45)

        img_top=Image.open(r"project-images\17.jpg")#insert a image
        img_top=img_top.resize((1600,720))#resize((530,130),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1600,height=720)

        dev_label=Label(f_lbl,text="Email: ",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=600,y=350)






if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
