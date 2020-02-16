import pandas as pd
import tkinter as tk
import datetime
from tkinter import messagebox
import random
from PIL import Image,ImageTk
test_data=[[52,26,13,18,30,12],[5,7,10,6,8,9],[4.5,3.8,5.0,4.9,4.0,4.7],
           ['Nanyang Technological University','National University of Singapore', 'Singapore Management University',
            'Singapore Institute of Management','Singapore University of Technology and Design','Lasalle College of Arts'],
           [2,3,4,1,2,3],[1,5,2,3,4,1]]
d1={'NRIC/Passport':[],'Age':[],'Weeks':[],'Work Hours':[],'GPA':[],'University':[],'Previous Job':[],
    'Skill Count':[],'Year Graduated':[],'Previous Company':[],'Years Worked':[]}
d2={'NRIC/Passport':[],'Age':[],'Weeks':[],'Work Hours':[],'GPA':[],'University':[],'Previous Job':[],
    'Skill Count':[],'Year Graduated':[],'Previous Company':[],'Years Worked':[]}
d3={'NRIC/Passport':[],'Age':[],'Weeks':[],'Work Hours':[],'GPA':[],'University':[],'Previous Job':[],
    'Skill Count':[],'Year Graduated':[],'Previous Company':[],'Years Worked':[]}
n=datetime.datetime.now()
root=tk.Tk()
java=tk.IntVar()
python=tk.IntVar()
r=tk.IntVar()
sql=tk.IntVar()
m1=tk.IntVar()
m2=tk.IntVar()
m3=tk.IntVar()
m4=tk.IntVar()
m5=tk.IntVar()
m6=tk.IntVar()
m7=tk.IntVar()
m8=tk.IntVar()
root.geometry('800x1200')
root.configure(bg='black')
t1="Amazoff App"
weekday=("Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday","Sunday")
s= t1+" "+str(n.replace(microsecond=0,second=0))+"  "+ str(weekday[n.weekday()])
root.title(s)
def company_info():
    for widget in root.winfo_children():
        widget.forget()
    img=ImageTk.PhotoImage(Image.open('back.jpg'))
    te="Our company was founded in 2006 by Mr. Alex Blackwell.\nIt started with 50 employees and two clients.\n Now it has 1000 employees and 100 clients.\nWe have been working tirelessly in recent times to promote gender equality.\nThat is our goal as well as vision!."
    l=tk.Label(root,text=te,fg="white",bg='black',font="Calibri 20")
    l.pack(anchor='n',fill=tk.X)
    image_label = tk.Label(root, image=img, bg="black")
    image_label.pack(anchor="n", fill="both", expand="yes")
    image_label.image =img
    back_button = tk.Button(root, text="Back", fg="black", font="Chalkboard 25", command=openingscreen)
    back_button.pack(side="bottom", fill=tk.X)
def work_info():
    for widget in root.winfo_children():
        widget.forget()
    l=tk.Label(root, text="Our Software Partner is 'In Toto'.\n It uses an algorithm that predicts the better profile for a job.\n It has been recently made to prevent bias against women in job recruitment.", fg="white",bg="black",font="Calibri 20")
    l.pack(anchor='n',fill=tk.X)
    img = ImageTk.PhotoImage(Image.open('in toto.png'))
    image_label = tk.Label(root, image=img, bg="black")
    image_label.pack(anchor="n", fill="both", expand="yes")
    image_label.image = img
    back_button = tk.Button(root, text="Back", fg="black", font="Chalkboard 25", command=openingscreen)
    back_button.pack(side="bottom", fill=tk.X)
