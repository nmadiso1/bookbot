
def word_count(text):
    return text.split()


def char_count(text):
    
    char_dict = {}

    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
        
    return char_dict


def sort_char(char_dict):
    return char_dict["num"]
