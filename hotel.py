from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_win
# from room import Room_win
from room import RoomBooking

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x800+0+0") 
        # width height x y axis

        img1 = Image.open("images/pic1.jpg")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        labeling1 = Label(self.root, image=self.photoimage1, bd=4, relief=RIDGE)
        labeling1.place(x=0, y=0, width=1550, height=140)

        #------------logo---------------#

        img2 = Image.open("images/pic2.png")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        labeling2 = Label(self.root, image=self.photoimage2, bd=4, relief=RIDGE)
        labeling2.place(x=0, y=0, width=230, height=140)

        #------------title---------------#

        label_ti = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        label_ti.place(x=0, y=140, width=1550, height=50)

        #------------main_frame---------#

        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        #------------menu---------------#
        label_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        label_menu.place(x=0, y=0, width=230)

        #------------btn frame---------#

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=("times new roman", 22, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.roombooking,width=22, font=("times new roman", 22, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22, font=("times new roman", 22, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 22, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        log_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 22, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        log_btn.grid(row=4, column=0, pady=1)

        #------------Right-side-image------------------#

        img3 = Image.open("images/pic5.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        labeling3 = Label(main_frame, image=self.photoimage3, bd=4, relief=RIDGE)
        labeling3.place(x=225, y=0, width=1310, height=590)

        #===================down images=====================

        img4 = Image.open("images/pic5.jpg")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img4)
        labeling4 = Label(main_frame, image=self.photoimage4, bd=4, relief=RIDGE)
        labeling4.place(x=0, y=225, width=230, height=210)

        img5 = Image.open("images/pic5.jpg")
        img5 = img5.resize((230, 190), Image.LANCZOS)
        self.photoimage5 = ImageTk.PhotoImage(img5)
        labeling5 = Label(main_frame, image=self.photoimage5, bd=4, relief=RIDGE)
        labeling5.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
