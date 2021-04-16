# Problem Task 02 (06/02/21)

# This is a program that asks a user to input a string sentence 
# which is outputted in reverse order with every second letter skipped

# Author: Caoimhin Vallely

# asks the user to input a string sentence
sentence = input('Please enter a string sentence: ')
sentence_reverse = sentence[::-1] # reverses the sentence and stores as variable 'sentence_reverse'
print(sentence_reverse[::2]) # prints the sentence with every second letter skipped