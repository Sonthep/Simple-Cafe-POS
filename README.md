# Zodiac Cafe POS

A small Python command-line project that models a cafe order from menu selection to an itemized receipt.

**Project type:** Learning project  
**ภาษาไทย:** โปรเจกต์ฝึก Python สำหรับรับออร์เดอร์ร้านกาแฟ คำนวณยอดรวม และพิมพ์บิลผ่าน Terminal

## What it demonstrates

- A `menuItem` class for menu names and prices.
- Functions that separate menu display, order input, and receipt output.
- Validation for menu choices and positive integer quantities.
- A list of order dictionaries containing quantity, unit price, and line total.
- A 10% discount when the subtotal is **greater than THB 100**.

## Run locally

Requires Python 3 with f-string support. The application uses the standard library only.

```bash
git clone https://github.com/Sonthep/Simple-Cafe-POS.git
cd Simple-Cafe-POS
python Cafe.py
```

On systems where Python 3 is named `python3`, use `python3 Cafe.py`.

1. Select a menu number from 1 to 4.
2. Enter a positive quantity.
3. Repeat to add more items.
4. Enter 0 to print the receipt and exit.

## Menu

| Item | Price (THB) |
| --- | ---: |
| Americano | 55.75 |
| Latte | 60.15 |
| Espresso | 50.15 |
| Cappuccino | 65.00 |

For example, two Lattes and one Americano produce a subtotal of THB 176.05. The application displays a 10% discount and a net total rounded to two decimal places.

## Source guide

All application code is in [Cafe.py](Cafe.py).

| Symbol | Responsibility |
| --- | --- |
| `menuItem` | Represent a menu item |
| `MENU_ITEMS` | Define the cafe menu |
| `display_menu()` | Print available items |
| `main()` | Read and validate orders |
| `print_receipt()` | Display line items, subtotal, and applicable discount |

## Scope and limitations

Orders exist only for the current session. This project does not implement a database, stock tracking, payment processing, a graphical interface, or receipt-printer integration.

Prices use Python floating-point arithmetic and are formatted to two decimal places. A production payment system would need explicit monetary rounding rules. For subtotals at or below THB 100, the current receipt prints the subtotal without a separate net-total line.

## Possible extensions

Persist receipts, add automated calculation tests, use decimal arithmetic for prices, and introduce stock tracking. These are future ideas, not implemented features.

## Author

[Sonthep](https://github.com/Sonthep)
