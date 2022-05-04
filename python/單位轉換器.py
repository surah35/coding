from cProfile import label
from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from typing_extensions import Self
from unicodedata import numeric

#creat window
win = Tk()
win.title("單位轉換器")
win.geometry("350x100")
win.resizable(False,False)

#function
def running():
    try:
         int(entry_1.get())
    except:
        messagebox.showwarning("警告","請輸入數字") 

    if cbb_1.get()=="秒鐘"and cbb_2.get()=="分鐘":
        label_3['text'] =int(entry_1.get())/60 
    elif cbb_1.get()=="分鐘"and cbb_2.get()=="秒鐘":
        label_3['text'] =int(entry_1.get())*60
    elif cbb_1.get()=="秒鐘"and cbb_2.get()=="小時":
        label_3['text'] =int(entry_1.get())/3600 
    elif cbb_1.get()=="小時"and cbb_2.get()=="秒鐘":
        label_3['text'] =int(entry_1.get())*3600
    elif cbb_1.get()=="分鐘"and cbb_2.get()=="小時":
        label_3['text'] =int(entry_1.get())/60 
    elif cbb_1.get()=="小時"and cbb_2.get()=="分鐘":
        label_3['text'] =int(entry_1.get())*60  
    else:
        label_3['text'] =int(entry_1.get())

    if cbb_3.get()=="公分"and cbb_4.get()=="公尺":
        label_4['text'] =int(entry_2.get())/100 
    elif cbb_3.get()=="公尺"and cbb_4.get()=="公分":
        label_4['text'] =int(entry_2.get())*100
    elif cbb_3.get()=="公分"and cbb_4.get()=="公里":
        label_4['text'] =int(entry_2.get())/100/1000 
    elif cbb_3.get()=="公里"and cbb_4.get()=="公分":
        label_4['text'] =int(entry_2.get())*100*1000
    elif cbb_3.get()=="公尺"and cbb_4.get()=="公里":
        label_4['text'] =int(entry_2.get())/1000 
    elif cbb_3.get()=="公里"and cbb_4.get()=="公尺":
        label_4['text'] =int(entry_2.get())*1000 
    else:
        label_4['text'] =int(entry_2.get())
# class
class frame_1:
    def __init__(self,*args):
        self.frame_1 = Frame(win)
        self.frame_1.grid()

    def change(self):
        self.frame_1.grid_forget()
        face2.frame_2.grid()

class frame_2:
    def __init__(self,*args):
        self.frame_2 = Frame(win)
        self.frame_2.grid()

    def change(self):
        self.frame_2.grid_forget()
        face1.frame_1.grid()
        

#object
face1 = frame_1()
face2 = frame_2()
#時間---
course = ["秒鐘","分鐘","小時"]
label_1 = Label(face1.frame_1,text="轉換前：")
label_1.config(font=20)
label_1.grid(row=0,column=0)

entry_1 = Entry(face1.frame_1,font=20,justify="center")
entry_1 .grid(row=0,column=1)

label_2 = Label(face1.frame_1,text="轉換後：")
label_2.config(font=20)
label_2.grid(row=1,column=0)

label_3 = Label(face1.frame_1,font=20,bg="white",width=17)
label_3.grid(row=1,column=1)



#cbb 表示下拉式選單
cbb_1 = ttk.Combobox(face1.frame_1,value=course,width=5)
cbb_1.current(0)

cbb_1.grid(row=0,column=2)

cbb_2 = ttk.Combobox(face1.frame_1,value=course,width=5)
cbb_2.current(1)
cbb_2.grid(row=1,column=2)

button_run = Button(face1.frame_1,text="轉換",width=15,command=running).grid(row=2,column=1)

#長度---
face2.frame_2.grid_forget()
course = ["公分","公尺","公里"]
label_1 = Label(face2.frame_2,text="轉換前：")
label_1.config(font=20)
label_1.grid(row=0,column=0)

entry_2 = Entry(face2.frame_2,font=20,justify="center")
entry_2 .grid(row=0,column=1)

label_2 = Label(face2.frame_2,text="轉換後：")
label_2.config(font=20)
label_2.grid(row=1,column=0)

label_4 = Label(face2.frame_2,font=20,bg="white",width=17)
label_4.grid(row=1,column=1)

#cbb 表示下拉式選單
cbb_3 = ttk.Combobox(face2.frame_2,value=course,width=5)
cbb_3.current(0)
cbb_3.grid(row=0,column=2)

cbb_4 = ttk.Combobox(face2.frame_2,value=course,width=5)
cbb_4.current(1)
cbb_4.grid(row=1,column=2)

button_run = Button(face2.frame_2,text="轉換",width=15,command=running).grid(row=2,column=1)

#creat menu
menubar = Menu(win)


opt_menu = Menu(menubar,tearoff=0,)
menubar.add_cascade(label="選項",menu=opt_menu)
opt_menu.add_command(label="時間",command=face2.change)
opt_menu.add_command(label="長度",command=face1.change)

win.config(menu=menubar)
win.mainloop()
