def count(text):
    strings = text.split()  # Directly split and store in strings
    word_count = len(strings)
    return word_count

def character_count(text):
    dictionary = {}  # Initialize an empty dictionary
    for x in text:
        x = x.lower()  # Convert character to lowercase
        if x.isalpha():  # Consider only alphabetic characters
            if x not in dictionary:
                dictionary[x] = 1
            else:
                dictionary[x] += 1
    return dictionary

def sort_on(dict_item):
    return dict_item["num"]

def report(file_path, word_count, dictionary):
    # Convert the dictionary into a list of dictionaries for sorting
    char_list = [{"char": k, "num": v} for k, v in dictionary.items()]
    
    # Sort the list by frequency of characters in descending order
    char_list.sort(reverse=True, key=sort_on)
    
    # Print the report header
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    # Print each character and its frequency
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    # Print the report footer
    print("--- End report ---")

def main():
    file_path = "/home/onbekende/workspace/books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
        
        # Count the words in the text
        word_count = count(file_contents)
        
        # Generate the character count dictionary
        dictionary = character_count(file_contents)
        
        # Print the report of character frequencies
        report(file_path, word_count, dictionary)

main()
