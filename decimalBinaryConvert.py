binary = []
num = int(input("Enter a number to convert: "))
base = int(input("Enter a base number system: "))
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
print("")

def getInput():
    newbase2 = int(input("Enter a base: "))
    deci = input("Enter another number (to convert to base 10): ")
    return newbase2, deci

def numToBaseTen(deci, newbase2):
    deciList = [int(d) for d in deci]
    deciList.reverse()
    total = 0
    for power, digit in enumerate(deciList):
        total += digit * (newbase2 ** power)
    print(f"Total: {total}")

newbase2, deci = getInput()
numToBaseTen(deci, newbase2)