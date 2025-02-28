import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

college_programs = {
    "COET": [
        "DIPLOMA IN CHEMICAL ENGINEERING TECHNOLOGY",
        "BS IN CIVIL ENGINEERING",
        "BS IN CERAMICS ENGINEERING",
        "BS IN CHEMICAL ENGINEERING",
        "BS IN COMPUTER ENGINEERING",
        "BS IN ELECTRONICS & COMMUNICATIONS ENGINEERING",
        "BS IN ELECTRICAL ENGINEERING",
        "BS IN MINING ENG'G.",
        "BS IN ENVIRONMENTAL ENGINEERING TECHNOLOGY",
        "BS IN MECHANICAL ENGINEERING",
        "BS IN METALLURGICAL ENGINEERING"
    ],
    "CSM": [
        "BS IN BIOLOGY (BOTANY)",
        "BS IN CHEMISTRY",
        "BS IN MATHEMATICS",
        "BS IN PHYSICS",
        "BS IN BIOLOGY (ZOOLOGY)",
        "BS IN BIOLOGY (MARINE)",
        "BS IN BIOLOGY (GENERAL)",
        "BS IN STATISTICS"
    ],
    "CCS": [
        "DIPLOMA IN ELECTRONICS ENGINEERING TECH (Computer Electronics)",
        "BS IN INFORMATION SYSTEMS",
        "BS IN INFORMATION TECHNOLOGY",
        "DIPLOMA IN ELECTRONICS TECHNOLOGY",
        "DIPLOMA IN ELECTRONICS ENGINEERING TECH (Communication Electronics)",
        "BS IN COMPUTER SCIENCE",
        "BS IN ELECTRONICS AND COMPUTER TECHNOLOGY (EMBEDDED SYSTEMS)",
        "BS IN ELECTRONICS AND COMPUTER TECHNOLOGY (COMMUNICATIONS SYSTEM)"
    ],
    "CED": [
        "BACHELOR OF SECONDARY EDUCATION (BIOLOGY)",
        "BS IN INDUSTRIAL EDUCATION (DRAFTING)",
        "BACHELOR OF SECONDARY EDUCATION (CHEMISTRY)",
        "BACHELOR OF SECONDARY EDUCATION (PHYSICS)",
        "BACHELOR OF SECONDARY EDUCATION (MATHEMATICS)",
        "BACHELOR OF SECONDARY EDUCATION (MAPEH)",
        "Certificate Program for Teachers",
        "BACHELOR OF SECONDARY EDUCATION (TLE)",
        "BACHELOR OF SECONDARY EDUCATION (GENERAL SCIENCE)",
        "BACHELOR OF ELEMENTARY EDUCATION (ENGLISH)",
        "BACHELOR OF ELEMENTARY EDUCATION (SCIENCE AND HEALTH)",
        "BS IN TECHNOLOGY TEACHER EDUCATION (INDUSTRIAL TECH)",
        "BS IN TECHNOLOGY TEACHER EDUCATION (DRAFTING TECH)"
    ],
    "CASS": [
        "GENERAL EDUCATION PROGRAM",
        "BA IN ENGLISH",
        "BS IN PSYCHOLOGY",
        "BA IN FILIPINO",
        "BA IN HISTORY",
        "BA IN POLITICAL SCIENCE"
    ],
    "CBAA": [
        "BS IN BUSINESS ADMINISTRATION (BUSINESS ECONOMICS)",
        "BS IN BUSINESS ADMINISTRATION (ECONOMICS)",
        "BS IN BUSINESS ADMINISTRATION (ENTREPRENEURIAL MARKETING)",
        "BS IN HOTEL AND RESTAURANT MANAGEMENT",
        "BS IN ACCOUNTANCY"
    ],
    "CHS": [
        "BS IN NURSING"
    ]
}
college_mapping = {
    "College of Engineering and Technology": "COET",
    "College of Science and Mathematics": "CSM",
    "College of Computer Studies": "CCS",
    "College of Education": "CED",
    "College of Arts and Science": "CASS",
    "College of Business Administration & Accountancy": "CBAA",
    "College of Nursing": "CHS"
}

