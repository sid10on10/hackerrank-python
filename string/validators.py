if __name__ == '__main__':
    s = input()
    char = list(s)
    result = any([c.isalnum() for c in char])
    print(result)
    result = any([c.isalpha() for c in char])
    print(result)
    result = any([c.isdigit() for c in char])
    print(result)
    result = any([c.islower() for c in char])
    print(result)
    result = any([c.isupper() for c in char])
    print(result)