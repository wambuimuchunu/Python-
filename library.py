from datetime import datetime

def calculate_fine(due_date, return_date):
    # Convert string dates to datetime objects
    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    return_date = datetime.strptime(return_date, "%Y-%m-%d")
    
    # Calculate days overdue
    days_overdue = (return_date - due_date).days
    
    # Determine fine rate based on days overdue
    if days_overdue <= 0:
        fine_rate = 0
    elif 0< days_overdue <= 7:
        fine_rate = 20
    elif 8 <= days_overdue <= 14:
        fine_rate = 50
    else:
        fine_rate = 100
        
    # Calculate fine amount
    fine_amount = days_overdue * fine_rate
    
    return days_overdue, fine_rate, fine_amount

# Inputs from the user
book_id = input("Enter Book ID: ")
due_date = input("Enter Due Date (YYYY-MM-DD): ")
return_date = input("Enter Return Date (YYYY-MM-DD): ")

# Calculate fine
days_overdue, fine_rate, fine_amount = calculate_fine(due_date, return_date)

# Display results
print("\nBook ID:", book_id)
print("Return Date:", return_date)
print("Days Overdue:", days_overdue)
print("Fine Rate: Ksh", fine_rate)
print("Fine Amount: Ksh", fine_amount)
