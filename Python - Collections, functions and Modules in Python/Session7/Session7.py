#Q:-1

# Write a Python script that takes a string input from the user and prints a dictionary 
# showing how many times each character appears in the string.

text = input("Enter a string: ")

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)


#Q:-2

# Create a program that reads a short review (multi-line string) about your favorite food 
# delivery app (like Zomato or Swiggy) and counts the frequency of each word, displaying the 
# results as a dictionary.<br><br><em><strong>Hint:</strong> Convert all words to lowercase 
# and remove punctuation for accurate counting.</em>

review = """
Zomato is a good food delivery app.
Zomato has many restaurants and good offers.
I use Zomato to order food.
"""

review = review.lower()

punctuation = ".,!?;:"

for mark in punctuation:
    review = review.replace(mark, "")

words = review.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)



#Q:-3

# Given the following string: 'Virat scored 100, Rohit scored 80, and Gill scored 50 in the'
# ' IPL match', write a function word_freq_dict(text) that returns a dictionary with the 
# frequency of each word.

def word_freq_dict(text):
    punctuation = ".,!?;:"

    for mark in punctuation:
        text = text.replace(mark, "")

    words = text.lower().split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match."

result = word_freq_dict(text)

print(result)



#Q:-4

# Modify your word frequency program to ignore common stopwords like 
# 'the', 'and', 'in', 'of', 'a', 'to', 'is' when counting word frequencies.
# <br><br><em><strong>Constraint:</strong> Use a list of stopwords and filter them out 
# before counting.</em>

text = """
Zomato is a good food delivery app.
It is one of the popular apps to order food.
"""

stopwords = ["the", "and", "in", "of", "a", "to", "is"]

text = text.lower()

punctuation = ".,!?;:"

for mark in punctuation:
    text = text.replace(mark, "")

words = text.split()

word_count = {}

for word in words:
    if word not in stopwords:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

print(word_count)



#Q:-5

# Refactor your character count script to use a function named char_count_dict(text) 
# that returns the frequency dictionary, and then print the dictionary sorted by character 
# (A-Z or a-z).

def char_count_dict(text):
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


text = input("Enter a string: ")

result = char_count_dict(text)

sorted_result = dict(sorted(result.items()))

print(sorted_result)