def score(nric,age,weeks,whrs,gpa,uni,j,count,yrgrad, comp,wkyrs):
    for widget in root.winfo_children():
        widget.forget()
    img = ImageTk.PhotoImage(Image.open('q.png'))
    op_label=tk.Label(root, text="Your Information",bg="black",fg="red",font="Calibri 35")
    op_label.pack(anchor='n', fill=tk.X)
    nric_label=tk.Label(root, text=str("Identification Number: "+str(nric)), fg="white",bg="black",font="Calibri 20")
    nric_label.pack(anchor='nw')
    age_label=tk.Label(root, text=str("Age: "+str(age)), fg="white",bg="black",font="Calibri 20")
    age_label.pack(anchor='nw')
    weeks_label=tk.Label(root, text=str("Number of weeks committed: "+str(weeks)), fg="white",bg="black",font="Calibri 20")
    weeks_label.pack(anchor='nw')
    whrs_label=tk.Label(root, text=str("Working Hours Committed: "+str(whrs)),fg="white",bg="black",font="Calibri 20")
    whrs_label.pack(anchor='nw')
    j_label=tk.Label(root, text=str("Previous Job: "+str(j)),fg="white",bg="black",font="Calibri 20")
    j_label.pack(anchor='nw')
    comp_label=tk.Label(root,text=str("Name of Company: "+ str(comp)),fg="white",bg="black",font="Calibri 20")
    comp_label.pack(anchor='nw')
    wkyrs_label=tk.Label(root, text=str("Number of years worked: "+ str(wkyrs)),fg="white",bg="black",font="Calibri 20")
    wkyrs_label.pack(anchor='nw')
    uni_label=tk.Label(root, text=str("University Attended: "+str(uni)), fg="white",bg="black",font="Calibri 20")
    uni_label.pack(anchor='nw')
    yrgrad_label=tk.Label(root, text=str("Year of Graduation: "+str(yrgrad)),fg="white",bg="black",font="Calibri 20")
    yrgrad_label.pack(anchor='nw')
    gpa_label=tk.Label(root, text=str("GPA: "+str(gpa)),fg="white",bg="black",font="Calibri 20")
    gpa_label.pack(anchor='nw')
    image_label = tk.Label(root, image=img, bg="black")
    image_label.pack(anchor="n", fill="both", expand="yes")
    image_label.image = img
    back_button = tk.Button(root, text="Back", fg="black", font="Chalkboard 25", command=openingscreen)
    back_button.pack(side="bottom", fill=tk.X)
    ok_button = tk.Button(root, text="Check Score", fg='black', font="Chalkboard 25", command=lambda:report(weeks,whrs,gpa,uni,count,wkyrs))
    ok_button.pack(side="bottom", fill=tk.X)
def report(weeks,whrs,gpa,uni,count,wkyrs):
    sc=0;
    if(weeks>=test_data[0][random.randint(0,5)]):
        sc=sc+1
    if(whrs>=test_data[1][random.randint(0,5)]):
        sc=sc+1
    if(gpa>=test_data[2][random.randint(0,5)]):
        sc=sc+1
    u=random.randint(0,5)
    k=0
    for i in (test_data[3]):
        if(uni==i):
            p=k
        k=k+1
    if(p>=u):
        sc=sc+1
    if(count>=test_data[4][random.randint(0,5)]):
        sc=sc+1
    if(wkyrs>=test_data[5][random.randint(0,5)]):
        sc=sc+1
    ou="Your score is "+str(sc)+"/6\n 1:Poor\n2:Okay\n3:Average\n4:Good\n5:Very Good\n6:Excellent"
    messagebox.showinfo("Score Report",ou)
