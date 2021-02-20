# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
m_set = set(list(map(int,input().split(" "))))
n = int(input())
n_set = set(list(map(int,input().split(" "))))

count = len(list(m_set.symmetric_difference(n_set)))
print(count)
