# Exercise 25
# LPTHW
# Even More Practice
# Page 86 (PDF page 101)

# similar to the last exercise, more practice using the principles we 
	# covered so far
    
# after saving this script, i imported it into the python interpreter
# using exer25.functionName you are able to tell the interpreter
    # that you want to use the function inside of the module
	
def break_words(stuff):
    """This function will break up words for us."""
    # this is another way to comment called documentation
    # will show up in help()
    words = stuff.split(' ')
    return words
    
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
    
def print_first_word(words):
    """prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
# can import everything from exer25 by typing
    # from exer25 import *

