from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student


class Face_Recognization_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")
      #first image  
        img=Image.open(r"C:\frs photos\OIP.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
       #2second image
        img1=Image.open(r"C:\frs photos\facialrecognition.png")
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

        title_lbl=Label(bg_lbl,text="FACE RECOGNIZATION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

       #student button
        img4=Image.open(r"C:\frs photos\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_lbl,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)


        b1_1=Button(bg_lbl,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


         #Detect Face button
        img5=Image.open(r"C:\frs photos\face_detector1.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)


        b1_1=Button(bg_lbl,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

         #Attendnce button
        img6=Image.open(r"C:\frs photos\report.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_lbl,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)


        b1_1=Button(bg_lbl,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)


         #Help  button
        img7=Image.open(r"C:\frs photos\help.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_lbl,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)


        b1_1=Button(bg_lbl,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        #Train  button
        img8=Image.open(r"C:\frs photos\Train.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_lbl,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)


        b1_1=Button(bg_lbl,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)


         #photo  button
        img9=Image.open(r"C:\frs photos\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_lbl,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)


        b1_1=Button(bg_lbl,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


         #Developer  button
        img10=Image.open(r"C:\frs photos\developer.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_lbl,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)


        b1_1=Button(bg_lbl,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

         #Exit  button
        img11=Image.open(r"C:\frs photos\exit.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_lbl,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)


        b1_1=Button(bg_lbl,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

        ##########function buttons###
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognization_System(root)
    root.mainloop()
