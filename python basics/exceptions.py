# using exceptions
def test(a):
    print(a)
    print(a)
    print(a)
try:
    userinput = int(input("Enter the number you want to triple: "))
    test(userinput)
except Exception as h:
    print("you have to enter a number please" ":", h)
finally:
    print("this final message must be printed anyway")