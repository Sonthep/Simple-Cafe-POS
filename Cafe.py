print("Welcome to the coffee shop!")
#สร้างสินค้าและราคา
americano_price = 55.75
latte_price = 60.15
espresso_price = 50.15
cappuccino_price = 65.00

#แสดงรายการสินค้า
print("กรุณาเลือกรายการที่ต้องการ")
print(f"1. Americano {americano_price} บาท")
print(f"2. Latte {latte_price} บาท")
print(f"3. Espresso {espresso_price} บาท")
print(f"4. Cappuccino {cappuccino_price} บาท")

#รับออเดอร์ เลือกสินค้า และจำนวน
order = int(input("กรุณาเลือกเมนู (1-4): "))
quantity = int(input("กรุณาระบุจำนวน: "))



#คำนวณราคา
if order == 1:
    total_price = americano_price * quantity
elif order == 2:
    total_price = latte_price * quantity
elif order == 3:
    total_price = espresso_price * quantity
elif order == 4:
    total_price = cappuccino_price * quantity


print(f"ราคารวมทั้งหมด: {total_price} บาท")
print("ขอบคุณที่มาใช้บริการครับ")
