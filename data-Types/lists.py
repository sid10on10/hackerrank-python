if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(0,N):
        command_arr = list(input().split(" "))
        command = command_arr[0]
        if command == "insert":
            index = int(command_arr[1])
            data = int(command_arr[2])
            arr.insert(index,data)
        elif command == "print":
            print(arr)
        elif command == "remove":
            to_remove = int(command_arr[1])
            arr.remove(to_remove)
        elif command == "append":
            to_append = int(command_arr[1])
            arr.append(to_append)
        elif command == "sort":
            arr.sort()
        elif command == "pop":
            arr.pop()
        elif command == "reverse":
            arr.reverse()
        else:
            pass
            
        
        
