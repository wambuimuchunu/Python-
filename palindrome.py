def is_palindrome(string):
    
    cleaned_string = ""
    for char in string:
        if char != " ":  
            cleaned_string += char.lower()  

    
    reversed_string = ""
    for char in cleaned_string:
        reversed_string = char + reversed_string  

    
    if cleaned_string == reversed_string:
        return True  
    else:
        return False  


words_to_check = ["mum", "dud", "nurses run"]


for word in words_to_check:
    if is_palindrome(word):
        print(word, "is a palindrome.")
    else:
        print(word, "is not a palindrome.")
