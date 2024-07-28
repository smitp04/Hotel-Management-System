from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Booking Details")
        self.root.geometry("1200x550+100+100")


        # Variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noOfdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()


        # Title
        label_ti = Label(self.root, text="Room Booking Details", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        label_ti.place(x=0, y=0, width=1170, height=50)

        # Logo
        img2 = Image.open("images/pic2.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        labeling2 = Label(self.root, image=self.photoimage2, bd=0, relief=RIDGE)
        labeling2.place(x=5, y=2, width=100, height=40)

        # Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=480)

        # Customer contact
        cust_contact = Label(labelframeleft, text="Customer Contact", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cust_contact.grid(row=0, column=0, sticky=W)
        entry_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, width=20, font=("arial", 13, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        btn_fetch = Button(labelframeleft, command=self.fetch_contact, text="Fetch Data", font=("times new roman", 14, "bold"), bg="black", fg="gold", width=10)
        btn_fetch.place(x=300, y=0)

        # Check-in date
        check_in_date = Label(labelframeleft, text="Check-in Date", font=("times new roman", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        entry_check_in = ttk.Entry(labelframeleft, textvariable=self.var_checkin, width=25, font=("arial", 13, "bold"))
        entry_check_in.grid(row=1, column=1)

        # Check-out date
        check_out_date = Label(labelframeleft, text="Check-out Date", font=("times new roman", 12, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        entry_check_out = ttk.Entry(labelframeleft, textvariable=self.var_checkout, width=25, font=("arial", 13, "bold"))
        entry_check_out.grid(row=2, column=1)

        # Room type
        room_type = Label(labelframeleft, text="Room Type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        room_type.grid(row=3, column=0, sticky=W)
        combo_room_type = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=("arial", 13, "bold"), width=23, state="readonly")
        combo_room_type["values"] = ("Single", "Double", "Luxury")
        combo_room_type.grid(row=3, column=1)

        # Meal
        meal = Label(labelframeleft, text="Meal", font=("times new roman", 12, "bold"), padx=2, pady=6)
        meal.grid(row=4, column=0, sticky=W)
        entry_meal = ttk.Entry(labelframeleft, textvariable=self.var_meal, width=25, font=("arial", 13, "bold"))
        entry_meal.grid(row=4, column=1)

        # Number of days
        num_of_days = Label(labelframeleft, text="Number of Days", font=("times new roman", 12, "bold"), padx=2, pady=6)
        num_of_days.grid(row=5, column=0, sticky=W)
        entry_num_of_days = ttk.Entry(labelframeleft, textvariable=self.var_noOfdays, width=25, font=("arial", 13, "bold"))
        entry_num_of_days.grid(row=5, column=1)

        # Paid Tax
        paid_tax = Label(labelframeleft, text="Paid Tax", font=("times new roman", 12, "bold"), padx=2, pady=6)
        paid_tax.grid(row=6, column=0, sticky=W)
        entry_paid_tax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, width=25, font=("arial", 13, "bold"))
        entry_paid_tax.grid(row=6, column=1)

        # Sub Total
        sub_total = Label(labelframeleft, text="Sub Total", font=("times new roman", 12, "bold"), padx=2, pady=6)
        sub_total.grid(row=7, column=0, sticky=W)
        entry_sub_total = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, width=25, font=("arial", 13, "bold"))
        entry_sub_total.grid(row=7, column=1)

        # Total Cost
        total_cost = Label(labelframeleft, text="Total Cost", font=("times new roman", 12, "bold"), padx=2, pady=6)
        total_cost.grid(row=8, column=0, sticky=W)
        entry_total_cost = ttk.Entry(labelframeleft, textvariable=self.var_total, width=25, font=("arial", 13, "bold"))
        entry_total_cost.grid(row=8, column=1)

        # Button bill
        btnbill = Button(labelframeleft, text="Add", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btnbill.grid(row=10, column=0, padx=1, sticky=W)

        # Buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=420, height=30)

        btn_add = Button(btn_frame, text="Save", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_reset.grid(row=0, column=3, padx=1)

        # Right side image
        img3 = Image.open("images/bed.jpeg")
        img3 = img3.resize((405, 220), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        labeling3 = Label(self.root, image=self.photoimage3, bd=0, relief=RIDGE)
        labeling3.place(x=760, y=55, width=405, height=220)

        # Table frame search system
        labelframeleft1 = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft1.place(x=435, y=280, width=730, height=260)

        search = Label(labelframeleft1, text="Search By: ", bg="red", fg="white", font=("times new roman", 12, "bold"))
        search.grid(row=0, column=0, sticky=W, padx=2)

        self.serch_var = StringVar()
        combo_search = ttk.Combobox(labelframeleft1, textvariable=self.serch_var, font=("times new roman", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Contact", "Room No")
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txt_search = ttk.Entry(labelframeleft1, textvariable=self.txt_search, width=24, font=("times new roman", 13, "bold"))
        txt_search.grid(row=0, column=2, padx=2)

        btn_search = Button(labelframeleft1, text="Search", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_search.grid(row=0, column=3, padx=1)

        btn_ShowAll = Button(labelframeleft1, text="Show All", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_ShowAll.grid(row=0, column=4, padx=1)

        table_frame = Frame(labelframeleft1, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=50, width=720, height=180)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(table_frame, column=("Contact", "Check-in", "Check-out", "Room Type", "Room No", "Meal", "NoOfDays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact", text="Contact")
        self.room_table.heading("Check-in", text="Check-in")
        self.room_table.heading("Check-out", text="Check-out")
        self.room_table.heading("Room Type", text="Room Type")
        self.room_table.heading("Room No", text="Room No")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("NoOfDays", text="No Of Days")

        self.room_table["show"] = "headings"

        self.room_table.column("Contact", width=100)
        self.room_table.column("Check-in", width=100)
        self.room_table.column("Check-out", width=100)
        self.room_table.column("Room Type", width=100)
        self.room_table.column("Room No", width=100)
        self.room_table.column("Meal", width=100)
        self.room_table.column("NoOfDays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)


#fetch data form the database
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error", "Please Enter Contact Number", parent=self.root)
        else:
            conne = mysql.connector.connect(host="localhost", username="root", password="Smit@5521", database="hotel")
            mycur = conne.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            mycur.execute(query,value)
            row=mycur.fetchone()
            if row==None:
                messagebox.showerror("This number not found!!",parent=self.root)
            else:
                conne.commit()
                conne.close()

                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=455,y=5,width=300,height=180)

                lblename=Label(showdataframe,text="Name:",font=("arial",12,"bold"))
                lblename.place(x=0,y=0)


                lbl=Label(showdataframe,text=row,font=("airal",12,"bold"))
                lbl.place(x=90,y=0)



if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
