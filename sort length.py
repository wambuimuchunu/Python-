#Python Function
def sort_by_length(words):
    
    sorted_words = sorted(words, key=len)
    return sorted_words


words_list = ["chiken", "lion", "dog", "cheeter", "ant"]
print("Words sorted by length:", sort_by_length(words_list))
