from faulthandler import disable
from os import link, remove
import tkinter
from tkinter import *
from turtle import textinput, width
from click import command
import webbrowser

# creat windows
win = Tk()
win.title("BMI計算機")
win.geometry("350x200")
win.resizable(False,False)

# funtion defind
def calculate():
    height = int(entry_h.get())
    weight = int(entry_w.get())
    height = height/100
    BMI = round(weight/(height**2),2)
    label['text'] =  BMI
    if BMI > 24:
        label_inform['text'] = "請注意，體重過重"
    elif BMI < 18.5:
        label_inform['text'] = "請注意，體重過輕"
    else:
        label_inform['text'] = "體重適中，請繼續保持"

def reset():
    entry_h.delete(0,'end')
    entry_w.delete(0,'end')
    label['text'] = ""
    label_inform['text'] = ""

def link_web():
    webbrowser.open_new("https://www.hpa.gov.tw/Pages/Detail.aspx?nodeid=542&pid=9737")
    
#物件

label_h = Label(text="請輸入身高(cm)：")
label_h.config(font=20)
label_h.grid(row=1,column=0)

label_w = Label(text="請輸入體重(kg)：")
label_w.config(font=20)
label_w.grid(row=2,column=0)

entry_h = Entry(font=20)
entry_h.grid(row=1,column=1)

entry_w = Entry(font=20)
entry_w.grid(row=2,column=1)

button_reset = Button(text="重置",command=reset)
button_reset.config(font=20)
button_reset.grid(row=3,column=0)

button = Button(text="計算",command=calculate)
button.config(font=20)
button.grid(row=3,column=1)

label_A = Label(text="計算結果：")
label_A.config(font=20)
label_A.grid(row=4,column=0)

label = Label()
label.config(font=20)
label.grid(row=4,column=1)

label_inform = Label(font=30,fg="red")
label_inform.grid(row=6,column=1)

button_web = Button(text="資料來源：衛生福利部全民健康署",
font=("times",13,"underline"),fg="blue",command=link_web)
button_web.config()
button_web.grid(row=8,column=0,columnspan=2)


#------------------------------


win.mainloop()