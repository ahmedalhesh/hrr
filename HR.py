import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# إنشاء قاعدة بيانات SQLite3
conn = sqlite3.connect('employees.db')
c = conn.cursor()

# إنشاء جدول الموظفين
c.execute('''CREATE TABLE IF NOT EXISTS employees
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              phone TEXT,
              job_number TEXT,
              hire_date TEXT,
              job_title TEXT,
              job_grade TEXT,
              qualification TEXT,
              leave_balance INTEGER,
              entitlement_balance INTEGER)''')

# إضافة موظف جديد
def add_employee():
    add_window = Toplevel(root)
    add_window.title("Add Employee")

    name_label = Label(add_window, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = Entry(add_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    phone_label = Label(add_window, text="Phone:")
    phone_label.grid(row=1, column=0, padx=5, pady=5)
    phone_entry = Entry(add_window)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)

    job_number_label = Label(add_window, text="Job Number:")
    job_number_label.grid(row=2, column=0, padx=5, pady=5)
    job_number_entry = Entry(add_window)
    job_number_entry.grid(row=2, column=1, padx=5, pady=5)

    hire_date_label = Label(add_window, text="Hire Date:")
    hire_date_label.grid(row=3, column=0, padx=5, pady=5)
    hire_date_entry = Entry(add_window)
    hire_date_entry.grid(row=3, column=1, padx=5, pady=5)

    job_title_label = Label(add_window, text="Job Title:")
    job_title_label.grid(row=4, column=0, padx=5, pady=5)
    job_title_entry = Entry(add_window)
    job_title_entry.grid(row=4, column=1, padx=5, pady=5)

    job_grade_label = Label(add_window, text="Job Grade:")
    job_grade_label.grid(row=5, column=0, padx=5, pady=5)
    job_grade_entry = Entry(add_window)
    job_grade_entry.grid(row=5, column=1, padx=5, pady=5)

    qualification_label = Label(add_window, text="Qualification:")
    qualification_label.grid(row=6, column=0, padx=5, pady=5)
    qualification_entry = Entry(add_window)
    qualification_entry.grid(row=6, column=1, padx=5, pady=5)

    leave_balance_label = Label(add_window, text="Leave Balance:")
    leave_balance_label.grid(row=7, column=0, padx=5, pady=5)
    leave_balance_entry = Entry(add_window)
    leave_balance_entry.grid(row=7, column=1, padx=5, pady=5)

    entitlement_balance_label = Label(add_window, text="Entitlement Balance:")
    entitlement_balance_label.grid(row=8, column=0, padx=5, pady=5)
    entitlement_balance_entry = Entry(add_window)
    entitlement_balance_entry.grid(row=8, column=1, padx=5, pady=5)

    # إضافة موظف جديد إلى قاعدة البيانات
    def save_employee():
        name = name_entry.get()
        phone = phone_entry.get()
        job_number = job_number_entry.get()
        hire_date = hire_date_entry.get()
        job_title = job_title_entry.get()
        job_grade = job_grade_entry.get()
        qualification = qualification_entry.get()
        leave_balance = leave_balance_entry.get()
        entitlement_balance = entitlement_balance_entry.get()
        c.execute('''INSERT INTO employees (name, phone, job_number, hire_date, job_title, job_grade, qualification, leave_balance, entitlement_balance)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (name, phone, job_number, hire_date, job_title, job_grade, qualification, leave_balance, entitlement_balance))
        conn.commit()
        messagebox.showinfo("Success", "Employee added successfully.")
        add_window.destroy()
        update_table()

    save_button = Button(add_window, text="Save", command=save_employee)
    save_button.grid(row=9, column=0, padx=5, pady=5)

# تعديل بيانات الموظف
def edit_employee():
    selected_item = tree.focus()
    if selected_item:
        edit_window = Toplevel(root)
        edit_window.title("Edit Employee")

        name_label = Label(edit_window, text="Name:")
        name_label.grid(row=0, column=0, padx=5, pady=5)
        name_entry = Entry(edit_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        phone_label = Label(edit_window, text="Phone:")
        phone_label.grid(row=1, column=0, padx=5, pady=5)
        phone_entry = Entry(edit_window)
        phone_entry.grid(row=1, column=1, padx=5, pady=5)

        job_number_label = Label(edit_window, text="Job Number:")
        job_number_label.grid(row=2, column=0, padx=5, pady=5)
        job_number_entry = Entry(edit_window)
        job_number_entry.grid(row=2, column=1, padx=5, pady=5)

        hire_date_label = Label(edit_window, text="Hire Date:")
        hire_date_label.grid(row=3, column=0, padx=5, pady=5)
        hire_date_entry = Entry(edit_window)
        hire_date_entry.grid(row=3, column=1, padx=5, pady=5)

        job_title_label = Label(edit_window, text="Job Title:")
        job_title_label.grid(row=4, column=0, padx=5, pady=5)
        job_title_entry = Entry(edit_window)
        job_title_entry.grid(row=4, column=1, padx=5, pady=5)

        job_grade_label = Label(edit_window, text="Job Grade:")
        job_grade_label.grid(row=5, column=0, padx=5, pady=5)
        job_grade_entry = Entry(edit_window)
        job_grade_entry.grid(row=5, column=1, padx=5, pady=5)

        qualification_label = Label(edit_window, text="Qualification:")
        qualification_label.grid(row=6, column=0, padx=5, pady=5)
        qualification_entry = Entry(edit_window)
        qualification_entry.grid(row=6, column=1, padx=5, pady=5)

        leave_balance_label = Label(edit_window, text="Leave Balance:")
        leave_balance_label.grid(row=7, column=0, padx=5, pady=5)
        leave_balance_entry = Entry(edit_window)
        leave_balance_entry.grid(row=7, column=1, padx=5, pady=5)

        entitlement_balance_label = Label(edit_window, text="Entitlement Balance:")
        entitlement_balance_label.grid(row=8, column=0, padx=5, pady=5)
        entitlement_balance_entry = Entry(edit_window)
        entitlement_balance_entry.grid(row=8, column=1, padx=5, pady=5)

        # ملء حقول الإدخال ببيانات الموظف المحدد
        values = tree.item(selected_item)['values']
        name_entry.insert(0, values[0])
        phone_entry.insert(0, values[1])
        job_number_entry.insert(0, values[2])
        hire_date_entry.insert(0, values[3])
        job_title_entry.insert(0, values[4])
        job_grade_entry.insert(0, values[5])
        qualification_entry.insert(0, values[6])
        leave_balance_entry.insert(0, values[7])
        entitlement_balance_entry.insert(0, values[8])

        # تحديث بيانات الموظف المحدد
        def update_employee():
            name = name_entry.get()
            phone = phone_entry.get()
            job_number = job_number_entry.get()
            hire_date = hire_date_entry.get()
            job_title = job_title_entry.get()
            job_grade = job_grade_entry.get()
            qualification = qualification_entry.get()
            leave_balance = leave_balance_entry.get()
            entitlement_balance = entitlement_balance_entry.get()
            c.execute('''UPDATE employees SET name=?, phone=?, job_number=?, hire_date=?, job_title=?, job_grade=?, qualification=?, leave_balance=?, entitlement_balance=?
                         WHERE id=?''', (name, phone, job_number, hire_date, job_title, job_grade, qualification, leave_balance, entitlement_balance, tree.item(selected_item)['text']))
            conn.commit()
            messagebox.showinfo("Success", "Employee updated successfully.")
            edit_window.destroy()
            update_table()

        save_button = Button(edit_window, text="Save", command=update_employee)
        save_button.grid(row=9, column=0, padx=5, pady=5)

# حذف موظف
def delete_employee():
    selected_item = tree.focus()
    if selected_item:
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this employee?")
        if confirm:
            c.execute('''DELETE FROM employees WHERE id=?''', (tree.item(selected_item)['text'],))
            conn.commit()
            messagebox.showinfo("Success", "Employee deleted successfully.")
            update_table()

# عرض بيانات الموظفين
def view_employees():
    update_table()

# إضافة الإجازات والاستحقاقات
def add_leave_entitlement():
    add_window = Toplevel(root)
    add_window.title("Add Leave/Entitlement")

    name_label = Label(add_window, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_var = StringVar()
    name_dropdown = ttk.Combobox(add_window, textvariable=name_var)
    name_dropdown.grid(row=0, column=1, padx=5, pady=5)

    # استرداد أسماء الموظفين من قاعدة البيانات
    c.execute('''SELECT name FROM employees''')
    rows = c.fetchall()
    names = [row[0] for row in rows]
    name_dropdown['values'] = names

    leave_balance_label = Label(add_window, text="Leave Balance:")
    leave_balance_label.grid(row=1, column=0, padx=5, pady=5)
    leave_balance_entry = Entry(add_window)
    leave_balance_entry.grid(row=1, column=1, padx=5, pady=5)

    entitlement_balance_label = Label(add_window, text="Entitlement Balance:")
    entitlement_balance_label.grid(row=2, column=0, padx=5, pady=5)
    entitlement_balance_entry = Entry(add_window)
    entitlement_balance_entry.grid(row=2, column=1, padx=5, pady=5)

    # إضافة الإجازات والاستحقاقات إلى قاعدة البيانات
    def save_leave_entitlement():
        name = name_var.get()
        leave_balance = leave_balance_entry.get()
        entitlement_balance = entitlement_balance_entry.get()
        c.execute('''UPDATE employees SET leave_balance=?, entitlement_balance=?
                     WHERE name=?''', (leave_balance, entitlement_balance, name))
        conn.commit()
        messagebox.showinfo("Success", "Leave/Entitlement added successfully.")
        add_window.destroy()
        update_table()

    save_button = Button(add_window, text="Save", command=save_leave_entitlement)
    save_button.grid(row=3, column=0, padx=5, pady=5)

# إنشاء واجهة المستخدم
root = Tk()
root.title("Employee Management System")

# إضافة شريط التنقل
menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

add_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Add", menu=add_menu)
add_menu.add_command(label="Employee", command=add_employee)
add_menu.add_command(label="Leave/Entitlement", command=add_leave_entitlement)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Employee", command=edit_employee)

delete_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Delete", menu=delete_menu)
delete_menu.add_command(label="Employee", command=delete_employee)

# إضافة جدول البيانات
data_frame = LabelFrame(root, text="Employee Data")
data_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

tree = ttk.Treeview(data_frame, columns=("name", "phone", "job_number", "hire_date", "job_title", "job_grade", "qualification", "leave_balance", "entitlement_balance"))
tree.heading("#0", text="ID")
tree.heading("name", text="Name")
tree.heading("phone", text="Phone")
tree.heading("job_number", text="Job Number")
tree.heading("hire_date", text="Hire Date")
tree.heading("job_title", text="Job Title")
tree.heading("job_grade", text="Job Grade")
tree.heading("qualification", text="Qualification")
tree.heading("leave_balance", text="Leave Balance")
tree.heading("entitlement_balance", text="Entitlement Balance")
tree.column("#0", width=50)
tree.column("name", width=100)
tree.column("phone", width=100)
tree.column("job_number", width=100)
tree.column("hire_date", width=100)
tree.column("job_title", width=100)
tree.column("job_grade", width=100)
tree.column("qualification", width=100)
tree.column("leave_balance", width=100)
tree.column("entitlement_balance", width=100)
tree.pack(fill=BOTH, expand=True)

# تحديث جدول البيانات
def update_table():
    tree.delete(*tree.get_children())
    c.execute('''SELECT * FROM employees''')
    rows = c.fetchall()
    for row in rows:
        tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

update_table()

# تعيين الوزن لكل عمود وصف
root.columnconfigure(0, weight=1)
data_frame.columnconfigure(0, weight=1)
data_frame.rowconfigure(1, weight=1)



# تشغيل الواجهة
root.geometry("800x600")
root.minsize(400, 300)
root.mainloop()
