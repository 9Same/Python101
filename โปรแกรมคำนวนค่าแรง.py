import tkinter
import datetime
from tkinter import *
from tkinter import messagebox


def Button_click():
    M1 = T1.get()  ### get คือการดึงค่าข้อมูลที่กรอกในช่อง Entry ###
    a = int(M1)
    M2 = T2.get()
    b = int(M2)
    M3 = T3.get()
    c = int(M3)
    d = (a * b) + (c * 50)
    print(d)
    text = "ยอดเงินของคุณ"
    messagebox.showinfo(text, "กำลังประมวลผล")
    T4.delete(0, tkinter.END)
    T4.insert(0, d)  ## insert ใช้ในการแสดงค่า ใช้ได้กลับ Entry เท่านั้น ###


### รับค่ามา เเล้ว นำไปหาค่าเงิน  #####

############# CSV Datalist################
import csv


def writcsv(datalist):
    with open('data1.csv', 'a', encoding='utf-8', newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)


def readcvs():
    with open('data1.csv', encoding='uft-8', newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data


##########################################

GUI = Tk()
GUI.title('โปรแกรมคำนวนค่าแรง')
GUI.geometry("900x700")
L1 = Label(GUI, text='โปรแกรมคำนวนเงินเดือน', font=('Angsana New', 30))
L1.pack(ipadx=20, ipady=20)

L2 = Label(GUI, text='ค่าแรงรายวัน', font=('Angsana New', 18))
L2.place(x=200, y=130)

T1 = Entry(GUI, font=('Angsana New', 18))
T1.place(x=450, y=130)

L3 = Label(GUI, text='จำนวนวันที่ทำงาน', font=('Angsana New', 18))
L3.place(x=200, y=230)

T2 = Entry(GUI, font=('Angsana New', 18))
T2.place(x=450, y=230)

L4 = Label(GUI, text='ทำงานล่วงเวลา OT (50บ/1 ชม) ', font=('Angsana New', 18))
L4.place(x=200, y=330)

T3 = Entry(GUI, font=('Angsana New', 18))
T3.place(x=450, y=330)

L5 = Label(GUI, text='ยอดเงินสุทธิ์', font=('Angsana New', 18))
L5.place(x=200, y=430)

v_data = StringVar()  # ดึงข้อมูลจากข้อความ GUI
T4 = Entry(GUI, textvariable=v_data, font=('Angsana New', 18), bg='green', fg='white')
T4.place(x=450, y=430)

B1 = Button(GUI, text='ประมวลผล', command=Button_click, font=('Angsana New', 20))
B1.place(x=350, y=500)


################## SaveData #####################################
def Savedata():
    t = datetime.datetime.now().strftime('ปี %Y เดือน %m วัน %d : เวลา %H นาฬิกา %M นาที  %S วินาที')
    data = v_data.get()  # ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    a = 'เงินสุทธิ์'
    text = [t, a, data]  # [เวลา,ข้อมูลที่ดึงมา]
    writcsv(text)  # บันทึกข้อมูลลง csv
    v_data.set('')


#################################################################
B2 = Button(GUI, text='บันทึก', command=Savedata, font=('Andsana New', 20))
B2.place(x=470, y=500)

GUI.mainloop()
