box = []
box.append('ปากกา')
box.append('ดินสอ')
box.append('ยาง')
print(box[1])
print(box[0])
print(box[2])
#### .append คือการเก็บข้อมูล เเละเรียกใช้ในรูปแบบ Array

brand = {'pen':['Lamy','Pentel','Fiber-castell'],'pencil':['hourse','staedler'],'eraser':'ยางลบ 2 สี'}
print(brand['pen']) # จะได้ข้อมูลมาทั้งก้อน
print(brand['pen'][1])
print(brand['eraser'])

print(brand.keys())
print(brand.values())


for b in box:
    print(b)

for br in brand.keys():
    print(br)

for br in brand.values():
    print(br)

for br in brand:
    print(br)

for br in brand.items():
    print(br)