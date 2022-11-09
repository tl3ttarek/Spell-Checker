import difflib

f = open("dictionary.txt", 'r')
dic = f.readlines()

def binary_search(alist, word):
  l, h = 0, len(alist)

  while l <= h:
    m = (h + l) // 2
    if word == alist[m]:
      return True
    elif alist[m] > word:
      h = m - 1
    else:
      l = m + 1

  return False

def is_correct(word):
  return binary_search(dic, word)

def spell_checker(word):
  if(not is_correct(word)):
    print(f'Word "{word}" is not right.')
    print(f'Do you mean "{suggest_word(word)}"?')

def suggest_word(word):
  ans = dic[0]
  score = 0
  for w in dic:
    f = difflib.SequenceMatcher(None, w, word)
    if f.ratio() > score:
      ans = w
      score = f.ratio()
  return ans[0:-1]

if __name__ == "__main__":
  text = input("Enter your text: ")
  list_of_text = text.split()
  for word in list_of_text:
    spell_checker(word)