def j1_input():
    for widget in root.winfo_children():
        widget.forget()
    def store_input():
        for widget in root.winfo_children():
            widget.forget()
        l = tk.Label(root, text=(l1_entry.get()))
        l.pack()
        nric=str(l1_entry.get())
        age=int(l2_entry.get())
        weeks=int(l3_entry.get())
        whrs=int(l4_entry.get())
        gpa=float(l5_entry.get())
        uni=str(l6_entry.get())
        j=str(l7_entry.get())
        yrgrad=int(l8_entry.get())
        comp=str(l9_entry.get())
        wkyrs=int(l10_entry.get())
        cb=[java.get(),python.get(),r.get(),sql.get()]
        count=0
        for i in cb:
            if(i==1):
                count=count+1
        d1['NRIC/Passport'].append(nric)
        d1['Age'].append(age)
        d1['Weeks'].append(weeks)
        d1['Work Hours'].append(whrs)
        d1['GPA'].append(gpa)
        d1['University'].append(uni)
        d1['Previous Company'].append(comp)
        d1['Year Graduated'].append(yrgrad)
        d1['Years Worked'].append(wkyrs)
        d1['Previous Job'].append(j)
        d1['Skill Count'].append(count)
        df1=pd.DataFrame(d1)
        data=pd.read_excel('Job1.xlsx')
        d=pd.DataFrame(data)
        w1 = pd.ExcelWriter('Job1.xlsx')
        data.to_excel(w1,'Sheet1', startrow=len(d) + 1, startcol=1, index=False)
        df1.to_excel(w1 ,'Sheet1',index=False)
        w1.save()
        score(nric,age,weeks,whrs,gpa,uni,j,count,yrgrad,comp,wkyrs)
    e1=tk.Label(root, text="Personal Details",fg="red",bg="black",font="Calibri 15")
    e1.pack(anchor='nw')
    l1=tk.Label(root, text="Enter your NRIC/Passport Number:",font='Calibri 12',fg="red",bg="black")
    l1.pack(anchor='nw')
    l1_entry=tk.Entry(root)
    l1_entry.pack(anchor='nw')
    l2 = tk.Label(root, text="Enter your age:", font="Calibri 12", fg="red", bg="black")
    l2.pack(anchor='nw')
    l2_entry = tk.Entry(root)
    l2_entry.pack(anchor='nw')
    e2 = tk.Label(root, text="Job Details", fg="red", bg="black", font="Calibri 15")
    e2.pack(anchor='nw')
    l3 = tk.Label(root, text="Enter the period of commitment (in weeks):", fg="red", bg="black", font="Calibri 12")
    l3.pack(anchor='nw')
    l3_entry = tk.Entry(root)
    l3_entry.pack(anchor='nw')
    l4 = tk.Label(root, text="Enter number of preferred working hours:", fg="red", bg="black", font="Calibri 12")
    l4.pack(anchor='nw')
    l4_entry = tk.Entry(root)
    l4_entry.pack(anchor='nw')
    e3 = tk.Label(root, text="Educational History", fg="red", bg="black", font="Calibri 15")
    e3.pack(anchor='nw')
    l6 = tk.Label(root, text="Enter your university:", fg="red", bg="black", font="Calibri 12")
    l6.pack(anchor='nw')
    l6_entry = tk.Entry(root)
    l6_entry.pack(anchor='nw')
    l8=tk.Label(root,text="Year of Graduation:", fg="red", bg="black", font ="Calibri 12")
    l8.pack(anchor='nw')
    l8_entry=tk.Entry(root)
    l8_entry.pack(anchor='nw')
    l5 = tk.Label(root, text="Enter your GPA according to the latest results:", font="Calibri 12", fg="red", bg="black")
    l5.pack(anchor='nw')
    l5_entry = tk.Entry(root)
    l5_entry.pack(anchor='nw')
    e4 = tk.Label(root, text="Employment History", fg="red", bg="black", font="Calibri 15")
    e4.pack(anchor='nw')
    l7 = tk.Label(root, text="Previous Job:", fg="red", bg="black", font="Calibri 12")
    l7.pack(anchor='nw')
    l7_entry = tk.Entry(root)
    l7_entry.pack(anchor='nw')
    l9=tk.Label(root, text="Name of Company:",fg="red", bg="black", font="Calibri 12")
    l9.pack(anchor='nw')
    l9_entry=tk.Entry(root)
    l9_entry.pack(anchor='nw')
    l10=tk.Label(root, text="Number of years spent working:", fg="red", bg="black", font="Calibri 14")
    l10.pack(anchor='nw')
    l10_entry=tk.Entry(root)
    l10_entry.pack(anchor='nw')
    e5 = tk.Label(root, text="Choose one or more skills:", fg="red", bg="black", font="Calibri 14")
    e5.pack(anchor='nw')
    c1 = tk.Checkbutton(root, text="Java", fg='red', bg='black', font="Calibri 10", variable=java)
    c1.pack(anchor="nw")
    c2 = tk.Checkbutton(root, text="Python", fg='red', bg='black', font="Calibri 10", variable=python)
    c2.pack(anchor='nw')
    c3 = tk.Checkbutton(root, text="R coding", fg="red", bg="black", font="Calibri 10", variable=r)
    c3.pack(anchor='nw')
    c4 = tk.Checkbutton(root, text="SQL", fg="red", bg="black", font="Calibri 10", variable=sql)
    c4.pack(anchor='nw')
    back_button = tk.Button(root, text="Back", fg="black", font="Chalkboard 15", command=openingscreen)
    back_button.pack(side="bottom", fill=tk.X)
    ok_button = tk.Button(root, text="Submit", fg='black', font="Chalkboard 15", command=store_input)
    ok_button.pack(side="bottom", fill=tk.X)
