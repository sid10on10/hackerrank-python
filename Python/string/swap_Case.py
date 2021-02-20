def swap_case(s):
    string = ""
    for each_char in s:
        if isinstance(each_char,str):
            if each_char.isupper():
                string += each_char.lower()
            else:
                string += each_char.upper()
        else:
            pass
                
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)