# Problem Task 02 - Week03


# This is a program that asks a user to input a string sentence 
# which is outputted in reverse order with every second letter skipped

# Author: Caoimhin Vallely

# asks the user to input a string sentence
sentence = input('Please enter a string sentence: ')
sentence_reverse = sentence[::-1] # reverses the sentence
sentence_skip = sentence_reverse[::2] # skips every second letter
print(sentence_skip) # prints the result