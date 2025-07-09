from stats import pretty_report
import sys


def get_book_text(filepath):
  with open(filepath, 'r', encoding='utf-8') as file:
    file_contents = file.read()
  return file_contents

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  pretty_report(sys.argv[1])

main()