if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique = []
    for i in arr:
        if i not in unique:
            unique.append(i)
        else:
            pass
    
    unique.sort()
    print(unique[-2])