def j2_input():
    for widget in root.winfo_children():
        widget.forget()
    def store_input():
        for widget in root.winfo_children():
            widget.forget()
        l = tk.Label(root, text=(l1_entry.get()))
        l.pack()
        nric=str(l1_entry.get())
        age=int(l2_entry.get())
        weeks=int(l3_entry.get())
        whrs=int(l4_entry.get())
        gpa=float(l5_entry.get())
        uni=str(l6_entry.get())
        j=str(l7_entry.get())
        yrgrad=int(l8_entry.get())
        comp=str(l9_entry.get())
        wkyrs=int(l10_entry.get())
        cb=[m1.get(),m2.get(),m3.get(),m4.get()]
        count=0
        for i in cb:
            if(i==1):
                count=count+1
        d2['NRIC/Passport'].append(nric)
        d2['Age'].append(age)
        d2['Weeks'].append(weeks)
        d2['Work Hours'].append(whrs)
        d2['GPA'].append(gpa)
        d2['University'].append(uni)
        d2['Previous Company'].append(comp)
        d2['Year Graduated'].append(yrgrad)
        d2['Years Worked'].append(wkyrs)
        d2['Previous Job'].append(j)
        d2['Skill Count'].append(count)
        df2=pd.DataFrame(d2)
        data = pd.read_excel('Job2.xlsx')
        d = pd.DataFrame(data)
        w2 = pd.ExcelWriter('Job2.xlsx')
        data.to_excel(w2, 'Sheet1', startrow=len(d) + 1, startcol=1, index=False)
        df2.to_excel(w2, 'Sheet1', index=False)
        w2.save()
        score(nric,age,weeks,whrs,gpa,uni,j,count,yrgrad,comp,wkyrs)
    e1=tk.Label(root, text="Personal Details",fg="red",bg="black",font="Calibri 15")
    e1.pack(anchor='nw')
    l1=tk.Label(root, text="Enter your NRIC/Passport Number:",font='Calibri 12',fg="red",bg="black")
    l1.pack(anchor='nw')
    l1_entry=tk.Entry(root)
    l1_entry.pack(anchor='nw')
    l2 = tk.Label(root, text="Enter your age:", font="Calibri 12", fg="red", bg="black")
    l2.pack(anchor='nw')
    l2_entry = tk.Entry(root)
    l2_entry.pack(anchor='nw')
    e2 = tk.Label(root, text="Job Details", fg="red", bg="black", font="Calibri 15")
    e2.pack(anchor='nw')
    l3 = tk.Label(root, text="Enter the period of commitment (in weeks):", fg="red", bg="black", font="Calibri 12")
    l3.pack(anchor='nw')
    l3_entry = tk.Entry(root)
    l3_entry.pack(anchor='nw')
    l4 = tk.Label(root, text="Enter number of preferred working hours:", fg="red", bg="black", font="Calibri 12")
    l4.pack(anchor='nw')
    l4_entry = tk.Entry(root)
    l4_entry.pack(anchor='nw')
    e3 = tk.Label(root, text="Educational History", fg="red", bg="black", font="Calibri 15")
    e3.pack(anchor='nw')
    l6 = tk.Label(root, text="Enter your university:", fg="red", bg="black", font="Calibri 12")
    l6.pack(anchor='nw')
    l6_entry = tk.Entry(root)
    l6_entry.pack(anchor='nw')
    l8=tk.Label(root,text="Year of Graduation:", fg="red", bg="black", font ="Calibri 12")
    l8.pack(anchor='nw')
    l8_entry=tk.Entry(root)
    l8_entry.pack(anchor='nw')
    l5 = tk.Label(root, text="Enter your GPA according to the latest results:", font="Calibri 12", fg="red", bg="black")
    l5.pack(anchor='nw')
    l5_entry = tk.Entry(root)
    l5_entry.pack(anchor='nw')
    e4 = tk.Label(root, text="Employment History", fg="red", bg="black", font="Calibri 12")
    e4.pack(anchor='nw')
    l7 = tk.Label(root, text="Previous Job:", fg="red", bg="black", font="Calibri 12")
    l7.pack(anchor='nw')
    l7_entry = tk.Entry(root)
    l7_entry.pack(anchor='nw')
    l9=tk.Label(root, text="Name of Company:",fg="red", bg="black", font="Calibri 12")
    l9.pack(anchor='nw')
    l9_entry=tk.Entry(root)
    l9_entry.pack(anchor='nw')
    l10=tk.Label(root, text="Number of years spent working:", fg="red", bg="black", font="Calibri 14")
    l10.pack(anchor='nw')
    l10_entry=tk.Entry(root)
    l10_entry.pack(anchor='nw')
    e5 = tk.Label(root, text="Choose one or more skills:", fg="red", bg="black", font="Calibri 14")
    e5.pack(anchor='nw')
    c1 = tk.Checkbutton(root, text="Operating Systems(Windows & MacOS)", fg='red', bg='black', font="Calibri 10", variable=m1)
    c1.pack(anchor="nw")
    c2 = tk.Checkbutton(root, text="Office Suites(Microsoft Office, G Suite)", fg='red', bg='black', font="Calibri 10", variable=m2)
    c2.pack(anchor='nw')
    c3 = tk.Checkbutton(root, text="Presentation Software(Powerpoint, Keynote)", fg="red", bg="black", font="Calibri 10", variable=m3)
    c3.pack(anchor='nw')
    c4 = tk.Checkbutton(root, text="Communication and Collaboration Tools(Slack,Skype etc.)", fg="red", bg="black", font="Calibri 10", variable=m4)
    c4.pack(anchor='nw')
    back_button = tk.Button(root, text="Back", fg="black", font="Chalkboard 15", command=openingscreen)
    back_button.pack(side="bottom", fill=tk.X)
    ok_button = tk.Button(root, text="Submit", fg='black', font="Chalkboard 15", command=store_input)
    ok_button.pack(side="bottom", fill=tk.X)
