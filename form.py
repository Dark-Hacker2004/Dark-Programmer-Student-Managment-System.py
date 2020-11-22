from tkinter import*
from tkinter import ttk
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1370x700+0+0")

        title=Label(self.root,text="Student Managements System ",font=("time new roman",40,"bold"),bg="yellow", fg="red")
        title.pack(side=TOP,fill=X)
        #=============Varible======
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.Address_var=StringVar()



        #============== Manage Frame============
        manage_Frame=Frame(self.root,bd=4, relief=RIDGE, bg="crimson")
        manage_Frame.place(x=5,y=100,width=400,height=580)


        #==========lable Frame=========


        Detail_Frame=Frame(self.root, bd=4 , relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=410,y=100,width=590,height=560)

        m_title=Label(manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        roll_title=Label(manage_Frame,textvariable=self.Roll_No_var,text="Roll No.", bg="crimson",fg="white",font=("times new roman",17,"bold"))
        roll_title.grid(row=1,column=0,pady=10,padx=20)

        txt_Roll=Entry(manage_Frame,font=("times new roman ",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=10,sticky="w")

    
        lbl_name=Label(manage_Frame,text="Name" , bg="crimson",fg="white",font=("times new roman",17,"bold"))
        lbl_name.grid(row=2,column=0,pady=10, padx=20, sticky="w")

        
        txt_name=Entry(manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10, padx=20, sticky="w")

        lbl_Email=Label(manage_Frame,textvariable=self.email_var,text="Email" , bg="crimson",fg="white",font=("times new roman",17,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10, padx=20, sticky="w")

        txt_Email=Entry(manage_Frame, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10, padx=20, sticky="w")

        lbl_gender=Label(manage_Frame,text="Gender" , bg="crimson",fg="white",font=("times new roman",17,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(manage_Frame,textvariable=self.gender_varfont=("times new roman",15,"bold"))
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4, column=1,pady=10,padx=20)

        lbl_contact=Label(manage_Frame,textvariable=self.contact_var, text="Contact", bg="crimson", fg="white", font=("times new roman",17,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10, padx=20, sticky="w")

        txt_contact=Entry(manage_Frame, font=("times new roman",15,"bold"),bd=5, relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10, padx=20, sticky="w")

        lbl_Dob=Label(manage_Frame,textvariable=self.dob_var,text="D.O.B",bg="crimson", fg="white", font=("times new roman",17,"bold"))
        lbl_Dob.grid(row=6,column=0,pady=10, padx=20, sticky="w")

        txt_Dob=Entry(manage_Frame, font=("times new roman",15,"bold"),bd=5, relief=GROOVE)
        txt_Dob.grid(row=6,column=1,pady=10, padx=20, sticky="w")

        lbl_add=Label(manage_Frame,textvariable=self.Address_var,text="Address",bg="crimson",fg="white",font=("times new roman",17,"bold"))
        lbl_add.grid(row=7,column=0,pady=10, padx=20, sticky="w")

        self.txt_Add=Text(manage_Frame, width=25,height=4,font=("",10))   
        self.txt_Add.grid(row=7,column=1, pady=10 ,padx=20, sticky="w")  

        

        #=============Button Frame=========
        btn_Frame=Frame(manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=10,y=500, width=370)

        addbtn=Button(btn_Frame,text="Add", width=10).grid(row=0,column=0 , padx=5,pady=10)
        updtebtn=Button(btn_Frame,text="Update", width=10).grid(row=0,column=1 , padx=5,pady=10)
        deleten=Button(btn_Frame,text="Delete", width=10).grid(row=0,column=2, padx=5,pady=10)
        clearbtn=Button(btn_Frame,text="Clear", width=10).grid(row=0,column=3 , padx=5,pady=10)


        #=============Detail Frame==============
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="red")
        Detail_Frame.place(x=410,y=100, width=590,height=560)   
        
        lbl_search=Label(Detail_Frame, text="Search By", bg="red", fg="white", font=("times new roman",17,"bold"))
        lbl_search.grid(row=0,column=0,pady=10, padx=20, sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,width=15,font=("times new roman",13,"bold"),state='readonly')
        combo_search['value']=("Roll","Name","Contact")
        combo_search.grid(row=0,column=1,padx=10,pady=10)
        

        txt_search=Entry(Detail_Frame,width=10,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
         
        searchbtn=Button(Detail_Frame, text="Search",width=15).grid(row=0, column=0, padx=10,pady=10) 
        showallbtn=Button(Detail_Frame, text="Show All ",width=10).grid(row=0, column=3, padx=10,pady=10, sticky="w") 

        #=========Tables========================
        Table_Frame=Frame(Detail_Frame,bd=4, relief=RIDGE , bg="crimson")
        Table_Frame.place(x=5,y=60,width=570,height=480)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        Student_Table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_Table.xview)
        scroll_y.config(command=Student_Table.yview)
        Student_Table.heading("roll",text="Roll No")
        Student_Table.heading("name",text="Name")
        Student_Table.heading("email",text="Email")
        Student_Table.heading("gender",text="Gender")
        Student_Table.heading("contact",text="Contact")
        Student_Table.heading("dob",text="D.O.B")
        Student_Table.heading("Address",text="Address")
        Student_Table['show']='headings'
        Student_Table.column("roll",width=50)
        Student_Table.column("name",width=100)
        Student_Table.column("email",width=100)
        Student_Table.column("gender",width=80)
        Student_Table.column("contact",width=100)
        Student_Table.column("dob",width=100)
        Student_Table.column("Address",width=100)
        Student_Table.pack(fill=BOTH,expand=1)
        
        


root=Tk()
obj=Student(root)
root.mainloop()        