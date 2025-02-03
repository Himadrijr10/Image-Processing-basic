from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1600x900+0+0")#you can set your own monitor resolution
                self.root.title("Face Recognition System")


                title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",36,"bold"),bg="white",fg="blue")
                title_lbl.place(x=0,y=0,width=1600,height=45)

                img_top=Image.open(r"project-images\7.jpg")#insert a image
                img_top=img_top.resize((1600,340))#resize((530,130),Image.ANTIALIAS)
                self.photoimg_top=ImageTk.PhotoImage(img_top)

                f_lbl=Label(self.root,image=self.photoimg_top)
                f_lbl.place(x=0,y=55,width=1600,height=340)
                
        # button
                b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,font=("times new roman",30,"bold"),bg="white",fg="blue",cursor="hand2")
                b1_1.place(x=0,y=400,width=1600,height=60)

                img_bottom=Image.open(r"project-images\7.jpg")#insert a image
                img_bottom=img_bottom.resize((1600,340))#resize((530,130),Image.ANTIALIAS)
                self.photoimg_left=ImageTk.PhotoImage(img_bottom)

                f_lbl=Label(self.root,image=self.photoimg_left)
                f_lbl.place(x=0,y=470,width=1600,height=340)


        def train_classifier(self):        
                data_dir=("data")
                path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

                faces=[]
                ids=[]

                for image in path:
                        img=Image.open(image).convert('L') #Gray scale image
                        imageNP=np.array(img,'uint8')
                        id=int(os.path.split(image)[1].split('.')[1])

                        faces.append(imageNP)
                        ids.append(id)
                        cv2.imshow("Training",imageNP)
                        cv2.waitKey(1)==13
                ids=np.array(ids)

                # Train the classifier and save
                clf=cv2.face.LBPHFaceRecognizer_create()
                clf.train(faces,ids)
                clf.write("classifier.xml")
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Training datasts completed!!!")






if __name__=="__main__":
        root=Tk()
        obj=Train(root)
        root.mainloop()
