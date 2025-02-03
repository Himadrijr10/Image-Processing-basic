from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")#you can set your own monitor resolution
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",36,"bold"),bg="white",fg="blue") 
        title_lbl.place(x=0,y=0,width=1600,height=45)

        img_top=Image.open(r"project-images\7.jpg")#insert a image
        img_top=img_top.resize((800,700))#resize((530,130),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)


        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=800,height=700)


           
        img_bottom=Image.open(r"project-images\7.jpg")#insert a image
        img_bottom=img_bottom.resize((800,700))#resize((530,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=800,y=55,width=800,height=700)

            # button
        b1_1=Button(f_lbl,text="Face Recogmition",font=("times new roman",18,"bold"),bg="white",fg="blue",cursor="hand2")
        b1_1.place(x=370,y=650,width=200,height=40)
        # attandance
    def mark_attandance(self,i,r,n,d):
        with open("Attandance.csv","r+",newline="\n"):
            myDataList=f.reallines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list)and (n not in name_list)and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},preset")


        # face recognition
            
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiscale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Himadri@124",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                   
                if confidence>75:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attandance(i,r,n,d)
                else:
                        cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,f"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
            
        def recognize(img,clf,faceCasede):
            coord=draw_boundray(img,faceCasede,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCasede=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCasede)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()

   

if __name__=="__main__":
        root=Tk()
        obj=Face_Recognition(root)
        root.mainloop()