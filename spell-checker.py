def spell_checker(word):
  if(not is_correct(word)):
    print(f'Word "{word}" is not right.')
    print(f'Do you mean "{suggest_word(word)}"?')


def is_correct(word):
  pass

def suggest_word(word):
  pass

if __name__ == "__main__":
  text = input("Enter your text: ")
  list_of_text = text.split()
  for word in list_of_text:
    spell_checker(word)