def j3_input():
    for widget in root.winfo_children():
        widget.forget()
    def store_input():
        for widget in root.winfo_children():
            widget.forget()
        l = tk.Label(root, text=(l1_entry.get()))
        l.pack()
        nric=str(l1_entry.get())
        age=int(l2_entry.get())
        weeks=int(l3_entry.get())
        whrs=int(l4_entry.get())
        gpa=float(l5_entry.get())
        uni=str(l6_entry.get())
        j=str(l7_entry.get())
        yrgrad=int(l8_entry.get())
        comp=str(l9_entry.get())
        wkyrs=int(l10_entry.get())
        cb=[m5.get(),m6.get(),m7.get(),m8.get()]
        count=0
        for i in cb:
            if((i==1)):
                count=count+1
        d3['NRIC/Passport'].append(nric)
        d3['Age'].append(age)
        d3['Weeks'].append(weeks)
        d3['Work Hours'].append(whrs)
        d3['GPA'].append(gpa)
        d3['University'].append(uni)
        d3['Previous Company'].append(comp)
        d3['Year Graduated'].append(yrgrad)
        d3['Years Worked'].append(wkyrs)
        d3['Previous Job'].append(j)
        d3['Skill Count'].append(count)
        df3 = pd.DataFrame(d3)
        data = pd.read_excel('Job3.xlsx')
        d = pd.DataFrame(data)
        w3 = pd.ExcelWriter('Job3.xlsx')
        data.to_excel(w3, 'Sheet1', startrow=len(d) + 1, startcol=1, index=False)
        df3.to_excel(w3, 'Sheet1', index=False)
        w3.save()
        score(nric,age,weeks,whrs,gpa,uni,j,count,yrgrad,comp,wkyrs)
    e1=tk.Label(root, text="Personal Details",fg="red",bg="black",font="Calibri 15")
    e1.pack(anchor='nw')
    l1=tk.Label(root, text="Enter your NRIC/Passport Number:",font='Calibri 12',fg="red",bg="black")
    l1.pack(anchor='nw')
    l1_entry=tk.Entry(root)
    l1_entry.pack(anchor='nw')
    l2 = tk.Label(root, text="Enter your age:", font="Calibri 12", fg="red", bg="black")
    l2.pack(anchor='nw')
    l2_entry = tk.Entry(root)
    l2_entry.pack(anchor='nw')
    e2 = tk.Label(root, text="Job Details", fg="red", bg="black", font="Calibri 15")
    e2.pack(anchor='nw')
    l3 = tk.Label(root, text="Enter the period of commitment (in weeks):", fg="red", bg="black", font="Calibri 12")
    l3.pack(anchor='nw')
    l3_entry = tk.Entry(root)
    l3_entry.pack(anchor='nw')
    l4 = tk.Label(root, text="Enter number of preferred working hours:", fg="red", bg="black", font="Calibri 12")
    l4.pack(anchor='nw')
    l4_entry = tk.Entry(root)
    l4_entry.pack(anchor='nw')
    e3 = tk.Label(root, text="Educational History", fg="red", bg="black", font="Calibri 15")
    e3.pack(anchor='nw')
    l6 = tk.Label(root, text="Enter your university:", fg="red", bg="black", font="Calibri 12")
    l6.pack(anchor='nw')
    l6_entry = tk.Entry(root)
    l6_entry.pack(anchor='nw')
    l8=tk.Label(root,text="Year of Graduation:", fg="red", bg="black", font ="Calibri 12")
    l8.pack(anchor='nw')
    l8_entry=tk.Entry(root)
    l8_entry.pack(anchor='nw')
    l5 = tk.Label(root, text="Enter your GPA according to the latest results:", font="Calibri 12", fg="red", bg="black")
    l5.pack(anchor='nw')
    l5_entry = tk.Entry(root)
    l5_entry.pack(anchor='nw')
    e4 = tk.Label(root, text="Employment History", fg="red", bg="black", font="Calibri 12")
    e4.pack(anchor='nw')
    l7 = tk.Label(root, text="Previous Job:", fg="red", bg="black", font="Calibri 12")
    l7.pack(anchor='nw')
    l7_entry = tk.Entry(root)
    l7_entry.pack(anchor='nw')
    l9=tk.Label(root, text="Name of Company:",fg="red", bg="black", font="Calibri 12")
    l9.pack(anchor='nw')
    l9_entry=tk.Entry(root)
    l9_entry.pack(anchor='nw')
    l10=tk.Label(root, text="Number of years spent working:", fg="red", bg="black", font="Calibri 14")
    l10.pack(anchor='nw')
    l10_entry=tk.Entry(root)
    l10_entry.pack(anchor='nw')
    e5 = tk.Label(root, text="Choose one or more skills:", fg="red", bg="black", font="Calibri 14")
    e5.pack(anchor='nw')
    c1 = tk.Checkbutton(root, text="Microsoft Office Suite", fg='red', bg='black', font="Calibri 10", variable=m5)
    c1.pack(anchor="nw")
    c2 = tk.Checkbutton(root, text="Proficiency in Public Speaking", fg='red', bg='black', font="Calibri 10", variable=m6)
    c2.pack(anchor='nw')
    c3 = tk.Checkbutton(root, text="R studio", fg="red", bg="black", font="Calibri 10", variable=m7)
    c3.pack(anchor='nw')
    c4 = tk.Checkbutton(root, text="Tools such as GoToMeeting and DocuSign.", fg="red", bg="black", font="Calibri 10", variable=m8)
    c4.pack(anchor='nw')
    back_button = tk.Button(root, text="Back", fg="black", font="Chalkboard 15", command=openingscreen)
    back_button.pack(side="bottom", fill=tk.X)
    ok_button = tk.Button(root, text="Submit", fg='black', font="Chalkboard 15", command=store_input)
    ok_button.pack(side="bottom", fill=tk.X)
