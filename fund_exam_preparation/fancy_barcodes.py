import re

count_of_barcodes = int(input())

for _ in range(count_of_barcodes):
    match = []
    barcode = input()
    match = re.findall(r"@[#]+(\b[A-Z][a-zA-Z0-9]{4,}[A-Z])@[#]+", barcode)
    if match:
        digits = re.findall(r"[\d]+", match[0])
        if digits:
            res = "".join(digits)
            print(f"Product group: {res}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
