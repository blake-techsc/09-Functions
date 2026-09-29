# functions that RETURN things
purchases = [2.99, 5.99, 7.99]

def calculate_total(prices, tax): # price will be a list of float, tax will be float
    """
    <h1> Will this work? </h1>
    <h2> It works! </h2>
    This is a super awesome function that returns your total. Oh hi Mark."""
    total = sum(prices)
    total = total + (total * tax)
    return total # notice the RETURN statement

my_total = calculate_total(purchases, 0.06)
print(f"{my_total:.2f}")


def get_user_in_within_range(min:int ,max:int) -> int:
    """Promts the user to enter a value between *min* and *max* (exclusive)
    Validates the input. Converts it to an int and returns it.
    eg. if *min* is 1 and *max* is 100, any number 1-99 is valid
    """
    while True:
        t = input(f"Enter a number between{min} and {max}: ")
        if t.isdigit():
            if int(t) >= min and int(t) < max:
                print("Good job.")
                break
        print("Invalid, Try again.")
    return int(t)

myNum = get_user_in_within_range(1, 100)

while True:
    num = get_user_in_within_range(1, 100)
    if num == 5:
        break