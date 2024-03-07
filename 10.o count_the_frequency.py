# • Write a Python program to count the frequency of words in a file.


with open("q-1.txt", 'r') as f:
    text = f.read()

word_list = text.split()
word_count = {}

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key, value in word_count.items():
    print(f"{key} :- {value} ")
