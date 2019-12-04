# print("Hello World")


def print_something(name="Sanjog", age=20):
    print("my name is ", name, "and my age is ", age)


# print_something()

def print_inf(*people):
    for person in people:
        print("Person is ", person)


# print_inf("John", "Smith", "Rog")

def do_math(num1, num2):
    return num1 + num2


math1 = do_math(2, 7)
math2 = do_math(3, 19)

# print("Math 1 is ",math1,"Math 2 is ",math2)

check = True


def if_else():
    if check == False:
        print("False")
    else:
        print("True")


# if_else()

numbers = [1, 2, 3, 4, 5]


def for_loop():
    for num in numbers:
        print("number is ", num)


# for_loop()

def while_loop():
    curr = 0
    run = True
    while run:
        if curr == 50:
            run = False
        else:
            print(curr)
            curr += 1

while_loop()