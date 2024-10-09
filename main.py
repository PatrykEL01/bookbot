characters_dict = {}
word_count = None
with open("books/frankenstein.txt") as file:
    text = file.read()
    words = text.split()
    
    # count words
    word_count = len(words)
    print(word_count)
    
    #count characters
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():
            characters_dict[char] = characters_dict.get(char, 0) + 1
    #print(characters_dict)
    

# write a report to stdout
for char, count in characters_dict.items():
    print(f"The {char} was found {count} times.")