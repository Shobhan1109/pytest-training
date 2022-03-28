def recA(x, y):
    return x*y
def recP(x, y):
    return 2*(x+y)
def square(x):
    return x*x
if __name__=="__main__":
    print("1.Area of the rectangle.")
    print("2.Perimeter of the rectangle.")
    print("3.Area of the square.")
    print("4.Exit.")
    c=int(input("Choose the option:"))

    if c == 1:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        print("Area of the rectangle:", recA(num1,num2))
    elif c == 2:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        print("Perimeter of rectangle:", recP(num1,num2))
    elif c == 3:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        print("Area of sqaure is:", square(num1))
    else:
        print("Exit")
        exit(4)
