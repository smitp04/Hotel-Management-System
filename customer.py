from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Details")
        self.root.geometry("1200x550+100+100")

        # Reference number
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()

        label_ti = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        label_ti.place(x=0, y=0, width=1170, height=50)

        # Logo
        img2 = Image.open("images/pic2.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        labeling2 = Label(self.root, image=self.photoimage2, bd=0, relief=RIDGE)
        labeling2.place(x=5, y=2, width=100, height=40)

        # Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # Customer reference
        cust_ref = Label(labelframeleft, text="Customer Reference", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cust_ref.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=25, state="readonly", font=("arial", 13, "bold"))
        entry_ref.grid(row=0, column=1)

        # Customer name
        cust_name = Label(labelframeleft, text="Customer Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cust_name.grid(row=1, column=0, sticky=W)
        entry_name = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, width=29, font=("times new roman", 13, "bold"))
        entry_name.grid(row=1, column=1)

        # Mother name
        label_mname = Label(labelframeleft, text="Mother Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_mname.grid(row=2, column=0, sticky=W)
        entry_mname = ttk.Entry(labelframeleft, textvariable=self.var_mother, width=29, font=("times new roman", 13, "bold"))
        entry_mname.grid(row=2, column=1)

        # Gender
        label_gender = Label(labelframeleft, text="Gender", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        gendercom = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("times new roman", 12, "bold"), width=32, state="readonly")
        gendercom["value"] = ("Male", "Female", "Other")
        gendercom.grid(row=3, column=1)

        # Postcode
        cust_pos = Label(labelframeleft, text="PostCode", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cust_pos.grid(row=4, column=0, sticky=W)
        entry_post = ttk.Entry(labelframeleft, width=29, textvariable=self.var_post, font=("times new roman", 13, "bold"))
        entry_post.grid(row=4, column=1)

        # Mobile number
        cust_mo = Label(labelframeleft, text="Mobile Number", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cust_mo.grid(row=5, column=0, sticky=W)
        entry_mobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, width=29, font=("times new roman", 13, "bold"))
        entry_mobile.grid(row=5, column=1)

        # Email
        cust_em = Label(labelframeleft, text="E-mail", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cust_em.grid(row=6, column=0, sticky=W)
        entry_email = ttk.Entry(labelframeleft, textvariable=self.var_email, width=29, font=("times new roman", 13, "bold"))
        entry_email.grid(row=6, column=1)

        # Nationality
        cust_nat = Label(labelframeleft, text="Nationality", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cust_nat.grid(row=7, column=0, sticky=W)
        gendercom_na = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=("times new roman", 12, "bold"), width=32, state="readonly")
        gendercom_na["value"] = ("Indian", "American", "Russian")
        gendercom_na.grid(row=7, column=1)

        # ID proof
        cust_id = Label(labelframeleft, text="Id-Proof", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cust_id.grid(row=8, column=0, sticky=W)
        gendercom_id = ttk.Combobox(labelframeleft, textvariable=self.var_idproof, font=("times new roman", 12, "bold"), width=32, state="readonly")
        gendercom_id["value"] = ("Aadharcard", "Driving license", "Passport")
        gendercom_id.grid(row=8, column=1)

        # ID number
        cust_idn = Label(labelframeleft, text="Id_Number", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cust_idn.grid(row=9, column=0, sticky=W)
        entry_idnumber = ttk.Entry(labelframeleft, textvariable=self.var_idnumber, width=29, font=("times new roman", 13, "bold"))
        entry_idnumber.grid(row=9, column=1)

        # Address
        cust_add = Label(labelframeleft, text="Address", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cust_add.grid(row=10, column=0, sticky=W)
        entry_address = ttk.Entry(labelframeleft, textvariable=self.var_address, width=29, font=("times new roman", 13, "bold"))
        entry_address.grid(row=10, column=1)

        # Buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=420, height=30)

        btn_add = Button(btn_frame, text="Add", command=self.add_dataaa, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete", command=self.delete_data, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_reset.grid(row=0, column=3, padx=1)

        labelframeleft1 = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft1.place(x=435, y=50, width=730, height=490)

        search = Label(labelframeleft1, text="Search By: ", bg="red", fg="white", font=("times new roman", 12, "bold"))
        search.grid(row=0, column=0, sticky=W, padx=2)

        self.serch_var = StringVar()
        combo_search = ttk.Combobox(labelframeleft1, textvariable=self.serch_var, font=("times new roman", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Mobile", "Ref")
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txt_search = ttk.Entry(labelframeleft1, textvariable=self.txt_search, width=24, font=("times new roman", 13, "bold"))
        txt_search.grid(row=0, column=2, padx=2)

        btn_search = Button(labelframeleft1, text="Search", command=self.search_data, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_search.grid(row=0, column=3, padx=1)

        btn_ShowAll = Button(labelframeleft1, text="Show All", command=self.fetch_data, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_ShowAll.grid(row=0, column=4, padx=1)

        # Show data table Frame


        table_frame = Frame(labelframeleft1, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=50, width=720, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(table_frame, column=("Ref", "Name", "Mother", "Gender", "PostCode", "Mobile", "Email", "Nationality", "IdProof", "IdNumber", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Ref", text="Refer No")
        self.Cust_Details_Table.heading("Name", text="Name")
        self.Cust_Details_Table.heading("Mother", text="Mother Name")
        self.Cust_Details_Table.heading("Gender", text="Gender")
        self.Cust_Details_Table.heading("PostCode", text="PostCode")
        self.Cust_Details_Table.heading("Mobile", text="Mobile")
        self.Cust_Details_Table.heading("Email", text="Email")
        self.Cust_Details_Table.heading("Nationality", text="Nationality")
        self.Cust_Details_Table.heading("IdProof", text="Id Proof")
        self.Cust_Details_Table.heading("IdNumber", text="Id Number")
        self.Cust_Details_Table.heading("Address", text="Address")

        self.Cust_Details_Table["show"] = "headings"
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)

        self.Cust_Details_Table.column("Ref", width=100)
        self.Cust_Details_Table.column("Name", width=100)
        self.Cust_Details_Table.column("Mother", width=100)
        self.Cust_Details_Table.column("Gender", width=100)
        self.Cust_Details_Table.column("PostCode", width=100)
        self.Cust_Details_Table.column("Mobile", width=100)
        self.Cust_Details_Table.column("Email", width=100)
        self.Cust_Details_Table.column("Nationality", width=100)
        self.Cust_Details_Table.column("IdProof", width=100)
        self.Cust_Details_Table.column("IdNumber", width=100)
        self.Cust_Details_Table.column("Address", width=100)
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)

        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_dataaa(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conne = mysql.connector.connect(host="localhost", username="root", password="Smit@5521", database="hotel")
                mycur = conne.cursor()
                mycur.execute("insert into Customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_ref.get(),
                        self.var_cust_name.get(),
                        self.var_mother.get(),
                        self.var_gender.get(),
                        self.var_post.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_nationality.get(),
                        self.var_idproof.get(),
                        self.var_idnumber.get(),
                        self.var_address.get()
                    ))

                conne.commit()
                self.fetch_data()
                conne.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conne = mysql.connector.connect(host="localhost", username="root", password="Smit@5521", database="hotel")
        mycur = conne.cursor()
        mycur.execute("SELECT * FROM customer")
        rows = mycur.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conne.commit()
        conne.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_idproof.set(row[8])
        self.var_idnumber.set(row[9])
        self.var_address.set(row[10])

    def update_data(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            try:
                conne = mysql.connector.connect(host="localhost", username="root", password="Smit@5521", database="hotel")
                mycur = conne.cursor()
                mycur.execute("update Customer set Name=%s, Mother=%s, Gender=%s, Postcode=%s, Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s, Addrress=%s where Ref=%s", (
                        self.var_cust_name.get(),
                        self.var_mother.get(),
                        self.var_gender.get(),
                        self.var_post.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_nationality.get(),
                        self.var_idproof.get(),
                        self.var_idnumber.get(),
                        self.var_address.get(),
                        self.var_ref.get()
                    ))


                conne.commit()
                self.fetch_data()
                conne.close()
                messagebox.showinfo("Update", "Customer details have been updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def delete_data(self):
        mdelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent=self.root)
        if mdelete > 0:
            conne = mysql.connector.connect(host="localhost", username="root", password="Smit@5521", database="hotel")
            mycur = conne.cursor()
            query = "DELETE FROM customer WHERE Ref=%s"
            value = (self.var_ref.get(),)
            mycur.execute(query, value)
            conne.commit()
            self.fetch_data()
            conne.close()
        else:
            if not mdelete:
                return

    def reset_data(self):
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("")
        self.var_idproof.set("")
        self.var_idnumber.set("")
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search_data(self):
        conne = mysql.connector.connect(host="localhost", username="root", password="Smit@5521", database="hotel")
        mycur = conne.cursor()
        search_column = self.serch_var.get()
        search_value = self.txt_search.get()

        if search_column == "Mobile":
            query = "SELECT * FROM customer WHERE Mobile=%s"
        elif search_column == "Ref":
            query = "SELECT * FROM customer WHERE Ref=%s"
        else:
            messagebox.showerror("Error", "Invalid search criteria", parent=self.root)
            return

        mycur.execute(query, (search_value,))
        rows = mycur.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conne.commit()
        conne.close()

        

if __name__ == "__main__":
    root = Tk()
    obj = Cust_win(root)
    root.mainloop()
