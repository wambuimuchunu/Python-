def filter_even_numbers(numbers):
    even_numbers = []  
  
    for num in numbers:
        if num % 2 == 0: 
            even_numbers.append(num)  
            
    return even_numbers


user_input = input("Enter a list of integers separated by spaces: ")


numbers_list = []  
for num in user_input.split():
    numbers_list.append(int(num))  


even_numbers = filter_even_numbers(numbers_list)
print("Even numbers:", even_numbers)
