n = int(input())
s = set(map(int, input().split(" ")))
n_c = int(input())


for _ in range(0,n_c):
    command = input().split(" ")
    #print(command)
    if len(command) == 1:
        s.pop()
    else:
        if command[0] == "remove":
            s.remove(int(command[1]))
        else:
            s.discard(int(command[1]))
            
print(sum(s))