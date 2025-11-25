def greet(fx):
    def mfx(*args, **kwargs):
        print ("Good Morning")
        fx(*args, **kwargs)
        print ("Thank You for using this function")
    return mfx

@greet
def add(x, y):
    z = x + y
    print ("The sum is:", z)

add(4, 5)
#print ("Hello World!")