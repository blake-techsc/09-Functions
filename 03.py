def get_user_in_withing_range_default_params(min=1, max=100):
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

userin = 0
while userin != 5:
    # userin = get_user_in_withing_range_default_params(50)
    userin = get_user_in_withing_range_default_params(max=50)