def job1():
    for widget in root.winfo_children():
        widget.forget()
    img = ImageTk.PhotoImage(Image.open('q.png'))
    l1=tk.Label(root, text="Job Description", fg="red",bg="black", font="Calibri 22")
    l1.pack(anchor='nw')
    info1="1.Require prior experience in coding in R, Python, Java, SQL, Excel."
    info2="2.Basic knowledge of data structures and algorithms."
    info3="3.Able to thrive in a startup environment."
    info4="4.Motivated and fast learner."
    info5 = "1.Data Crunching and data massage."
    info6 = "2.Implementation/tuning of machine learning algorithms."
    info7 = "3.Data science/machine learning experiments."
    info8 = "4.Expected Stress-level: Medium."
    info9 = "5.Expected working hours at home: 4 hours."
    info10 ="6.Daily commitment at at office: 5 hours."
    info5_label = tk.Label(root, text=info5, fg="white", font="Calibri 15", bg="black")
    info5_label.pack(anchor='nw')
    info6_label = tk.Label(root, text=info6, fg="white", font="Calibri 15", bg="black")
    info6_label.pack(anchor='nw')
    info7_label = tk.Label(root, text=info7, fg="white", font="Calibri 15", bg="black")
    info7_label.pack(anchor='nw')
    info8_label = tk.Label(root, text=info8, fg="white", font="Calibri 15", bg="black")
    info8_label.pack(anchor='nw')
    info9_label = tk.Label(root, text=info9, fg="white", font="Calibri 15", bg="black")
    info9_label.pack(anchor='nw')
    info10_label = tk.Label(root, text=info10, fg="white", font="Calibri 15", bg="black")
    info10_label.pack(anchor='nw')
    l2 = tk.Label(root, text="\nJob Requirements", font="Calibri 22", fg="red", bg="black")
    l2.pack(anchor='nw')
    info1_label = tk.Label(root, text=info1, fg="white", font="Calibri 15", bg="black")
    info1_label.pack(anchor='nw')
    info2_label = tk.Label(root, text=info2, fg="white", font="Calibri 15", bg="black")
    info2_label.pack(anchor='nw')
    info3_label = tk.Label(root, text=info3, fg="white", font="Calibri 15", bg="black")
    info3_label.pack(anchor='nw')
    info4_label = tk.Label(root, text=info4, fg="white", font="Calibri 15", bg="black")
    info4_label.pack(anchor='nw')
    image_label = tk.Label(root, image=img, bg="black")
    image_label.pack(anchor="n", fill="both", expand="yes")
    image_label.image = img
    back_button = tk.Button(root, text="Back", fg="black", font="Chalkboard 25", command=openingscreen)
    back_button.pack(side="bottom", fill=tk.X)
    apply_button = tk.Button(root, text="Apply Now", fg='black', bg='black',font="Chalkboard 25", command=j1_input)
    apply_button.pack(side="bottom", fill=tk.X)
