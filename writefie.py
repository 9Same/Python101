
def writedata():
    with open('data.text','w',encoding='utf-8') as file:
        file.write('สะบายดีไหม?')

#### (text) สามารถเพิ่มข้อมูลใน Text ได้ ###
def adddata(text):
    with open('add-data.text','a',encoding='utf-8') as file:
        file.writelines(text + '\n')

def readdata():
    with open('add-data.text',encoding='utf-8') as file:
        #data = file.readlines() # export to list  .readline คือ การอ่านทีละบรรทัด
        data = file.read() ###.read คือ การอ่านทั้งหมด
        print(data)
readdata()

#adddata('ยางลบ 100 บาท')
#adddata('สมุดวาดรูป 70 บาท')
#adddata('กบเหลา 120 บาท')

