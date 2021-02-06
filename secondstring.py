# Program that asks a user to input a string and outputs every second letter in reverse order
# Author: Caoimhin Vallely

sentence = input('Please enter a string sentence: ')
sentenceReverse = sentence[::-1] # reverses the sentence
sentenceSkip = sentenceReverse[::2] # prints every second letter
print(sentenceSkip)