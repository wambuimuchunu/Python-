def most_frequent_char(string):
    
    char_count = {}

    for char in string:
        
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1  
    most_frequent = ''
    highest_count = 0

    
    for char, count in char_count.items():
        if count > highest_count:  
            highest_count = count  
            most_frequent = char  

    return most_frequent

user_input = input("Enter a string: ")

print("The most frequent character is:", most_frequent_char(user_input))
