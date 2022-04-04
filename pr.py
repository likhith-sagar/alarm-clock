print("Please wait while we import things for you...")
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from pygame import mixer

home=Tk()
icon=PhotoImage(file="icon.png")
home.iconphoto(True,icon)
home.configure(background='#efefef')
home.title("Alarm Clock")
home.minsize(680,460)
home.maxsize(680,460)
home.geometry("680x460")

mixer.init()
mixer.music.load("alarm_1.mp3")

var_hr=StringVar()
var_min=StringVar()
active_alarm=[]


class alarm_time:
	def __init__(self,hr,mins):
		self.hr=hr
		self.mins=mins
		self.btn=Button(side_frame,text="Alarm set on: "+str(hr)+":"+str(mins),font="comicsansms 12",bg="#dedede",command=lambda : self.remove_alarm("btn"))
		self.btn.pack(padx=4,pady=2,fill=X)
	def remove_alarm(self,source="fun"):
		if source=="btn":
			result=messagebox.askyesno("Remove","Are you sure you want to remove alarm at "+str(self.hr)+":"+str(self.mins)+"?",icon="warning")

		else:
			result=True
		if result:
			global active_alarm
			active_alarm.remove(self)
			self.btn.destroy()


def validate(hr,mins):
	if hr>24 or hr<0:
		return False
	if mins>59 or mins<0:
		return False
	if hr==mins==0:
		return False
	if active_alarm:
		for i in active_alarm:
			if i.hr==hr and i.mins==mins:
				
				return False
	return True

def add_alarm():
	try:
		global var_hr
		global var_min
		if validate(int(var_hr.get()),int(var_min.get())):

			global active_alarm
			active_alarm.append(alarm_time(int(var_hr.get()),int(var_min.get())))
			
		else:
			messagebox.showwarning("Error","Invalid Time! or Alarm already exists!")
	except :
			messagebox.showerror("Error","Invalid Time!")

def take_action():
	mixer.music.play(-1)
	res=messagebox.showinfo("Alarm","Its time to Get Things Done!!!\nTurn off the Alarm")
	if res:
		mixer.music.stop()
		mixer.music.load("alarm_1.mp3")
	

def set_date():
	temp=datetime.now().date()
	date_disp["text"]="Date:\n"+str(temp)
	return


def run_time():
	temp=datetime.now().time()
	time_disp["text"]="Time:\n"+str(temp)[:8]
	check=check_alarm(int(str(temp)[:2]),int(str(temp)[3:5]))
	if check:
		
		take_action()
		check.remove_alarm()
		
		
	home.after(1,run_time)



def check_alarm(hr,mins):
	for i in active_alarm:
		if i.hr==hr and i.mins==mins:
			
			return i
		
	return False


side_frame=Frame(home,bg="#bbcccc",width=200,borderwidth=2,relief=RIDGE)
side_frame.pack(fill=Y,side=RIGHT)
top_frame=Frame(home,height=100,borderwidth=2,relief=RIDGE)
top_frame.pack(fill=X,side=TOP)
input_frame=Frame(home,bg="#dddddd",height=240,width=200,borderwidth=2,relief=GROOVE)
input_frame.pack(pady=20)

Tk.update(home)
t1_frame=Frame(top_frame,padx=8,pady=4,height=96,width=((top_frame.winfo_width())-4)/2)
t2_frame=Frame(top_frame,padx=8,pady=4,height=96,width=((top_frame.winfo_width())-4)/2)
t1_frame.pack(fill=Y,side=LEFT)
t2_frame.pack(fill=Y,side=RIGHT)

#input widgets
Label(input_frame,text="SET ALARM",font="comicsansms 16 bold",bg="#222222",fg="white",borderwidth=2,relief=RIDGE).pack(side=TOP,fill=X,pady=10,padx=6)

f1=Frame(input_frame,bg="#dddddd",height=50)
f1.pack(fill=X,side=TOP,padx=10,pady=6)
f2=Frame(input_frame,bg="#dddddd",height=50)
f2.pack(fill=X,side=TOP,padx=10,pady=6)
f3=Frame(input_frame,bg="#dddddd",height=50)
f3.pack(fill=X,side=TOP,padx=10,pady=10)


hr_label=Label(f1,text="Hour:",font="helvetica 14 ",bg="#dddddd")
hr_label.pack(pady=2,side=LEFT,padx=4)

hr_inp=Entry(f1,textvariable=var_hr,font="helvetica 14 ")
hr_inp.pack(pady=2,side=RIGHT,padx=2)

min_label=Label(f2,text="Mins:",font="helvetica 14 ",bg="#dddddd")
min_label.pack(pady=2,side=LEFT,padx=4)

min_inp=Entry(f2,textvariable=var_min,font="helvetica 14 ")
min_inp.pack(pady=2,side=RIGHT,padx=2)


date_disp=Label(t1_frame,text="DATE HERE",font="comicsansms 20 ")
date_disp.pack(padx=10,pady=20)

time_disp=Label(t2_frame,text="TIME HERE",font="comicsansms 20 ")
time_disp.pack(padx=10,pady=20)

Label(side_frame,text="List of active alarms",font="comicsansms 12 bold",bg="#222222",fg="white").pack(padx=4,pady=10,side=TOP)

Label(side_frame,text="Click on Alarms to Delete",font="comicsansms 10 bold ",bg="#bbcccc",fg="black").pack(padx=4,pady=5,side=BOTTOM)

submit=Button(f3,text="Add Alarm",command=add_alarm,font="comicsansms 12 bold",bg="#4466A1",fg="white")
submit.pack()

def on_closing():
	if messagebox.askokcancel("Quit","Do you want to quit?"):
		home.destroy()


home.protocol("WM_DELETE_WINDOW", on_closing)


set_date()
run_time()





home.mainloop()