program_codes = {
    "DIPLOMA IN CHEMICAL ENGINEERING TECHNOLOGY": "DCET",
    "BS IN CIVIL ENGINEERING": "BSCE",
    "BS IN CERAMICS ENGINEERING": "BSCR",
    "BS IN CHEMICAL ENGINEERING": "BSChE",
    "BS IN COMPUTER ENGINEERING": "BSCpE",
    "BS IN ELECTRONICS & COMMUNICATIONS ENGINEERING": "BSECE",
    "BS IN ELECTRICAL ENGINEERING": "BSEE",
    "BS IN MINING ENG'G.": "BSME",
    "BS IN ENVIRONMENTAL ENGINEERING TECHNOLOGY": "BSEET",
    "BS IN MECHANICAL ENGINEERING": "BSME",
    "BS IN METALLURGICAL ENGINEERING": "BSMetE",
    "BS IN BIOLOGY (BOTANY)": "BSB",
    "BS IN CHEMISTRY": "BSC",
    "BS IN MATHEMATICS": "BSM",
    "BS IN PHYSICS": "BSP",
    "BS IN BIOLOGY (ZOOLOGY)": "BSBZ",
    "BS IN BIOLOGY (MARINE)": "BSBM",
    "BS IN BIOLOGY (GENERAL)": "BSBG",
    "BS IN STATISTICS": "BSS",
    "DIPLOMA IN ELECTRONICS ENGINEERING TECH (Computer Electronics)": "DEETCE",
    "BS IN INFORMATION SYSTEMS": "BSIS",
    "BS IN INFORMATION TECHNOLOGY": "BSIT",
    "DIPLOMA IN ELECTRONICS TECHNOLOGY": "DET",
    "DIPLOMA IN ELECTRONICS ENGINEERING TECH (Communication Electronics)": "DEETCE",
    "BS IN COMPUTER SCIENCE": "BSCS",
    "BS IN ELECTRONICS AND COMPUTER TECHNOLOGY (EMBEDDED SYSTEMS)": "BSECTES",
    "BS IN ELECTRONICS AND COMPUTER TECHNOLOGY (COMMUNICATIONS SYSTEM)": "BSECTCS",
    "BACHELOR OF SECONDARY EDUCATION (BIOLOGY)": "BSEB",
    "BS IN INDUSTRIAL EDUCATION (DRAFTING)": "BSIED",
    "BACHELOR OF SECONDARY EDUCATION (CHEMISTRY)": "BSEC",
    "BACHELOR OF SECONDARY EDUCATION (PHYSICS)": "BSEP",
    "BACHELOR OF SECONDARY EDUCATION (MATHEMATICS)": "BSEM",
    "BACHELOR OF SECONDARY EDUCATION (MAPEH)": "BSEM",
    "Certificate Program for Teachers": "CPT",
    "BACHELOR OF SECONDARY EDUCATION (TLE)": "BSET",
    "BACHELOR OF SECONDARY EDUCATION (GENERAL SCIENCE)": "BSEGS",
    "BACHELOR OF ELEMENTARY EDUCATION (ENGLISH)": "BEEE",
    "BACHELOR OF ELEMENTARY EDUCATION (SCIENCE AND HEALTH)": "BEESH",
    "BS IN TECHNOLOGY TEACHER EDUCATION (INDUSTRIAL TECH)": "BSTTEIT",
    "BS IN TECHNOLOGY TEACHER EDUCATION (DRAFTING TECH)": "BSTTEDT",
    "GENERAL EDUCATION PROGRAM": "GEP",
    "BA IN ENGLISH": "BAE",
    "BS IN PSYCHOLOGY": "BSP",
    "BA IN FILIPINO": "BAF",
    "BA IN HISTORY": "BAH",
    "BA IN POLITICAL SCIENCE": "BAPS",
    "BS IN BUSINESS ADMINISTRATION (BUSINESS ECONOMICS)": "BSBABE",
    "BS IN BUSINESS ADMINISTRATION (ECONOMICS)": "BSBAE",
    "BS IN BUSINESS ADMINISTRATION (ENTREPRENEURIAL MARKETING)": "BSBAEM",
    "BS IN HOTEL AND RESTAURANT MANAGEMENT": "BSHRM",
    "BS IN ACCOUNTANCY": "BSA",
    "BS IN NURSING": "BSN"
}
import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

def autofill_code(event):
    selected_college = CollName_entry.get()
    if selected_college in college_mapping:
        CollCode_entry.delete(0, END)
        CollCode_entry.insert(0, college_mapping[selected_college])
        program_combobox['values'] = college_programs[college_mapping[selected_college]]

def autofill_program_code(event):
    selected_program = program_combobox.get()
    if selected_program in program_codes:
        ProgCode_entry.delete(0, END)
        ProgCode_entry.insert(0, program_codes[selected_program])

