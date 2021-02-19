# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english_set = set(list(map(int,input().split(" "))))
m = int(input())
french_set = set(list(map(int,input().split(" "))))

print(len(english_set.intersection(french_set)))