
def count_words(filepath):
  with open(filepath, 'r', encoding='utf-8') as file:
    text = file.read()
  words = text.split()
  return len(words)

def count_characters(filepath):
  with open(filepath, 'r', encoding='utf-8') as file:
    text = file.read()
  
  lowercase_text = text.lower()
  
  character_counts = {}
  
  for character in lowercase_text:
    if character in character_counts:
      character_counts[character] += 1
    else:
      character_counts[character] = 1
  
  return character_counts


def pretty_report(filepath):
  count_characters_dict = count_characters(filepath)
  word_count = count_words(filepath)
  print("============ BOOKBOT ============")
  print(f"Analizing book found at: {filepath}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("---------- Character Count -------")
  for character, count in sorted(count_characters_dict.items()):
    if character.isalpha():  # Only print alphabetic characters
      print(f"{character}: {count}")
  print("----------- Word Count ----------")