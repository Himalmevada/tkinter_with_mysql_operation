from tkinter import *
from tkinter.messagebox import *
import mysql.connector
from functools import partial

def call_value(emp_name,emp_city,emp_country):
    name = emp_name.get()
    city = emp_city.get()
    country = emp_country.get()
    
    if (len(name.strip()) == 0) or (len(city.strip()) == 0) or (len(country.strip()) == 0):
        return showerror(title="Error",message="All fields are required.")
    try:
        conn = mysql.connector.connect(host="localhost",user="root",password="",database="bank_data")
        cursor = conn.cursor()

        query = "insert into emp(e_name,e_city,e_country) values(%s,%s,%s)"
        val = (name,city,country)
        cursor.execute(query,val)
        conn.commit()
        showinfo("Success","Data added successfully.")
        
    except Exception as e:
        print("Something wrong!",e)
        

top = Tk()
top.geometry("270x290")

menubar = Menu(top)

file = Menu(menubar,tearoff=0)
file.add_command(label="New")
file.add_command(label="Save")
file.add_command(label="Save As")

edit= Menu(menubar,tearoff=0)
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")

menubar.add_cascade(label="File",menu=file)
menubar.add_cascade(label="Edit",menu=edit)

top.config(menu=menubar)

emp_name = Label(top,text="Name").place(x=30,y=60)
emp_city = Label(top,text="Email").place(x=30,y=90)
emp_country = Label(top,text="Country").place(x=30,y=120)

# StringVar() creates a string variable which holds the string values.
e_name_str = StringVar()
e_city_str = StringVar()
e_country_str = StringVar()

e_name = Entry(top,textvariable=e_name_str).place(x=90,y=60)
e_city = Entry(top,textvariable=e_city_str).place(x=90,y=90)
e_country = Entry(top,textvariable=e_country_str).place(x=90,y=120)


# we need to send this string data into submit button to do some operations.
# partial function fixes the argument of function and gives new function. 
call_value = partial(call_value,e_name_str,e_city_str,e_country_str)

submit_btn = Button(top,text="Submit",command=call_value).place(x=90,y=160)

top.mainloop()