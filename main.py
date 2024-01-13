import customtkinter as ctk
import darkdetect
from tkinter import *
import time
from times import Time
from PIL import ImageTk,Image
from database import Db


def screentime():

    flag = True
    mins,sec,hr = 0,0,0
    while flag:
        try:
            if sec < 59 and mins <=59 and hr <=23:
                sec += 1
            elif sec == 59 and mins <59 and hr <23:
                sec = 0
                mins += 1
            elif sec == 59 and mins == 59 and hr <23:
                hr += 1
                sec = 0
                mins= 0
            elif sec == 59 and mins == 59 and hr == 23:
                mins = 0
                sec= 0
                hr = 0
            txt = '{:02d}:{:02d}:{:02d}'.format(hr,mins, sec)
            label.place(relx = 0.5,rely= 0.1,anchor=N)
            label.config(text=txt)
            label.update() 
            time.sleep(1)
        except:
            return txt

            
        
app = Tk()
app.geometry("250x450")
app.wm_title("screenOntime")
app.config(bg="black")
app.iconphoto(False,PhotoImage(file='app icon/icon.png'))
app.resizable(False,False)

image = Image.open('themes/theme4.jpg')
img = ImageTk.PhotoImage(image)
img_label =  Label(app,image=img,background="black")
img_label.pack()

label = Label(app,text = "Hi",bg = "black",fg="white",font=('Times New Roman bold italic', 30))
label.pack()



db = Db()
tm = Time()
start = tm.started()
history = db.gethistory()
print(history)

card1 = Canvas(app,height = 35,width=230,bg = 'white')
card1.create_text(110,15,text= '1. ' + history[-1][0]+'-' + history[-1][1]+str(', ')+'delta:'+history[-1][2],fill='black',font=("Times", "11","bold italic"),anchor=CENTER,justify=CENTER)
card1.pack()
card1.place(relx=0.5,rely=0.65,anchor=CENTER)
card2 = Canvas(app,height = 35,width=230,bg = 'black')
card2.create_text(110,15,text='2. '+history[-2][0]+'-'+ history[-2][1]+str(', ')+'delta:'+history[-2][2],fill='white',font=("Times", "11","bold italic"),anchor=CENTER,justify = LEFT)
card2.pack()
card2.place(relx=0.5,rely=0.75,anchor=CENTER)
card3 = Canvas(app,height = 35,width=230,bg = 'black')
card3.create_text(110,15,text= '3. '+history[-3][0]+str('-')+ history[-3][1]+str(', ')+'delta:'+history[-3][2],fill='white',font=("Times", "11","bold italic"),anchor=CENTER,justify = LEFT)
card3.pack()
card3.place(relx=0.5,rely=0.85,anchor=CENTER)
card4 = Canvas(app,height =35,width=230,bg = 'black')
card4.create_text(110,15,text= '4.'+str(' ')+history[-4][0]+str('-') + history[-4][1]+str(', ')+'delta:'+history[-4][2],fill='white',font=("Times", "11","bold italic"),anchor=CENTER)
card4.pack()
card4.place(relx=0.5,rely=0.95,anchor=CENTER)

data = screentime()
end = tm.finished()
print(start)
print(end)
print(data)

db.insert([start,end,data])



app.mainloop()



    
        

 

    
    
    
    