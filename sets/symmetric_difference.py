# Enter your code here. Read input from STDIN. Print output to STDOUT

m = input()
m_set = set(list(map(int,input().split(" "))))
n = input()
n_set = set(list(map(int,input().split(" "))))

arr_m = list(m_set.difference(n_set))
arr_n = list(n_set.difference(m_set))

arr_m.extend(arr_n)
outarr = sorted(arr_m)

for each in outarr:
    print(each)