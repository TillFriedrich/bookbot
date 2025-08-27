from stats import count_words, count_letters, sort_dictionary
import sys

def get_book_text(file_path):
  with open(file_path) as f:
    contents = f.read()
  return contents


def main():
  if 2 > len(sys.argv):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  print(sys.argv[0])
  buch = get_book_text(sys.argv[1])
  print("============ BOOKBOT ============")
#  print(buch) 
  print(f"Analyzing book found at {sys.argv[1]}")
  num_words = count_words(buch)
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  num_letters = count_letters(buch)
#  print(num_letters)
  
  sorted_dict = sort_dictionary(num_letters)
  for i in range(len(sorted_dict)):
    print(sorted_dict[i]["char"]+ ": " + str(sorted_dict[i]["num"]))
  
main()