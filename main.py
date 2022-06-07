def count_letter(words, letter):
  i = 0
  for word in words:
    if letter in word:
      i += 1
  return i

print(count_letter(['python', 'c++', 'c', 'scala', 'java'], '+'))