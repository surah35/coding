from tkinter import *  #導入Tkinter模組
win=Tk()
win.title('計算機')
win.geometry('330x340')
win.resizable(width=0, height=0) #設定寬度和高度都不能被調整
display=StringVar()
display.set('0')
textlabel=Label(win)
textlabel.config(bg='black',fg='white',width=36, height=7,font='50',anchor=E)#設定顯示面板顏色、大小、字體顏色、字體大小
textlabel['textvariable'] = display
textlabel.grid(row=0, column=0, columnspan=4)#設定顯示面板位置
#定義函示
def end():                                   #執行此函式時
    h=eval(display.get())                   #將顯示面板的值做運算
    display.set(str(h))                      #並將顯示面板設定成算出來的值
    
def updateDisplay(buttonString):             #執行此函式時
 content = display.get()                     
 if content == "0":                          #判斷如果顯示面板的數字是=0
     content = ""                            #將顯示面板變為空白
 display.set(content + buttonString)         #將顯示面板判斷的結果+按鈕的字串
 
def backspace():                             #執行此函式時
    display.set(str(display.get()[:-1]))     #將顯示面板的字串消去一個
    if len(str(display.get())) == 0:
          display.set('0')
          
def clear():                                 #執行此函式時
    display.set('0')                         #將顯示面板設定=0
    

def change():                                #執行此函式時
    if '-' in str(display.get()) :           #判斷如果顯示面板中有'-'字元
     display.set(''+display.get()[1:])     #將'-'換成''(空字元)
    elif '0' in str(display.get()):
     display.set('0') 
    else :                                   #判斷如果顯示面板中沒有'-'字元
     display.set('-'+str(display.get()))     #將'-'+顯示面板的字串
#按鈕設定    
Button(win, text = '+', width = 8, height = 2,bg = 'orange',font=('100') , command = lambda:updateDisplay('+')).grid(row = 1, column = 3)
Button(win, text = '-', width = 8, height = 2,bg = 'orange',font=('100') ,command = lambda:updateDisplay('-')).grid(row = 2, column = 3)
Button(win, text = '×', width = 8, height = 2,bg = 'orange',font=('100') , command = lambda:updateDisplay('*')).grid(row = 3, column = 3)
Button(win, text = '÷',width = 8, height = 2,bg = 'orange', font=('100') ,command = lambda:updateDisplay('/')).grid(row = 4, column = 3)
Button(win, text = '←', width = 8, height = 2,bg = 'black',fg='white',font=('100') , command = backspace).grid(row = 1, column = 1)
Button(win, text = 'c', width = 8, height = 2,bg = 'black',fg='white',font=('100') , command = clear).grid(row = 1, column = 0)
Button(win, text = '+/-', width = 8, height = 2,bg = 'black',fg='white',font=('100') , command =change).grid(row = 1, column = 2)
Button(win, text = '0', width = 17, height = 2,bg = 'black',fg='white' ,font=('100') , command = lambda:updateDisplay('0')).grid(row = 5, column = 0, columnspan = 2)
Button(win, text = '1', width = 8, height = 2,bg = 'black',fg='white' ,font=('100') , command = lambda:updateDisplay('1')).grid(row = 4, column= 0)
Button(win, text = '2', width = 8, height = 2,bg = 'black',fg='white' ,font=('100') , command = lambda:updateDisplay('2')).grid(row = 4, column= 1)
Button(win, text = '3', width = 8, height = 2,bg = 'black',fg='white' ,font=('100') , command = lambda:updateDisplay('3')).grid(row = 4, column = 2)
Button(win, text = '4', width = 8, height = 2,bg = 'black',fg='white' ,font=('100') , command = lambda:updateDisplay('4')).grid(row = 3, column = 0)
Button(win, text = '5', width = 8, height = 2,bg = 'black',fg='white' ,font=('100') , command = lambda:updateDisplay('5')).grid(row = 3, column = 1)
Button(win, text = '6', width = 8, height = 2,bg = 'black',fg='white' ,font=('100') , command = lambda:updateDisplay('6')).grid(row = 3, column = 2)
Button(win, text = '7', width = 8, height = 2,bg = 'black',fg='white' ,font=('100') , command = lambda:updateDisplay('7')).grid(row = 2, column = 0)
Button(win, text = '8', width = 8, height = 2,bg = 'black',fg='white' ,font=('100') , command = lambda:updateDisplay('8')).grid(row = 2, column = 1)
Button(win, text = '9', width = 8, height = 2,bg = 'black',fg='white' ,font=('100') , command = lambda:updateDisplay('9')).grid(row = 2, column = 2)
Button(win, text = '=', width = 8, bg = 'orange', height = 2,font=('100') ,command = lambda:end()).grid(row = 5, column = 3)
Button(win, text = '.', width = 8, height = 2,bg = 'black',fg='white' ,font=('100') ,command = lambda:updateDisplay('.')).grid(row = 5, column = 2)

        


win.mainloop()

