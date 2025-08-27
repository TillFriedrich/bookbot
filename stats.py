def count_words(text):
  num_words = 0
  words = text.split()
  for w in words:
    num_words += 1  
  return num_words
  
def count_letters(text):
  letters = {
    
  }
  for letter in text.lower():
    if letter in letters:
      letters[letter] += 1
    else:
      letters[letter] = 1
  return letters

def sort_on(item):
  return item["num"]

def sort_dictionary(dictionary):
  dict_list = []
  for key in dictionary:
    if key.isalpha():
      dictionaries = {
        "char" : key,
        "num": dictionary[key]
      }
      dict_list.append(dictionaries)
#  print(dict_list)
  dict_list.sort(key=sort_on, reverse=True)
  return dict_list