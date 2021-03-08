import random

#Ask the user for a string and print out whether this string is a palindrome
#or not. (A palindrome is a string that reads the same forwards and backwards.)

# setup user input
# read string forward and backwards and compare
# userinput[0] == userinput[len(userinput)-1]
# userinput[1] == userinput[len(userinput)-2]
# ignore punctuation

def palindromechecker(word):
    x = 0
    y = len(word) - 1
    c = []
    for i in word:
        if i == word[y]:
            c.append(i)
            x += 1
            y -= 1
        else:
            print("sorry this is not a palindrome")
            break
    if c == list(word):
        print("This is a palindrome!!!")
palindromechecker(input("This is a Palindrome checker! Type a word: "))


def palindromechecker2():
    word = input("Palindrome check: ")

    print(word)
    print(word[0:])
    print(word[::-1])


    if word[0:] == word[::-1]:
        print("Success! " + word + " is a Palindrome")
    else:
        print("no dice")

palindromechecker2()
