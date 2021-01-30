# Enter your code here. Read input from STDIN. Print output to STDOUT

countenglish = input()
english_roll = list(map(int,input().split(" ")))
english_set = set(english_roll)
countfrench = input()
french_roll = list(map(int,input().split(" ")))
french_set = set(french_roll)
only_english = english_set.difference(french_set)
print(len(only_english))
