sentence = input("Enter a word or a sentence to check if it is a palindrome: ")
joined_sentence = sentence.replace(" ", "") 
re_sentence  = ""

for i in reversed(range(len(joined_sentence))):
    re_sentence += joined_sentence[i]

if joined_sentence == re_sentence:
    print(f"{sentence} is a palindrome.")
else:
    print(f"{sentence} is not a palindrome.")
