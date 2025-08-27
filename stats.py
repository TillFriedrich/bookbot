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

def get_words(text):
  words = text.lower()
  word_list = {
    
  }
  for word in words.split():
    if word in word_list:
      word_list[word] += 1
    else:
     word_list[word] = 1
#  print(word_list)
  return word_list

def sort_word_dictionary(dictionary):
  dict_list = []
  for key in dictionary:
    dictionaries = {
      "word" : key,
      "num" : dictionary[key]
    }
    dict_list.append(dictionaries)
  dict_list.sort(key=sort_on, reverse=True)
  return dict_list