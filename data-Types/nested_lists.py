if __name__ == '__main__':
    data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name,score])
        
    #print(data)
    scores = []
    for each_data in data:
        if each_data[1] not in scores:
            scores.append(each_data[1])
    
    scores.sort()
    second_lowest = scores[1]
    #print(second_lowest)
    
    names = []
    def name(arr):
        return arr[1] == second_lowest
        
    arr = list(filter(name,data))
    for each in arr:
        names.append(each[0])
        
    names.sort()
    for each in names:
        print(each)