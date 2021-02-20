def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        hex_ = str(hex(i)[2:]).upper()
        binary = str(bin(i)[2:])
        print(decimal,end=" ")
        print(octal,end=" ")
        print(hex_,end=" ")
        print(binary)
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)