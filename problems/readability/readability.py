from cs50 import get_string

# Get the string from user
INPUT = get_string("Text: ")


# Number of letters, words, sentences
letters = 0
words = 1
sentences = 0
for char in INPUT:
    if char.isalpha():
        letters += 1
    if char.isspace():
        words += 1
    if char in ['?', '.', '!']:
        sentences += 1


# Use coleman-liau to get grade
L = (letters * 100.0) / words
S = (sentences * 100.0) / words
last_grade = int((0.0588 * L - 0.296 * S - 15.8) + 0.5)


# Print the grade
if last_grade < 1:
    print("Before Grade 1")
elif last_grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {last_grade}")
