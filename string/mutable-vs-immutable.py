def mutate_string(string, position, character):
    str_arr = list(string)
    str_arr[position] = character
    result = "".join(str_arr)
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)