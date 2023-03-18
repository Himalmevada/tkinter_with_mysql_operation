from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk

import mysql.connector


top = Tk()
top.geometry("270x290")

conn = mysql.connector.connect(host="localhost",user="root",password="",database="auction")
cursor = conn.cursor()

query = "show tables"
cursor.execute(query)
tables = cursor.fetchall()
table_options = [i[0] for i in tables]

def selected(event):
    
    top2 = Toplevel(top)
    top2.title(f"{clicked.get()} Table")
    
    query = f"desc {clicked.get()}"
    cursor.execute(query)

    cols = cursor.fetchall()
    cols = [i[0] for i in cols]

    query = f"select * from {clicked.get()}"
    cursor.execute(query)

    rows = cursor.fetchall()
    rows.insert(0,cols)
    
    for i in range(len(rows)):
        for j in range(len(cols)):
            e = Entry(top2)
            e.grid(row=i,column=j)
            e.insert(END,rows[i][j])

    # myLabel = Label(top,text=clicked.get()).pack()
    

clicked = StringVar()
clicked.set(table_options[0])

dropdown_select = OptionMenu(top,clicked,*table_options,command=selected).pack(pady=10)

# submit_btn = Button(top,text="Submit",command=selected).pack(pady=10)

top.mainloop()