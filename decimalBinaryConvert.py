binary = []
num = int(input("Enter the number you want to convert: "))
base = int(input("Enter the base number system you want: "))
deci = 0.0
newbase2 = ""

def numToNewNumSystem(num, newbase):
    rem_num = num
    while rem_num != 0:
        rem_num = num // newbase
        binary.append(str(num%newbase))
        num = rem_num
    #binary.append("1")
    binary.reverse()
    return "".join(binary)

# write a function that takes a number and a base and converts it to base10

print(numToNewNumSystem(num, base))

def numToBaseTen(deci, newbase2):
    deciList = [int(num)for num in deci]
    deciList.reverse()
    total = 0
    for power,digit in enumerate(deciList):
        value = digit * (newbase2 ** power)
        total += value
    print(f"Total: {total}")
def getInput():
    newbase2 = int(input("Enter a base: "))
    deci = input("Enter a deci: ")
    return newbase2,deci

numToBaseTen(deci, newbase2)