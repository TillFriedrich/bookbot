from stats import count_words, count_letters, sort_dictionary, get_words, sort_word_dictionary
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
  
  words = get_words(buch)
#  print(words)
  print("----- Most common words --------")
  sorted_word_dict = sort_word_dictionary(words)
  for i in range(10):
    if sorted_word_dict[i]["num"] > 3:
      print(sorted_word_dict[i]["word"]+ ": " + str(sorted_word_dict[i]["num"]))
main()