def job2():
    for widget in root.winfo_children():
        widget.forget()
    img = ImageTk.PhotoImage(Image.open('q.png'))
    l1 = tk.Label(root, text="Job Description", fg="red", bg="black", font="Calibri 22")
    l1.pack(anchor='nw')
    info1 = "1.High level of inter-personal skills."
    info2 = "2.Ability to multi-task and conduct themselves in a variety of situations."
    info3 = "3.Should be able to take calls post-office hours up until 9pm."
    info4 = "4.Expected to have excellent verbal and written communication and presentation skills."
    info5 = "1.Expected Stress-level: High."
    info6 = "2.Able to make strong networks and connections within the work environment."
    info7 = "3.Expected daily commitment at office: 8 hours."
    info8 = "4.This position will require you to travel once in every 2 months on an average."
    info9 = "5.Expected working hours at home: 2 hours."
    info10 ="6.Generating business insights or product ideas from qualitative and quantitative analysis."
    info5_label = tk.Label(root, text=info5, fg="white", font="Calibri 15", bg="black")
    info5_label.pack(anchor='nw')
    info6_label = tk.Label(root, text=info6, fg="white", font="Calibri 15", bg="black")
    info6_label.pack(anchor='nw')
    info7_label = tk.Label(root, text=info7, fg="white", font="Calibri 15", bg="black")
    info7_label.pack(anchor='nw')
    info8_label = tk.Label(root, text=info8, fg="white", font="Calibri 15", bg="black")
    info8_label.pack(anchor='nw')
    info9_label = tk.Label(root, text=info9, fg="white", font="Calibri 15", bg="black")
    info9_label.pack(anchor='nw')
    info10_label = tk.Label(root, text=info10, fg="white", font="Calibri 15", bg="black")
    info10_label.pack(anchor='nw')
    l2 = tk.Label(root, text="\nJob Requirements", font="Calibri 22", fg="red", bg="black")
    l2.pack(anchor='nw')
    info1_label = tk.Label(root, text=info1, fg="white", font="Calibri 15", bg="black")
    info1_label.pack(anchor='nw')
    info2_label = tk.Label(root, text=info2, fg="white", font="Calibri 15", bg="black")
    info2_label.pack(anchor='nw')
    info3_label = tk.Label(root, text=info3, fg="white", font="Calibri 15", bg="black")
    info3_label.pack(anchor='nw')
    info4_label = tk.Label(root, text=info4, fg="white", font="Calibri 15", bg="black")
    info4_label.pack(anchor='nw')
    image_label = tk.Label(root, image=img, bg="black")
    image_label.pack(anchor="n", fill="both", expand="yes")
    image_label.image = img
    back_button = tk.Button(root, text="Back", fg="black", font="Chalkboard 25", command=openingscreen)
    back_button.pack(side="bottom", fill=tk.X)
    apply_button = tk.Button(root, text="Apply Now", fg='black', bg='black', font="Chalkboard 25", command=j2_input)
    apply_button.pack(side="bottom", fill=tk.X)
