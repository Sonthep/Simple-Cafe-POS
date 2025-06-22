print("Welcome to the Zodiac Cafe POS V4")

# สร้างรายการเมนูพร้อมราคา
menu_items = [
    {"name": "Americano", "price": 55.75},
    {"name": "Latte", "price": 60.15},
    {"name": "Espresso", "price": 50.15},
    {"name": "Cappuccino", "price": 65.00}
]

# แสดงรายการสินค้า
print("กรุณาเลือกรายการที่ต้องการ (กด 0 เพื่อคิดเงิน)")
for i, item in enumerate(menu_items):
    print(f"{i+1}. {item['name']} {item['price']:.2f} บาท")

running_total = 0
order_list = [] 

# รับออเดอร์ เลือกสินค้า และจำนวน
while True:
    print("-" * 30)
    order_input = input("กรุณาเลือกเมนู (1-4) หรือ 0 เพื่อสรุปยอด: ")
    
    if not order_input.isdigit():
        print("กรุณาป้อนเป็นตัวเลขเท่านั้น")
        continue

    order = int(order_input)
    
    if order == 0:
        break

    if 1 <= order <= len(menu_items):
        quantity_input = input("กรุณาระบุจำนวน: ")
        if not quantity_input.isdigit() or int(quantity_input) <= 0:
            print("กรุณาป้อนจำนวนเป็นตัวเลขที่มากกว่า 0")
            continue
        
        quantity = int(quantity_input)
        
        selected_item = menu_items[order - 1]
        item_name = selected_item['name']
        unit_price = selected_item['price'] ### แก้ไข: ใช้ชื่อตัวแปร unit_price ให้ชัดเจน
        
        line_total = unit_price * quantity
        running_total += line_total
        
        # ### แก้ไขจุดที่ 1: เพิ่ม 'unit_price' เข้าไปใน dictionary ที่จะเก็บ
        order_list.append({
            "name": item_name,
            "quantity": quantity,
            "unit_price": unit_price, # เก็บราคาต่อหน่วย
            "line_total": line_total
        })
        
        print(f"เพิ่ม '{item_name} x{quantity}' เรียบร้อย")
        print(f"ยอดชั่วคราว: {running_total:.2f} บาท")

    else:
        print("ขออภัย ไม่มีเมนูที่คุณเลือก กรุณาเลือกใหม่อีกครั้ง")
    
# สรุปยอด
print("\n========================")
print("        รายการสั่งซื้อ (บิล)")
print("------------------------")

if not order_list:
    print("      *** ไม่มีรายการสั่งซื้อ ***")
else:
    for item in order_list:
        # ### แก้ไขจุดที่ 2: เพิ่มการแสดงผล (หน่วยละ xx.xx) เข้าไปในบิล
        print(f"- {item['name']} x{item['quantity']} (หน่วยละ {item['unit_price']:.2f}) \t= {item['line_total']:.2f} บาท")

print("------------------------")
print(f"ยอดรวมทั้งหมด : {running_total:.2f} บาท")

# --- ส่วนลดโปรโมชั่น ---
if running_total > 100:
    discount = running_total * 0.1
    final_price = running_total - discount
    print(f"ส่วนลด 10% : -{discount:.2f} บาท")
    print(f"ยอดสุทธิที่ต้องชำระ: {final_price:.2f} บาท")

print("\nขอบคุณที่มาใช้บริการครับ")
print("========================")