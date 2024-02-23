from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")

        ####variable###
        self.var_Dep=StringVar()
        self.var_Course=StringVar()
        self.var_Year=StringVar()
        self.var_Sem=StringVar()
        self.var_ID=StringVar()
        self.var_Name=StringVar()
        self.var_Div=StringVar()
        self.var_Roll=StringVar()
        self.var_Gender=StringVar()
        self.var_DOB=StringVar()
        self.var_Email=StringVar()
        self.var_phone=StringVar()
        self.var_Adress=StringVar()
        self.var_teacher=StringVar()
        


        #first image  
        img=Image.open(r"C:\frs photos\OIP.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
       #2second image
        img1=Image.open(r"C:\frs photos\imgref3_orig.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image

        img2=Image.open(r"C:\frs photos\OIP.jpeg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #background image

        img3=Image.open(r"C:\frs photos\bg.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_lbl=Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=130,width=1530,height=710)

         #title card

        title_lbl=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1480,height=600)

        #left side label frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=580)

        img_left=Image.open(r"C:\frs photos\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=730,height=130)
        
        #current course

        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=115)

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Dep,font=("times new roman",13,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","EEE","CSIT","ECE","CSE","MECH")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Section

        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Course,font=("times new roman",13,"bold"),state="readonly")
        course_combo["values"]=("Select Course","A","B","C")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #YEAR

        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_label_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Year,font=("times new roman",13,"bold"),state="readonly")
        year_label_combo["values"]=("Select Year","I","II","III","IV")
        year_label_combo.current(0)
        year_label_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


         #Semester

        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_label_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Sem,font=("times new roman",13,"bold"),state="readonly")
        semester_label_combo["values"]=("Select Year","I","II")
        semester_label_combo.current(0)
        semester_label_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student infprmatiom

        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student  Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

        #student details

        studentid_label=Label(class_student_frame,text="Student ID",font=("times new roman",13,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_ID,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student name

        studentname_label=Label(class_student_frame,text="Student Name",font=("times new roman",13,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_Name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,sticky=W)

        #class division

        division_label=Label(class_student_frame,text="Division",font=("times new roman",13,"bold"),bg="white")
        division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

       

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Div,font=("times new roman",13,"bold"),state="readonly")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #roll no

        roll_label=Label(class_student_frame,text="Roll No",font=("times new roman",13,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_Roll,width=20,font=("times new roman",13,"bold"))
        roll_label_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender

        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

       

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","FEMALE","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)


        #DOB

        dob_label=Label(class_student_frame,text="DOB",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        dob_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",13,"bold"))
        dob_label_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #email

        email_label=Label(class_student_frame,text="Email",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_Email,width=20,font=("times new roman",13,"bold"))
        email_label_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone number

        number_label=Label(class_student_frame,text="Phone No",font=("times new roman",13,"bold"),bg="white")
        number_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        number_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        number_label_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #adress

        adress_label=Label(class_student_frame,text="Adress",font=("times new roman",13,"bold"),bg="white")
        adress_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        adress_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_Adress,width=20,font=("times new roman",13,"bold"))
        adress_label_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #class teacher name

        ct_label=Label(class_student_frame,text="Class tacher name",font=("times new roman",13,"bold"),bg="white")
        ct_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        ct_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        ct_label_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #radio buttons for left
        self.var_radio1=StringVar()

        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=5,column=1)




        #button frmae

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=715,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.rest_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=245,width=715,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take a photo sample",width=39,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        upload_photo_btn=Button(btn_frame1,text="Upload photo sample",width=39,font=("times new roman",12,"bold"),bg="blue",fg="white")
        upload_photo_btn.grid(row=0,column=1)


        #Right side label frame

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))

        right_frame.place(x=780,y=10,width=680,height=580)

        img_right=Image.open(r"C:\frs photos\gettyimages-1022573162.jpg")
        img_right=img_right.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl1=Label(right_frame,image=self.photoimg_right)
        f_lbl1.place(x=5,y=0,width=720,height=130)

        #searching system

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=700,height=70)

        search_label=Label(search_frame,text="Search By",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select ","Roll_NO","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_label_entry=ttk.Entry(search_frame,width=20,font=("times new roman",13,"bold"))
        search_label_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="search",width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showbtn_btn=Button(search_frame,text="Show All",width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showbtn_btn.grid(row=0,column=4,padx=4)

        #table frame

        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=210,width=670,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("Dep","Course","Year","Sem","ID","Name","Div","Roll","Gender","DOB","Email","phone","Adress","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
    
        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="Student Id")
        self.student_table.heading("Name",text="student Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Roll",text="Roll no")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("Adress",text="Adress")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="photosamplestatus")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("Adress",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        

        



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    #######function declaration####
    def add_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Vamsi@123",database="face_manager")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                             self.var_Dep.get(),
                                                                                             self.var_Course.get(),
                                                                                             self.var_Year.get(),
                                                                                             self.var_Sem.get(),
                                                                                             self.var_ID.get(),
                                                                                             self.var_Name.get(),
                                                                                             self.var_Div.get(),
                                                                                             self.var_Roll.get(),
                                                                                             self.var_Gender.get(),
                                                                                             self.var_DOB.get(),
                                                                                             self.var_Email.get(),
                                                                                             self.var_phone.get(),
                                                                                             self.var_Adress.get(),
                                                                                             self.var_teacher.get(),
                                                                                             self.var_radio1.get()
                                                                                           ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Succes","Student details has been added Seccessfuly",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    ###########fetch data####
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Vamsi@123",database="face_manager")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

############get cursor#######
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Dep.set(data[0]),
        self.var_Course.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Sem.set(data[3]),
        self.var_ID.set(data[4]),
        self.var_Name.set(data[5]),
        self.var_Div.set(data[6]),
        self.var_Roll.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_Email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_Adress.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

####update function###
    def update_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","Do you want update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Vamsi@123",database="face_manager")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Div=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,phone=%s,Adress=%s,teacher=%s,photo=%s where ID=%s",(

                                                                                                                                                             self.var_Dep.get(),
                                                                                                                                                             self.var_Course.get(),
                                                                                                                                                            self.var_Year.get(),
                                                                                                                                                            self.var_Sem.get(),                                                                                                                                                   
                                                                                                                                                            self.var_Name.get(),
                                                                                                                                                            self.var_Div.get(),
                                                                                                                                                            self.var_Roll.get(),
                                                                                                                                                            self.var_Gender.get(),
                                                                                                                                                            self.var_DOB.get(),
                                                                                                                                                            self.var_Email.get(),
                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                            self.var_Adress.get(),
                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                            self.var_ID.get()               
                                                                                                                                                     ))      
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","student details Update Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

                ##delete function#
    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student Delete Page","Do you want to deletethis studemt details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Vamsi@123",database="face_manager")
                    my_cursor=conn.cursor()
                    sql="delete from student where ID=%s"
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #reset
    def rest_data(self):
        self.var_Dep.set("Select Department")
        self.var_Course.set("Select Course")
        self.var_Year.set("Select Year")
        self.var_Sem.set("Select Semester")
        self.var_ID.set("")
        self.var_Name.set("")
        self.var_Div.set("Select Division")
        self.var_Roll.set("")
        self.var_Gender.set("Select Gender")
        self.var_DOB.set("")
        self.var_Email.set("")
        self.var_phone.set("")
        self.var_Adress.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#########generate data setor take photo sample#
    def generate_dataset(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Vamsi@123",database="face_manager")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Div=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,phone=%s,Adress=%s,teacher=%s,photo=%s where ID=%s",(

                                                                                                                                                        self.var_Dep.get(),
                                                                                                                                                        self.var_Course.get(),
                                                                                                                                                        self.var_Year.get(),
                                                                                                                                                        self.var_Sem.get(),                                                                                                                                                   
                                                                                                                                                        self.var_Name.get(),
                                                                                                                                                        self.var_Div.get(),
                                                                                                                                                        self.var_Roll.get(),
                                                                                                                                                        self.var_Gender.get(),
                                                                                                                                                        self.var_DOB.get(),
                                                                                                                                                        self.var_Email.get(),
                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                        self.var_Adress.get(),
                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                        self.var_ID.get()==id+1              
                                                                                                                                                     )) 
                conn.commit()
                self.fetch_data()
                self.rest_data()
                conn.close()

####load predeined data on face frontal from open cv####

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BAYER_BG2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    ##scalling factor=1.3
                    ##minium Neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
    
                cap=cv2.VideoCapture(0)
                img_id=0         
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
           
                    face=cv2.resize(face_cropped(my_frame),(450,450))
                    face=cv2.cvtColor(face,cv2.COLOR_BAYER_BG2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path)
                    cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Reault","Generating data set completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   

                
                
                
    
    
    
                    
          




        
          




                 
          
    
        


        







if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