def job3():
    for widget in root.winfo_children():
        widget.forget()
    img = ImageTk.PhotoImage(Image.open('q.png'))
    l1 = tk.Label(root, text="Job Description", fg="red", bg="black", font="Calibri 22")
    l1.pack(anchor='nw')
    info1 = "1.Ability to work in a fast-paced environment."
    info2 = "2.Good problem-solving skills with action mindset."
    info3 = "3.Critical and evaluative thinking."
    info4 = "4.Proficiency in Microsoft Excel."
    info5 = "1.Expected Stress-level: Medium."
    info6 = "2.Expected to work on weekends when closer to deadlines."
    info7 = "3.Expected daily commitment at office: 7 hours."
    info8 = "4.Looking for team player with good people management skills."
    info9 = "5.Usually not expected to work post office hours."
    info10 ="6.Independent work with high degree of initiative."
    info5_label = tk.Label(root, text=info5, fg="white", font="Calibri 15", bg="black")
    info5_label.pack(anchor='nw')
    info6_label = tk.Label(root, text=info6, fg="white", font="Calibri 15", bg="black")
    info6_label.pack(anchor='nw')
    info7_label = tk.Label(root, text=info7, fg="white", font="Calibri 15", bg="black")
    info7_label.pack(anchor='nw')
    info8_label = tk.Label(root, text=info8, fg="white", font="Calibri 15", bg="black")
    info8_label.pack(anchor='nw')
    info9_label = tk.Label(root, text=info9, fg="white", font="Calibri 15", bg="black")
    info9_label.pack(anchor='nw')
    info10_label = tk.Label(root, text=info10, fg="white", font="Calibri 15", bg="black")
    info10_label.pack(anchor='nw')
    l2 = tk.Label(root, text="\nJob Requirements", font="Calibri 22", fg="red", bg="black")
    l2.pack(anchor='nw')
    info1_label = tk.Label(root, text=info1, fg="white", font="Calibri 15", bg="black")
    info1_label.pack(anchor='nw')
    info2_label = tk.Label(root, text=info2, fg="white", font="Calibri 15", bg="black")
    info2_label.pack(anchor='nw')
    info3_label = tk.Label(root, text=info3, fg="white", font="Calibri 15", bg="black")
    info3_label.pack(anchor='nw')
    info4_label = tk.Label(root, text=info4, fg="white", font="Calibri 15", bg="black")
    info4_label.pack(anchor='nw')
    image_label = tk.Label(root, image=img, bg="black")
    image_label.pack(anchor="n", fill="both", expand="yes")
    image_label.image = img
    back_button = tk.Button(root, text="Back", fg="black", font="Chalkboard 25", command=openingscreen)
    back_button.pack(side="bottom", fill=tk.X)
    apply_button = tk.Button(root, text="Apply Now", fg='black', bg='black', font="Chalkboard 25", command=j3_input)
    apply_button.pack(side="bottom", fill=tk.X)
def jobs_avail():
    for widget in root.winfo_children():
        widget.forget()
    img=ImageTk.PhotoImage(Image.open('q.png'))
    pos_avail=tk.Label(root, text="Positions Available", font="Calibri 45", fg="red", bg="black")
    pos_avail.pack(anchor='n', fill=tk.X)
    pos1=tk.Button(root,text="1.Data Scientist",fg="black",font="Chalkboard 25",command=job1)
    pos1.pack(anchor='n',fill=tk.X)
    pos2=tk.Button(root, text="2.Marketing and Communications Intern",font="Chalkboard 25",command=job2)
    pos2.pack(anchor='n',fill=tk.X)
    pos3=tk.Button(root,text="3.Business Development Manager",font="Chalkboard 25", command=job3)
    pos3.pack(anchor='n',fill=tk.X)
    image_label = tk.Label(root, image=img, bg="black")
    image_label.pack(anchor="n", fill="both", expand="yes")
    image_label.image = img
    back_button = tk.Button(root, text="Back", fg="red", font="Chalkboard 25",command=openingscreen)
    back_button.pack(side="bottom",fill=tk.X)
def openingscreen():
    for widget in root.winfo_children():
        widget.forget()
    img=ImageTk.PhotoImage(Image.open("back.jpg"))
    open_message=""
    open_message_label = tk.Label(root, font='Calibri 45', fg="red", bg="black", text=open_message)
    open_message_label.pack(anchor="n", fill=tk.X)
    option1_button=tk.Button(root, text="ABOUT US",font="Chalkboard 25",fg="black", background="blue",command=company_info)
    option1_button.pack(anchor='n',fill=tk.X)
    option2_button=tk.Button(root, text="OUR PARTNERS", font="Chalkboard 25", fg="black", background='blue', command=work_info)
    option2_button.pack(anchor='n',fill=tk.X)
    option3_button=tk.Button(root, text="JOIN US", font="Chalkboard 25", fg="black", background="blue", command=jobs_avail)
    option3_button.pack(anchor='n', fill=tk.X)
    image_label=tk.Label(root, image=img,bg="black")
    image_label.pack(anchor="n",fill="both",expand="yes")
    image_label.image = img
    option3_button = tk.Button(root, text="Exit", font="Chalkboard 25", fg="black", command=exit)
    option3_button.pack(side="bottom", fill=tk.X)
openingscreen()
root.mainloop()