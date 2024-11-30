def add(a,b):
    answer = a +b 
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a,b):
    answer = a -b
    print (str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def multi(a,b):
    answer = a * b
    print (str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def divi(a,b):
    answer = a / b
    print (str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    print("A. addition")
    print("B. subtraction")
    print("C. multiplication")
    print("D. division")
    print("E. exit")

    choice = input("Input choice: ")


    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        multi(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        divi(a, b)
    elif choice == "e" or choice == "E":
        print("Exit")
        quit()