# input: word
#output: yes/no palindrome
#problem: check palindrome
#solution: Break down problems into smaller part
#1st part: convert into lowercase
#2ndpart: slice to  get reverse of the word
#3rdpart: use condtion  compare both step(1-2)


def check_palindrome(word):
    #using variable to convert into lowercase
    word_case = word.lower()
    # using varible to hold slicing into reversing
    reversed = word[::-1]
    # check reverse is same as original
    if word_case == reversed:
        return "Yes"
    return "No"    

# word = input(("enter woed to check palindrome: "))

words = ["radar", "Level", "madam", "civic", "noon", "Apple", "python", "flower", "Window", "chAir"]

# print(f"{word} is: ",check_palindrome(word)) 

i=0
while i<len(words):
    print(f"{words[i]} is palindrome? ",check_palindrome(words[i]))
    i+=1

print(words[0])
# for i in words:
#     print(f"{i} is :",check_palindrome(i))
    