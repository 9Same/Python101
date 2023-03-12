unit = int(input("กรอกจำนวนของสินค้า : "))
price = float(input("กรอกราคาสินค้า : "))
member = input('คุณเป็น "สมาชิก" หรือไม่ ถ้าใช้ให้กด "y" ถ้าไม่ใช้ให้กด "n" :')
total = unit * price
discount = 0

if member == "y":
    if total <= 500:
        discount = total * 0.1
    elif total > 500 and total < 1000 :
        discount = total * 0.15
    else:
        discount = total * 0.20

elif member == "n":
    if total <= 500 :
        discount = total *0.05
    elif total > 500  and total < 1000 :
        discount = total * 0.1
    else:
        discount = total * 0.15

amount = total - discount

print("ยอดเงิน %.2f " % total)
print("ส่วนลด %.2f "% discount)
print("ยอดเงินสุทธิ %.2f " % amount)