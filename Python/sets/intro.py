def average(array):
    distinct = set(array)
    average = sum(distinct)/len(distinct)
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)