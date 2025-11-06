char_numbers = {}

def get_words_numbers(a):
    
    return len(a.split())

def get_char_numbers(a):
    char_numbers = {}
    
    for b in a.lower().split():
        for c in list(b):
            if c in char_numbers:
                char_numbers[c] += 1
            else:
                char_numbers[c] = 1

    return char_numbers
    
def sort_on(items):
    return items["num"]
    
def sorted_list(a):
    emty_list = []

    for b in a:
        emty_dictionary = {"char": "", "num": 0}
        emty_dictionary["char"] = b
        emty_dictionary["num"] = a[b]
        emty_list.append(emty_dictionary)

    emty_list.sort(reverse=True, key=sort_on)
    return emty_list
