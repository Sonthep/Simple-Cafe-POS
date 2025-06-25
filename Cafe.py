# V5 - Refactored with Functions

# ----- DATA (ข้อมูลหลักของร้าน) -----
# การตั้งชื่อตัวแปรเป็นตัวพิมพ์ใหญ่ทั้งหมด เป็นข้อตกลงว่าข้อมูลนี้เป็นค่าคงที่ (Constant)
MENU_ITEMS = [
    {"name": "Americano", "price": 55.75},
    {"name": "Latte", "price": 60.15},
    {"name": "Espresso", "price": 50.15},
    {"name": "Cappuccino", "price": 65.00}
]

# ----- FUNCTIONS (เครื่องมือที่เราสร้างขึ้น) -----

def display_menu(menu):
    """ฟังก์ชันสำหรับแสดงผลเมนู"""
    print("กรุณาเลือกรายการที่ต้องการ (กด 0 เพื่อคิดเงิน)")
    for i, item in enumerate(menu):
        print(f"{i+1}. {item['name']} {item['price']:.2f} บาท")

def print_receipt(order_list, total):
    """ฟังก์ชันสำหรับพิมพ์ใบเสร็จทั้งหมด"""
    print("\n========================")
    print("        รายการสั่งซื้อ (บิล)")
    print("------------------------")

    if not order_list:
        print("    *** ไม่มีรายการสั่งซื้อ ***")
    else:
        for item in order_list:
            print(f"- {item['name']} x{item['quantity']} (หน่วยละ {item['unit_price']:.2f}) \t= {item['line_total']:.2f} บาท")

    print("------------------------")
    print(f"ยอดรวมทั้งหมด : {total:.2f} บาท")

    # --- ส่วนลดโปรโมชั่น ---
    if total > 100:
        discount = total * 0.1
        final_price = total - discount
        print(f"ส่วนลด 10% : -{discount:.2f} บาท")
        print(f"ยอดสุทธิที่ต้องชำระ: {final_price:.2f} บาท")

    print("\nขอบคุณที่มาใช้บริการครับ")
    print("========================")

# ----- MAIN APPLICATION LOGIC -----

def main():
    """ฟังก์ชันหลักที่ควบคุมการทำงานของโปรแกรมทั้งหมด"""
    print("Welcome to the Zodiac Cafe POS V5")
    
    running_total = 0
    order_list = []

    while True:
        display_menu(MENU_ITEMS) # เรียกใช้ฟังก์ชันแสดงเมนู
        print("-" * 30)
        order_input = input("กรุณาเลือกเมนู (1-4) หรือ 0 เพื่อสรุปยอด: ")
        
        if not order_input.isdigit():
            print("กรุณาป้อนเป็นตัวเลขเท่านั้น")
            continue

        order = int(order_input)
        
        if order == 0:
            break

        if 1 <= order <= len(MENU_ITEMS):
            quantity_input = input("กรุณาระบุจำนวน: ")
            if not quantity_input.isdigit() or int(quantity_input) <= 0:
                print("กรุณาป้อนจำนวนเป็นตัวเลขที่มากกว่า 0")
                continue
            
            quantity = int(quantity_input)
            
            selected_item = MENU_ITEMS[order - 1]
            unit_price = selected_item['price']
            line_total = unit_price * quantity
            running_total += line_total
            
            order_list.append({
                "name": selected_item['name'],
                "quantity": quantity,
                "unit_price": unit_price,
                "line_total": line_total
            })
            
            print(f"เพิ่ม '{selected_item['name']} x{quantity}' เรียบร้อย")
            print(f"ยอดชั่วคราว: {running_total:.2f} บาท")

        else:
            print("ขออภัย ไม่มีเมนูที่คุณเลือก กรุณาเลือกใหม่อีกครั้ง")
            
    # หลังจากออกจาก Loop แล้ว ให้เรียกใช้ฟังก์ชันพิมพ์ใบเสร็จ
    print_receipt(order_list, running_total)

# ----- ENTRY POINT (จุดเริ่มต้นของโปรแกรม) -----
# เป็นข้อตกลงใน Python ว่าจะเรียกฟังก์ชัน main() จากตรงนี้
if __name__ == "__main__":
    main()