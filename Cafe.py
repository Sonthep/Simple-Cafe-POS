# V5 - Refactored with Functions (Corrected Version)

class menuItem:
    """A class to represent an item on the cafe menu."""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} {self.price:.2f} บาท"
        
# ----- DATA (Store's primary data) -----
# Using all caps is a convention for constants.
MENU_ITEMS = [
    menuItem("Americano", 55.75),
    menuItem("Latte", 60.15),
    menuItem("Espresso", 50.15),
    menuItem("Cappuccino", 65.00)
]

# ----- FUNCTIONS (Custom tools) -----

def display_menu(menu):
    """Function to display the menu."""
    print("กรุณาเลือกรายการที่ต้องการ (กด 0 เพื่อคิดเงิน)")
    for i, item in enumerate(menu):
        # CORRECTED: Use dot notation (item.name) for object attributes
        print(f"{i+1}. {item.name} {item.price:.2f} บาท")

def print_receipt(order_list, total):
    """Function to print the final receipt."""
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

    # --- Promotional Discount ---
    if total > 100:
        discount = total * 0.1
        final_price = total - discount
        print(f"ส่วนลด 10% : -{discount:.2f} บาท")
        print(f"ยอดสุทธิที่ต้องชำระ: {final_price:.2f} บาท")

    print("\nขอบคุณที่มาใช้บริการครับ")
    print("========================")

# ----- MAIN APPLICATION LOGIC -----

def main():
    """The main function that controls the program's flow."""
    print("Welcome to the Zodiac Cafe POS V5")
    
    running_total = 0
    order_list = []

    while True:
        display_menu(MENU_ITEMS) # Call the menu display function
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
            
            # CORRECTED: Use dot notation for object attributes
            unit_price = selected_item.price
            line_total = unit_price * quantity
            running_total += line_total
            
            # This part is correct, as it creates a new dictionary for the order list
            order_list.append({
                "name": selected_item.name, # CORRECTED
                "quantity": quantity,
                "unit_price": unit_price,
                "line_total": line_total
            })
            
            # CORRECTED: Use dot notation for the print statement
            print(f"เพิ่ม '{selected_item.name} x{quantity}' เรียบร้อย")
            print(f"ยอดชั่วคราว: {running_total:.2f} บาท\n")

        else:
            print("ขออภัย ไม่มีเมนูที่คุณเลือก กรุณาเลือกใหม่อีกครั้ง")
            
    # After the loop ends, call the receipt printing function
    print_receipt(order_list, running_total)

# ----- ENTRY POINT (Program's starting point) -----
# This is a standard convention in Python to call the main() function.
if __name__ == "__main__":
    main()