binary = []

def numToBin():
    num = int(input("Enter the number you want to convert: "))
    base = int(input("Binary base: "))
    rem_num = num
    while not rem_num == 1:
        rem_num = num // 2
        binary.append(num%2)
        num = rem_num
    binary.append(1)
    binary.reverse()
    print(f"Number in binary: {binary}")

while True:
    numToBin()