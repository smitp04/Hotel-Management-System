from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox


class detailsroom:
    def __init__(self, root):
        self.root = root
        self.root.title("Details")
        self.root.geometry("1200x550+100+100")

        # Title
        label_ti = Label(self.root, text="Room Booking Details", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        label_ti.place(x=0, y=0, width=1170, height=40)

        
        # Logo
        img2 = Image.open("images/pic2.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        labeling2 = Label(self.root, image=self.photoimage2, bd=0, relief=RIDGE)
        labeling2.place(x=5, y=2, width=100, height=40)

        # Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Added ", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)



        # Floor name
        floor_read = Label(labelframeleft, text="Floor Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        floor_read.grid(row=0, column=0, sticky=W)

        self.var_floor=StringVar()
        floor = ttk.Entry(labelframeleft, textvariable=self.var_floor,width=29, font=("times new roman", 13, "bold"))
        floor.grid(row=0, column=1)


        # Room No
        floor_room = Label(labelframeleft, text="Room No", font=("times new roman", 12, "bold"), padx=2, pady=6)
        floor_room.grid(row=1, column=0, sticky=W)
        self.var_roomno=StringVar()
        floor1 = ttk.Entry(labelframeleft,textvariable=self.var_roomno, width=29, font=("times new roman", 13, "bold"))
        floor1.grid(row=1, column=1)

        # Room Type
        floor_name2 = Label(labelframeleft, text="Room Type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        floor_name2.grid(row=2, column=0, sticky=W)
        self.var_roomtyp=StringVar()
        floor2 = ttk.Entry(labelframeleft,textvariable=self.var_roomtyp, width=29, font=("times new roman", 13, "bold"))
        floor2.grid(row=2, column=1)


        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=420, height=30)

        btn_add = Button(btn_frame, text="Add", command=self.add_dataaa, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update", command=self.fetch_data,font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_reset.grid(row=0, column=3, padx=1)


        labelframeleft1 = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show room Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft1.place(x=500, y=55, width=600, height=400)

        scroll_x = ttk.Scrollbar(labelframeleft1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(labelframeleft1, orient=VERTICAL)

        self.room_table = ttk.Treeview(labelframeleft1, column=("Floor", "RoomNo", "RoomType"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Floor", text="Floor")
        self.room_table.heading("RoomNo", text="RoomNo")
        self.room_table.heading("RoomType", text="RoomType")

        self.room_table["show"] = "headings"

        self.room_table.column("Floor", width=100)
        self.room_table.column("RoomNo", width=100)
        self.room_table.column("RoomType", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor) 




    def add_dataaa(self):
        if self.var_floor.get() == "" or self.var_roomtyp.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conne = mysql.connector.connect(host="localhost", username="root", password="Smit@5521", database="hotel")
                mycur = conne.cursor()
                mycur.execute("insert into details values(%s,%s,%s)", (
                        self.var_floor.get(),
                        self.var_roomno.get(),
                        self.var_roomtyp.get(),
                    ))

                conne.commit()
                self.fetch_data()
                conne.close()
                messagebox.showinfo("Success", "New room added sucessfully!", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Smit@5521", database="hotel")
        cursor = conn.cursor()
        cursor.execute("select * from details")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for row in rows:
                self.room_table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtyp.set(row[2])

    def update_data(self):
        if self.var_floor .get() == "":
            messagebox.showerror("Error", "Please enter Floor number", parent=self.root)
        else:
            try:
                conne = mysql.connector.connect(host="localhost", username="root", password="Smit@5521", database="hotel")
                mycur = conne.cursor()
                mycur.execute("update details set Floor=%s,RoomType=%s  where  RoomNo=%s"),(                       
                        self.var_floor.get(),
                        self.var_roomtyp.get(),
                        self.var_roomno.get(),
                    )


                conne.commit()
                self.fetch_data()
                conne.close()
                messagebox.showinfo("Update", "Room details have been updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
 




if __name__ == "__main__":
    root = Tk()
    obj = detailsroom(root)
    root.mainloop()
