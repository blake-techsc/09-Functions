# a function is a block of reusable code that performs a specific task
# ANY TIME CODE IS REPEATED - rewrite it into a function
# why? easier to read and maintain - less errors

def fun_class():
    print("This class is fun")
    print("This class is fun because ... well there's gotta be a reason")
    print("This class is fun")

fun_class()

def something(person):
    print(f"{person} is cool")
    print(f"{person} is cool because ... well there's gotta be a reason")
    print(f"{person} is cool")

something("Isaac")
something("Charlie")
something("Alan")

def someone_is(person, mood):
    print(f"{person} is {mood}")
    print(f"{person} is {mood} because ... well there's gotta be a reason")
    print(f"{person} is {mood}")

someone_is("This dude", "evil")
someone_is("Pablo", "happy")