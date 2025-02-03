from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")#you can set your own monitor resolution
        self.root.title("Face Recognition System")

    # variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

    # 1st image
        img1=Image.open(r"project-images\1.jpg")#insert a image 
        img1=img1.resize((800,200))#resize((530,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=800,height=200)

    # 2nd image
        img2=Image.open(r"project-images\3.jpg")#insert a image
        img2=img2.resize((800,200))#resize((530,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=800,height=200)
       
    # bg image
        img4=Image.open(r"project-images\bg5.webp")#insert a image
        img4=img4.resize((1600,900))#resize((530,130),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1600,height=700)

        title_lbl=Label(bg_img,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",36,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1600,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=45,width=1570,height=650)

    #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=770,height=630)

        img_left=Image.open(r"project-images\7.jpg")#insert a image
        img_left=img_left.resize((760,130))#resize((530,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=0,width=760,height=130)

        left_inside_frame=Frame(Left_frame,relief=RIDGE,bd=2,bg="white")
        left_inside_frame.place(x=5,y=135,width=760,height=470)

    # Labeland entry
        # Attendance Id
        attendanceID_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=25,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        # Name
        Namelabel=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        Namelabel.grid(row=0,column=2)

        atten_name=ttk.Entry(left_inside_frame,width=25,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_name.grid(row=0,column=3,pady=10)

        # roll no
        rolllabel=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        rolllabel.grid(row=1,column=0,padx=10,pady=10)

        atten_roll=ttk.Entry(left_inside_frame,width=25,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        atten_roll.grid(row=1,column=1,pady=10)

        # department
        deplabel=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        deplabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,font=("times new roman",12,"bold"),width=25,textvariable=self.var_atten_dep)
        atten_dep.grid(row=1,column=3,pady=10)

        # time
        timelabel=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        timelabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,font=("times new roman",12,"bold"),width=25,textvariable=self.var_atten_time)
        atten_time.grid(row=2,column=1,pady=10)

        # Date
        datelabel=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        datelabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=25,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,pady=10)

        # attendance
        attendancelabel=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attendancelabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold"),state="readonly",width=25,textvariable=self.var_atten_attendance)
        self.atten_status["values"]=("Select Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,pady=10)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=728,height=37)
       
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update=Button(btn_frame,text="Export csv",command=self.exportCsv,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update.grid(row=0,column=1)

        delete=Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete.grid(row=0,column=2)

        reset=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset.grid(row=0,column=3)

    #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=780,height=630)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=760,height=600)

    # Scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","roll","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # fetch data


    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")






if __name__=="__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop()