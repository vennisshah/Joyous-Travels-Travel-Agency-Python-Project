import sqlite3
from tkinter import *
from tkinter import messagebox
    
root=Tk()
root.title("TRAVEL AGENCY")
root.geometry("1500x1000")
canvas = Canvas(root,width = 1000, height = 1000,bg="black")
img = PhotoImage(file="img3.png")      
canvas.create_image(0,0, anchor=NW, image=img)
imga = PhotoImage(file="img9.png")
imgb = PhotoImage(file="img8.png")
imgc = PhotoImage(file="img10.png")
imgd = PhotoImage(file="img11.png")
imge = PhotoImage(file="img12.png")
imgf = PhotoImage(file="img13.png")
img1 = PhotoImage(file="img2.png")      
canvas.create_image(850,75, anchor=W, image=img1,activeimage=imge)
img2 = PhotoImage(file="img1.png")      
canvas.create_image(850,350, anchor=NW, image=img2,activeimage=imgf)
img3 = PhotoImage(file="img4.png")      
canvas.create_image(950,170, anchor=NW, image=img3,activeimage=imgb)
img4 = PhotoImage(file="img5.png")      
canvas.create_image(850,170, anchor=NW, image=img4,activeimage=imgd)
img5 = PhotoImage(file="img6.png")      
canvas.create_image(1155,0, anchor=NW, image=img5,activeimage=imgc)
img6 = PhotoImage(file="img7.png")      
canvas.create_image(1215,163, anchor=NW, image=img6,activeimage=imga)
id=canvas.create_text(400,300,text="JOYOUS TRAVELS",font=('arial',55),fill="black")
id=canvas.create_text(1300,675,text="*T & C apply",font=('arial',12),fill="white")
id=canvas.create_text(95,650,text='''BON  VOYAGE!!!''',font=('arial',16,'italic'),fill="cyan")
id=canvas.create_text(400,375,text='''"TRAVEL\nis literally the language of life"''',font=('arial',20,'italic'),fill="blue")

conn=sqlite3.connect('JOYOUS.db')
cur=conn.cursor()
cur.execute('''create table if NOT EXISTS User(Name VARCHAR(20),Age INT,Contact INT,Id INT UNIQUE)''')
print("Table User created...")
cur.execute('''create table if NOT EXISTS Airways(Id INT UNIQUE, Adults INT, Children INT, Type Varchar(20),
            Class INT, Source VARCHAR(20), Destination VARCHAR(20), Date VARCHAR(20), Payment_method VARCHAR(20))''')
print("Table Airways created...")
cur.execute('''create table if NOT EXISTS Railways(Id INT UNIQUE, Adults INT, Children INT,
            Class INT, Source VARCHAR(20), Destination VARCHAR(20), Date VARCHAR(20), Payment_method VARCHAR(20))''')
print("Table Railways created...")
cur.execute('''create table if NOT EXISTS Roadways(Id INT UNIQUE, No_of_passengers INT,
            Class INT, Source VARCHAR(20), Destination VARCHAR(20), Date VARCHAR(20), Payment_method VARCHAR(20))''')
print("Table Roadways created...")


view_id=IntVar()
ro_id=IntVar()
rop=IntVar()
roclass=StringVar()
ros=StringVar()
rod=StringVar()
rodate=StringVar()
default5=StringVar()
default6=StringVar()
rail_id=IntVar()
ra=IntVar()
rc=IntVar()
rs=StringVar()
rd=StringVar()
rdate=StringVar()
default3=StringVar()
default4=StringVar()
USERNAME=StringVar()
Age=IntVar()
Contact=IntVar()
Id=IntVar()
Air_Id=IntVar()
Adults=IntVar()
Child=IntVar()
Type=IntVar()
Class=IntVar()
Source=StringVar()
Destination=StringVar()
Date=IntVar()
Pymt_mtd=StringVar()
v=IntVar()
default1=StringVar()
default2=StringVar()
view_id=IntVar()
cancel_id=IntVar()
v1=IntVar()
def login():
    login= Toplevel(bg="cyan")
    login.title("Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    login.resizable(0, 0)
    login.geometry("%dx%d+%d+%d" % (width, height, x, y))
    user_details = Label(login, text="User Details:\t\t\t\t", font=('arial', 20), relief=RAISED)
    user_details.pack()
    l1=Label(login,text="Name:",font=('arial', 15))
    l1.pack()
    v1=StringVar()
    e1=Entry(login, textvariable=USERNAME)
    e1.pack()
    l2=Label(login, text="Age:", font=('arial',15))
    l2.pack()
    v2=StringVar()
    e2=Entry(login, textvariable=Age)
    e2.pack()
    l3=Label(login, text="Contact", font=('arial',15))
    l3.pack()
    v3=StringVar()
    e3=Entry(login, textvariable=Contact)
    e3.pack()
    l4=Label(login, text="User ID:(eg.s@123)", font=('arial',15))
    l4.pack()
    v4=StringVar()
    e4=Entry(login, textvariable=Id)
    e4.pack()
    def execute():

        
        cur.execute('''insert into 'User' (Name,Age,Contact,Id) values(?,?,?,?)''',(USERNAME.get(),Age.get(),Contact.get(),Id.get()))
        conn.commit()
        USERNAME.set("")
        Age.set("")
        Contact.set("")
        Id.set("")
        cur.execute('''select * from User''')
        for row in cur:
            print(row)
        hello()
    def hello():
        messagebox.showinfo("Message",'''You have successfully created your id''')
    b1=Button(login, text="Login",command=execute)
    b1.pack()
    login()
def loginids():    #cancel
    login= Toplevel(bg="cyan")
    login.title("Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    login.resizable(0, 0)
    login.geometry("%dx%d+%d+%d" % (width, height, x, y))
    user_details = Label(login, text="User Details:\t\t\t\t", font=('arial', 20), relief=RAISED)
    user_details.pack()
    l1=Label(login, text="Enter User ID.:", font=('arial',15))
    l1.pack()
    cancel_id=IntVar()
    e1=Entry(login, textvariable=cancel_id,show='*')
    e1.pack()
    cancel_id.set("")
    def hello():
        ans=messagebox.askquestion("Confirm","Are you sure your want to cancel all your bookings?")
        if ans=="yes":
            L2='delete from User where Id=%d' %cancel_id.get()
            cur.execute(L2)
            L='delete from Airways where Id=%d' %cancel_id.get()
            cur.execute(L)
            L1='delete from Railways where Id=%d' %cancel_id.get()
            cur.execute(L1)
            l='delete from Roadways where Id=%d' %cancel_id.get()
            cur.execute(L)
            print("Account deleted!")
            messagebox.showinfo("Account","Your bookings have been cancelled!")
    b1=Button(login, text="Enter",command=hello)
    b1.pack()
    login()
R1=IntVar()
R2=IntVar()
R3=IntVar()
v1=IntVar()
def loginid():   #view
    login= Toplevel(bg="cyan")
    login.title("Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    login.resizable(0, 0)
    login.geometry("%dx%d+%d+%d" % (width, height, x, y))
    choice = Label(login, text="Mode of Travel?\t\t",font=('arial',20),relief=RAISED)
    R1=Radiobutton(login,text="Airways",variable=v1,value=1,font=('arial',15)).pack()
    R2=Radiobutton(login,text="Railways",variable=v1,value=2, font=('arial',15)).pack()
    R3=Radiobutton(login,text="Roadways",variable=v1,value=3,font=('arial',15)).pack()
    user_details = Label(login, text="User Details:\t\t\t\t", font=('arial', 20), relief=RAISED)
    user_details.pack()
    l1=Label(login, text="Enter User ID:", font=('arial',15))
    l1.pack()
    
    e1=Entry(login, textvariable=view_id,show='*')
    e1.pack()
    def hello():
        login= Toplevel(bg="cyan")
        login.title("Ticket")
        width = 600
        height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        login.resizable(0, 0)
        login.geometry("%dx%d+%d+%d" % (width, height, x, y))
        user_details = Label(login, text="Traveller Details:\t\t\t\t", font=('arial', 20), relief=RAISED)
        user_details.pack()
        n1=StringVar()
        L1='select Name from User where Id=%d' %view_id.get()
        cur.execute(L1)
        n1=cur.fetchall()
        l1=Label(login, text="Your name is : "+str(n1),font=('arial',15))
        l1.pack()
        if (v1.get())==1:
            L2='select Date from Airways where Id=%d' %view_id.get()
            cur.execute(L2)
            n2=StringVar()
            n2=cur.fetchall()
            l2=Label(login, text="Your date of travel is : "+str(n2), font=('arial',15))
            l2.pack()
            L3='select Adults from Airways where Id=%d' %view_id.get()
            cur.execute(L3)
            n3=StringVar()
            n3=cur.fetchall()
            l3=Label(login, text="Number of adult passengers are : "+str(n3), font=('arial',15))
            l3.pack()
            L4='select Children from Airways where Id=%d' %view_id.get()
            cur.execute(L4)
            n4=StringVar()
            n4=cur.fetchall()
            l4=Label(login, text="Number of child passengers are : "+str(n4), font=('arial',15))
            l4.pack()
            L5='select Source from Airways where Id=%d' %view_id.get()
            cur.execute(L5)
            n5=StringVar()
            n5=cur.fetchall()
            l5=Label(login, text="Your source is : "+str(n5), font=('arial',15))
            l5.pack()
            L6='select Destination from Airways where Id=%d' %view_id.get()
            cur.execute(L6)
            n6=StringVar()
            n6=cur.fetchall()
            l6=Label(login, text="Your destination is : "+str(n6), font=('arial',15))
            l6.pack()
            L7='select Class from Airways where Id=%d' %view_id.get()
            cur.execute(L7)
            n7=StringVar()
            n7=cur.fetchall()
            l7=Label(login, text="Your class of travel is : "+str(n7), font=('arial',15))
            l7.pack()
            
        elif (v1.get())==2:
            L2='select Date from Railways where Id=%d' %view_id.get()
            cur.execute(L2)
            n2=StringVar()
            n2=cur.fetchall()
            l2=Label(login, text="Your date of travel is : "+str(n2), font=('arial',15))
            l2.pack()
            L3='select Adults from Railways where Id=%d' %view_id.get()
            cur.execute(L3)
            n3=StringVar()
            n3=cur.fetchall()
            l3=Label(login, text="Number of adult passengers are : "+str(n3), font=('arial',15))
            l3.pack()
            L4='select Children from Railways where Id=%d' %view_id.get()
            cur.execute(L4)
            n4=StringVar()
            n4=cur.fetchall()
            l4=Label(login, text="Number of child passengers are : "+str(n4), font=('arial',15))
            l4.pack()
            L5='select Source from Railways where Id=%d' %view_id.get()
            cur.execute(L5)
            n5=StringVar()
            n5=cur.fetchall()
            l5=Label(login, text="Your source is : "+str(n5), font=('arial',15))
            l5.pack()
            L6='select Destination from Railways where Id=%d' %view_id.get()
            cur.execute(L6)
            n6=StringVar()
            n6=cur.fetchall()
            l6=Label(login, text="Your destination is : "+str(n6), font=('arial',15))
            l6.pack()
            L7='select Class from Railways where Id=%d' %view_id.get()
            cur.execute(L7)
            n7=StringVar()
            n7=cur.fetchall()
            l7=Label(login, text="Your class of travel is : "+str(n7), font=('arial',15))
            l7.pack()
        else:
            L2='select Date from Roadways where Id=%d' %view_id.get()
            cur.execute(L2)
            n2=StringVar()
            n2=cur.fetchall()
            l2=Label(login, text="Your date of travel is : "+str(n2), font=('arial',15))
            l2.pack()
            L3='select No_of_passengers from Roadways where Id=%d' %view_id.get()
            cur.execute(L3)
            n3=StringVar()
            n3=cur.fetchall()
            l3=Label(login, text="Number of passengers are : "+str(n3), font=('arial',15))
            l3.pack()
            L5='select Source from Roadways where Id=%d' %view_id.get()
            cur.execute(L5)
            n5=StringVar()
            n5=cur.fetchall()
            l5=Label(login, text="Your source is : "+str(n5), font=('arial',15))
            l5.pack()
            L6='select Destination from Roadways where Id=%d' %view_id.get()
            cur.execute(L6)
            n6=StringVar()
            n6=cur.fetchall()
            l6=Label(login, text="Your destination is : "+str(n6), font=('arial',15))
            l6.pack()
            L7='select Class from Roadways where Id=%d' %view_id.get()
            cur.execute(L7)
            n7=StringVar()
            n7=cur.fetchall()
            l7=Label(login, text="Your class of travel is : "+str(n7), font=('arial',15))
            l7.pack()
    b1=Button(login, text="Enter",command=hello)
    b1.pack()
    login()

def ShowAirlines():
    Airlines= Toplevel(bg="cyan")
    Airlines.title("Airlines")
    width = 600
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Airlines.resizable(0, 0)
    Airlines.geometry("%dx%d+%d+%d" % (width, height, x, y))
    
    l=Label(Airlines, text="Booking Details", font=('arial',20),relief=RAISED)
    l.pack()
    ll=Label(Airlines, text="Enter User ID:", font=('arial',15))
    ll.pack()
    v1=StringVar()
    el=Entry(Airlines, textvariable=Air_Id)
    el.pack()
    l1=Label(Airlines, text="Number of adult passengers", font=('arial',15))
    l1.pack()
    v2=StringVar()
    e1=Entry(Airlines, textvariable=Adults)
    e1.pack()
    l2=Label(Airlines, text="Number of child passengers(Below 5 years)", font=('arial',15))
    l2.pack()
    v3=StringVar()
    e2=Entry(Airlines, textvariable=Child)
    e2.pack()
    
    v4=StringVar()
    r1=Radiobutton(Airlines,text="Domestic",variable=v,value=1,font=('arial',15)).pack()
    r2=Radiobutton(Airlines,text="International",variable=v,value=2, font=('arial',15)).pack()
    l3=Label(Airlines, text="Class of Travel", font=('arial',15))
    default1=StringVar(Airlines)
    default1.set("Economic")
    l3.pack()
    v5=StringVar()
    menu1=OptionMenu(Airlines, default1, "Economic", "Business", "First")
    menu1.pack()
    l4=Label(Airlines, text="Source", font=('arial',15))
    l4.pack()
    v6=StringVar()
    e4=Entry(Airlines, textvariable=Source)
    e4.pack()
    l5=Label(Airlines, text="Destination", font=('arial',15))
    l5.pack()
    v7=StringVar()
    e5=Entry(Airlines, textvariable=Destination)
    e5.pack()
    l6=Label(Airlines, text="Date of travel", font=('arial',15))
    l6.pack()
    v8=StringVar()
    e6=Entry(Airlines, textvariable=Date)
    e6.pack()
    l7=Label(Airlines, text="Payment method", font=('arial',15))
    l7.pack()
    v9=StringVar()
    default2=StringVar(Airlines)
    default2.set("Credit Card")
    menu2=OptionMenu(Airlines, default2, "Credit Card", "Debit Card")
    menu2.pack()
    def execute():
        cur.execute('''insert into 'Airways' (Id,Adults,Children,Type,Class,Source,Destination,Date,Payment_method) values(?,?,?,?,?,?,?,?,?)''',(Air_Id.get(),Adults.get(),Child.get(),v.get(),default1.get(),Source.get(),Destination.get(),Date.get(),default2.get()))
        conn.commit()
        Air_Id.set("")
        Adults.set("")
        Child.set("")
        Type.set("")
        Class.set("")
        Source.set("")
        Destination.set("")
        Date.set("")
        Pymt_mtd.set("")
        cur.execute('''select * from Airways''')
        for r in cur:
            print(r)
        hello()
    def hello():
        messagebox.showinfo("Message",'''Your booking is successful!!\nCheck your Tickets in the "View Tickets" section.''')
    button=Button(Airlines, text="\n   BOOK   \n",command=execute)
    button.pack()
    Airlines()
def ShowRailways():
    Railways= Toplevel(bg="yellow")
    Railways.title("Railways")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Railways.resizable(0, 0)
    Railways.geometry("%dx%d+%d+%d" % (width, height, x, y))
    
    l=Label(Railways, text="Booking Details", font=('arial',20),relief=RAISED)
    l.pack()
    la=Label(Railways, text="Enter User ID:", font=('arial',15))
    la.pack()
    ea=Entry(Railways, textvariable=rail_id)
    ea.pack()
    l1=Label(Railways, text="Number of  passengers", font=('arial',15))
    l1.pack()
    e1=Entry(Railways, textvariable=ra)
    e1.pack()
    l2=Label(Railways, text="Number of child passengers(Below 5 years)", font=('arial',15))
    l2.pack()
    e2=Entry(Railways, textvariable=rc)
    e2.pack()
    l3=Label(Railways, text="Class of Travel", font=('arial',15))
    default3=StringVar(Railways)
    default3.set("Sleeper")
    l3.pack()
    menu1=OptionMenu(Railways, default3, "First", "Sleeper", "AC 3-Tier", "AC Chair Car")
    menu1.pack()
    l4=Label(Railways, text="Source", font=('arial',15))
    l4.pack()
    e4=Entry(Railways, textvariable=rs)
    e4.pack()
    l5=Label(Railways, text="Destination", font=('arial',15))
    l5.pack()
    e5=Entry(Railways, textvariable=rd)
    e5.pack()
    l6=Label(Railways, text="Date of travel", font=('arial',15))
    l6.pack()
    e6=Entry(Railways, textvariable=rdate)
    e6.pack()
    l7=Label(Railways, text="Payment method", font=('arial',15))
    l7.pack()
    default4=StringVar(Railways)
    default4.set("Credit Card")
    menu2=OptionMenu(Railways, default4, "Credit Card", "Debit Card")
    menu2.pack()
    def execute():
        cur.execute('''insert into 'Railways' (Id,Adults,Children,Class,Source,Destination,Date,Payment_method) values(?,?,?,?,?,?,?,?)''',(rail_id.get(),ra.get(),rc.get(),default3.get(),rs.get(),rd.get(),rdate.get(),default4.get()))
        conn.commit()
        rail_id.set("")
        ra.set("")
        rc.set("")
        ra.set("")
        rd.set("")
        rdate.set("")
        cur.execute('''select * from Railways''')
        for r in cur:
            print(r)
        hello()
    def hello():
        messagebox.showinfo("Message",'''Your booking is successful!!\nCheck your Tickets in the "View Tickets" section.''')
    button=Button(Railways, text="\n   BOOK   \n",command=execute)
    button.pack()
    Railways()
def ShowRoadways():
    
    Roadways= Toplevel(bg="orange")
    Roadways.title("Roadways")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Roadways.resizable(0, 0)
    Roadways.geometry("%dx%d+%d+%d" % (width, height, x, y))
    l=Label(Roadways, text="Booking Details", font=('arial',20),relief=RAISED)
    l.pack()
    lb=Label(Roadways, text="Enter User ID:", font=('arial',15))
    lb.pack()
    eb=Entry(Roadways, textvariable=ro_id)
    eb.pack()
    l1=Label(Roadways, text="Number of passengers", font=('arial',15))
    l1.pack()
    e1=Entry(Roadways, textvariable=rop)
    e1.pack()
    l3=Label(Roadways, text="Class of Travel", font=('arial',15))
    default5=StringVar(Roadways)
    default5.set("Regular Seater")
    l3.pack()
    menu1=OptionMenu(Roadways, default5, "Regular Seater", "Regular Sleeper", "AC Seater", "AC Sleeper")
    menu1.pack()
    l4=Label(Roadways, text="Source", font=('arial',15))
    l4.pack()
    e4=Entry(Roadways, textvariable=ros)
    e4.pack()
    l5=Label(Roadways, text="Destination", font=('arial',15))
    l5.pack()
    e5=Entry(Roadways, textvariable=rod)
    e5.pack()
    l6=Label(Roadways, text="Date of travel", font=('arial',15))
    l6.pack()
    e6=Entry(Roadways, textvariable=rodate)
    e6.pack()
    l7=Label(Roadways, text="Payment method", font=('arial',15))
    l7.pack()
    default6=StringVar(Roadways)
    default6.set("Credit Card")
    menu2=OptionMenu(Roadways, default6, "Credit Card", "Debit Card")
    menu2.pack()
    def execute():
        cur.execute('''insert into 'Roadways' (Id,NO_of_passengers,Class,Source,Destination,Date,Payment_method) values(?,?,?,?,?,?,?)''',(ro_id.get(),rop.get(),default5.get(),ros.get(),rod.get(),rodate.get(),default6.get()))
        conn.commit()
        ro_id.set("")
        rop.set("")
        ros.set("")
        rod.set("")
        rodate.set("")
        cur.execute('''select * from Roadways''')
        for r in cur:
            print(r)
        hello()
    def hello():
        messagebox.showinfo("Message",'''Your booking is successful!!\nCheck your Tickets in the "View Tickets" section.''')
    button=Button(Roadways, text="\n   BOOK   \n",command=execute)
    button.pack()
    Roadways()
def ShowCall():
    calls= Toplevel(bg="black")
    calls.title("Contact Details")
    width = 500
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    calls.resizable(0, 0)
    calls.geometry("%dx%d+%d+%d" % (width, height, x, y))
    label=Label(calls, text="  CONTACT DETAILS  ", font=('arial',20), relief=RAISED)
    label.pack()
    text=Text(calls)
    text.insert(INSERT,'''\n->PHONE NO:02288653872\n->MOBILE NO:9675235460\n->MOBILE NO:9565429990\n->FAX NO:022234876509''')
    text.pack()
    calls()
def ShowEmail():
    e= Toplevel(bg="black")
    e.title("Contact Details")
    width = 500
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    e.resizable(0, 0)
    e.geometry("%dx%d+%d+%d" % (width, height, x, y))
    label=Label(e, text="  CONTACT DETAILS  ", font=('arial',20), relief=RAISED)
    label.pack()
    text=Text(e)
    text.insert(INSERT,'''\n->EMAIL ID :joyoustravels@gmail.com''')
    text.pack()
    e()
def ShowTerms():
    Terms= Toplevel(bg="black")
    Terms.title("Terms & Conditions")
    width = 800
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Terms.resizable(0, 0)
    Terms.geometry("%dx%d+%d+%d" % (width, height, x, y))

    
    label=Label(Terms, text="  TERMS & CONDITIONS  ", font=('arial',20), relief=RAISED)
    label.pack()
    text=Text(Terms)
    text.insert(INSERT,'''\n-> Please Carry following documents compulsorily before boarding :
    \n-> Travel Ticket (2 Copies . One copy is retained by us)
    \n-> Photo Identity Card (One Copy - Govt. Approved)
    \n-> Reporting time is 30 minutes before scheduled departure.
    \n-> Management reserves the right to change the seat numbers.
    \n-> Co-Seats of lady passenger to be confirmed to a lady passenger only.
    \n-> Video is an additional facility, not a condition.
    \n-> Ticket is neither transferable, nor refundable.
    \n-> Changes to the origin and/or destination of travel and/or customer name are not permitted on ticket.
    \n-> Ticket cancellation / modification/Refund:
    \n-> Cancellation:
    \n-> Cancellations are not entertained over phone
    \n-> Cancellation charges within 4 hrs - 100%
    \n-> Cancellation charges within 12 hrs - 53%
    \n-> Cancellation charges within 1 days - 28%
    \n-> Cancellation charges before 200 days 14 hrs 40 mins - 13%
    \n-> Partial cancellation is not allowed.
    \n-> Note: 15% service tax extra on cancellation charge amount
    \n-> Cancelled ticket amount is transferred back to the source, which means your credit / debit / net banking / cash card or mobile payment account. The cancelled ticket amount is refunded by the respective bank subject to terms and conditions of the bank. However, if you need any assistance for repayments you can contact our Head office.
    \n-> No-Refund after departure.
    \n-> The refund should be credited in your account within 3-14 working days depending upon your bank.
    \n-> Discount Policies:
    \n-> Ticket should be booked online through www.shrinath.biz
    \n-> Up to Discount 5% subject to maximum Rs.50/per seat
    \n-> Cancellation charges and refund on net of Discount fare
    \n-> Service tax on net of Discount fare
    \n-> Cancelled ticket amount is transferred back to the source, which means your credit / debit / net banking / cash card or mobile payment account. The cancelled ticket amount is refunded by the respective bank subject to terms and conditions of the bank. However, if you need any assistance for repayments you can contact our Head office or mail us at support@shrinath.biz
    \n-> No-Refunds or Complaints will be entertained for passenger waiting for the Bus at an incorrect boarding point. The passenger is requested to confirm the exact boarding point and time with shrinath Travels well in advance.
    \n-> In case AC unit fails, proportionate refund will be paid back from the Head Office.
    \n-> Maximum 20kg of Baggage & Luggage is allowed per passenger. Above 20kgs is chargeable as per policies.
    \n-> Management is not responsible for any loss, theft or damages to the goods or property of the passenger.
    \n-> Luggage & Baggage is carried at your own risk.
    \n-> No Contraband articles are permitted to be carried by any passenger.
    \n-> Management is not responsible for delay and cancellation of trips on account of Breakdown, Accident, Riots etc., and due to any unforeseen circumstances.
    \n-> In case of cancellation of a coach, proportionate refund will be paid back.
    \n-> The coaches and the passengers are covered by insurance. That means, accident and consequential injury and loss of life, are covered in the insurance.
    \n-> In case of coach break-down, management is not responsible for any alternate transport arrangement, though management will try its best to provide another available coach.
    \n-> Pets, Animals, Birds are not permitted in the coach, and if found, the passenger is bound to be alighted (get out) from coach.
    \n-> Smoking and Drinking are not permitted inside the coach.
    \n-> The arrival & departure time mentioned on the ticket are tentative timings and may change due to unforeseen events. The coach will not leave the source before the time that is mentioned on the ticket.
    \n-> Seats Will Be Confirmed Only After Successful Payment. (Depending Upon Seat Availability).
    \n-> Passenger found disturbing the co-passenger, in a logical way, is liable to be alighted from the coach. However for further assistance or complaint please feel free to Contact Us
    \n-> All transaction amount is in INR (Indian National Rupee)
    \n-> All disputes are subject to MUMBAI Jurisdiction.''')
    text.pack()
    Terms()


im = PhotoImage(file="i1.png")
im1=PhotoImage(file="i2.png")
im2=PhotoImage(file="i3.png")
im3=PhotoImage(file="i4.png")
im4=PhotoImage(file="i5.png")
im5=PhotoImage(file="i6.png")
im6=PhotoImage(file="i7.png")
menubar1=Menu(root)
root.configure(menu=menubar1)
lmenu=Menu(menubar1,tearoff=0)
menubar1.add_cascade(label="Login",menu=lmenu)
lmenu.add_cascade(label="Create id",command=login,image=im5,compound=LEFT)
fmenu=Menu(menubar1,tearoff=0)
menubar1.add_cascade(label="Mode",menu=fmenu)
fmenu.add_command(label="Airways",command=ShowAirlines,image=im,compound=LEFT)
fmenu.add_command(label="Roadways",command=ShowRoadways,image=im1,compound=LEFT)
fmenu.add_command(label="Railways",command=ShowRailways,image=im2,compound=LEFT)
vmenu=Menu(menubar1,tearoff=0)
menubar1.add_cascade(label="View Tickets",menu=vmenu)
vmenu.add_command(label="Login",command=loginid,image=im6,compound=LEFT)
cmenu=Menu(menubar1,tearoff=0)
menubar1.add_cascade(label="Cancel Tickets",menu=cmenu)
cmenu.add_command(label="Login",command=loginids,image=im5,compound=LEFT)
tmenu=Menu(menubar1,tearoff=0)
menubar1.add_cascade(label="Terms &Conditions",menu=tmenu)
tmenu.add_command(label="Read",command=ShowTerms)
amenu=Menu(menubar1,tearoff=0)
menubar1.add_cascade(label="Contact",menu=amenu)
amenu.add_command(label="Call",command=ShowCall,image=im3,compound=LEFT)
amenu.add_command(label="Email",command=ShowEmail,image=im4,compound=LEFT)

canvas.pack(expand = 1, fill=BOTH)
root.mainloop()
