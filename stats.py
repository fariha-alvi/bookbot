# Function to return the number of words in the string that is passed
def get_num_words(contents):
    words = contents.split()
    return len(words)

# Function to return a dictionary with characters and their counts in the string that is passed
def get_num_chars(contents):
    num_chars = {}
    for c in contents:
        if c.lower() in num_chars:
            num_chars[c.lower()] += 1
        else:
            num_chars[c.lower()] = 1
    return(num_chars)   

# Function that returns the char count dictionary sorted by counts
def get_sorted_num_chars(num_chars):
    num_chars_list = []
    for key, value in num_chars.items():
        num_chars_list.append({"char": key, "num": value})
    num_chars_list.sort(reverse=True, key=lambda x: x["num"])
    return(num_chars_list)