s = input()
words = s.replace(',',' ').split()
cleaned_text = ' '.join(words)

print(cleaned_text)
print(len(words))