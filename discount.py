	
purchase_amount = float(input("Enter the amount of purchase in KSh: "))

if purchase_amount > 1000:
    discount = purchase_amount * 0.05
    total_amount = purchase_amount - discount
    print(f"You qualify for a discount of KSh {discount:.2f}.")
else:
    total_amount = purchase_amount
print(f"The total amount to be paid is KSh {total_amount:.2f}.")
