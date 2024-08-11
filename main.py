def is_palindrome():
  s = input("Введите строку: ")
  if s == s[::-1]:
      print("yes")
  else:
      print("no")
is_palindrome()

def normalize_spaces():
  s = input("Введите строку с пробелами: ")
  normalized = ' '.join(s.split())
  print("Измененная строка:", normalized)
normalize_spaces()
