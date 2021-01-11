def split_and_join(line):
    # write your code here
    words = line.split(" ")
    string = "-".join(words)
    return string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)