def save_to_csv():
    idnum = idnum_var.get()
    fname = fname_var.get()
    lname = lname_var.get()
    sex = sex_var.get()
    progcode = progcode_var.get()
    year = year_var.get()
    collname = collname_var.get()
    collcode = collcode_var.get()

    if not (idnum and fname and lname and sex and progcode and year and collname and collcode):
        messagebox.showwarning("Input Error", "All fields must be filled out")
        return

    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([idnum, fname, lname, sex, progcode, year, collname, collcode])

    student_info.insert('', 'end', values=(idnum, fname, lname, sex, progcode, year, collname, collcode))

    idnum_var.set("")
    fname_var.set("")
    lname_var.set("")
    sex_var.set("")
    progcode_var.set("")
    year_var.set("")
    collname_var.set("")
    collcode_var.set("")

def load_from_csv():
    try:
        with open('students.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                student_info.insert('', 'end', values=row)
    except FileNotFoundError:
        pass

def delete_selected():
    selected_item = student_info.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "No item selected")
        return

    for item in selected_item:
        student_info.delete(item)

    with open('students.csv', 'r', newline='') as file:
        rows = list(csv.reader(file))

    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if not any(row == student_info.item(item, 'values') for item in selected_item):
                writer.writerow(row)

def update_search_suggestions(event):
    search_term = search_var.get().lower()

    matching_items = []
    for child in student_info.get_children():
        values = student_info.item(child, 'values')
        if any(search_term in str(value).lower() for value in values):
            matching_items.append(child)

    for item in student_info.get_children():
        student_info.detach(item)

    if search_term == "":
        load_from_csv()
    else:
        for item in matching_items:
            student_info.reattach(item, '', 'end')
            student_info.selection_set(item)
            student_info.see(item)

def sort_by_column(column):
    data = [(student_info.set(child, column).strip().lower(), child) for child in student_info.get_children('')]
    data.sort()

    for index, (value, child) in enumerate(data):
        student_info.move(child, '', index)

def validate_idnum(new_value):
    pattern = re.compile(r'^\d{0,4}(-\d{0,4})?$')
    return pattern.match(new_value) is not None

root = Tk()

root.title("Student System Information")
root.geometry("1450x500")

frame = Frame(root, bg="#f0f0f0", bd=5, relief=RIDGE)
frame.place(width=1450, height=500)

# variables

idnum_var = StringVar()
fname_var = StringVar()
lname_var = StringVar()
sex_var = StringVar()
progcode_var = StringVar()
year_var = IntVar()
collname_var = StringVar()
collcode_var = StringVar()
search_var = StringVar()

# Saving student info

StuInfo = LabelFrame(frame, text="Student Information", font=("Arial", 12, "bold"), bg="#e0e0e0", bd=5, relief=RIDGE)
StuInfo.grid(row=0, column=0, sticky="news")

idnum_label = Label(StuInfo, text="ID Number", font=("Arial", 10))
idnum_label.grid(row=0, column=0)
fname_label = Label(StuInfo, text="First Name", font=("Arial", 10))
fname_label.grid(row=0, column=1)
lname_label = Label(StuInfo, text="Last Name", font=("Arial", 10))
lname_label.grid(row=0, column=2)
sex_label = Label(StuInfo, text="Sex", font=("Arial", 10))
sex_label.grid(row=2, column=0)

# student info entry

vcmd = (root.register(validate_idnum), '%P')
idnum_entry = Entry(StuInfo, textvariable=idnum_var, font=("Arial", 10), validate='key', validatecommand=vcmd)
idnum_entry.grid(row=1, column=0)
fname_entry = Entry(StuInfo, textvariable=fname_var, font=("Arial", 10))
fname_entry.grid(row=1, column=1)
lname_entry = Entry(StuInfo, textvariable=lname_var, font=("Arial", 10))
lname_entry.grid(row=1, column=2)
Gender_entry = ttk.Combobox(StuInfo, values=["F", "M"], textvariable=sex_var, font=("Arial", 10), state='readonly')
Gender_entry.grid(row=3, column=0)

for widget in StuInfo.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# saving college info
StuColl = LabelFrame(frame, text="College Information", font=("Arial", 12, "bold"), bg="#e0e0e0", bd=5, relief=RIDGE)
StuColl.grid(row=1, column=0, sticky="news")

CollName_label = Label(StuColl, text="College Name:", font=("Arial", 10))
CollName_label.grid(row=0, column=0)
CollCode_label = Label(StuColl, text="College Code:", font=("Arial", 10))
CollCode_label.grid(row=0, column=2)

# college info entry
CollName_entry = ttk.Combobox(StuColl, values=list(college_mapping.keys()), textvariable=collname_var, font=("Arial", 10), state='readonly')
CollName_entry.grid(row=0, column=1)
CollName_entry.bind("<<ComboboxSelected>>", autofill_code)
CollCode_entry = Entry(StuColl, textvariable=collcode_var, font=("Arial", 10))
CollCode_entry.grid(row=0, column=3)

for widget in StuColl.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# Saving Program Info
StuProg = LabelFrame(frame, text="Program Information", font=("Arial", 12, "bold"), bg="#e0e0e0", bd=5, relief=RIDGE)
StuProg.grid(row=2, column=0, sticky="news")

program_label = Label(StuProg, text="Select Program:", font=("Arial", 10))
program_label.grid(row=0, column=0)
ProgCode_label = Label(StuProg, text="Program Code", font=("Arial", 10))
ProgCode_label.grid(row=1, column=0)
Year_label = Label(StuProg, text="Year Level", font=("Arial", 10))
Year_label.grid(row=2, column=0)

# Program Info
program_combobox = ttk.Combobox(StuProg, values=[], textvariable=progcode_var, font=("Arial", 10), state='readonly')
program_combobox.grid(row=0, column=1)
program_combobox.bind("<<ComboboxSelected>>", autofill_program_code)
ProgCode_entry = Entry(StuProg, textvariable=progcode_var, font=("Arial", 10))
ProgCode_entry.grid(row=1, column=1)
Year_entry = ttk.Combobox(StuProg, values=["1", "2", "3", "4"], textvariable=year_var, font=("Arial", 10), state='readonly')
Year_entry.grid(row=2, column=1)

for widget in StuProg.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# Buttons
button_save = ttk.Button(frame, text="Save", command=save_to_csv, style="TButton")
button_save.grid(row=3, column=0, sticky="news", padx=50, pady=10)

Saved_student = LabelFrame(frame, text="Saved Students", font=("Arial", 12, "bold"), bg="#e0e0e0", bd=5, relief=RIDGE)
Saved_student.place(x=600, y=0, width=840, height=400)
Search_frame = Frame(Saved_student, bg="#e0e0e0")
Search_frame.pack(side=TOP, fill=X)

search_entry = Entry(Search_frame, textvariable=search_var, font=("Arial", 10))
search_entry.grid(row=0, column=0, padx=20)
search_entry.bind('<KeyRelease>', update_search_suggestions)

button_delete = ttk.Button(Search_frame, text="Delete", command=delete_selected, style="TButton")
button_delete.grid(row=0, column=1)

button_sort_id = ttk.Button(Search_frame, text="Sort by ID Number", command=lambda: sort_by_column("ID Number"), style="TButton")
button_sort_id.grid(row=0, column=2)

button_sort_fname = ttk.Button(Search_frame, text="Sort by First Name", command=lambda: sort_by_column("First Name"), style="TButton")
button_sort_fname.grid(row=0, column=3)

button_sort_lname = ttk.Button(Search_frame, text="Sort by Last Name", command=lambda: sort_by_column("Last Name"), style="TButton")
button_sort_lname.grid(row=0, column=4)

Data_frame = Frame(Saved_student, bg="#f0f0f0", bd=5, relief=RIDGE)
Data_frame.pack(side=TOP, fill=BOTH, expand=True)

yscroll = Scrollbar(Data_frame, orient=VERTICAL)
xscroll = Scrollbar(Data_frame, orient=HORIZONTAL)

student_info = ttk.Treeview(Data_frame, columns=("ID Number", "First Name", "Last Name", "Sex", "Program Code", "Year Level", "College Name", "College Code"), yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
yscroll.config(command=student_info.yview)
xscroll.config(command=student_info.xview)

yscroll.pack(side=RIGHT, fill=Y)
xscroll.pack(side=BOTTOM, fill=X)
student_info.pack(fill=BOTH, expand=True)

student_info.heading("ID Number", text="ID Number")
student_info.heading("First Name", text="First Name")
student_info.heading("Last Name", text="Last Name")
student_info.heading("Sex", text="Sex")
student_info.heading("Program Code", text="Program Code")
student_info.heading("Year Level", text="Year Level")
student_info.heading("College Name", text="College Name")
student_info.heading("College Code", text="College Code")

student_info['show'] = 'headings'

load_from_csv()

root.mainloop()