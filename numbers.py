
def add():
    print('Add two numbers')
    num1 = int(input('Enter 1st number: ')) #input takes keyboard input
    num2 = int(input('Enter 2nd number: '))
    ans = num1+num2
    print("The answer is " + str(ans))
    return ans

def sub():
    print('subtract two numbers')
    num1 = int(input('Enter 1st number:  ')) #this part is taking in the first number
    num2 = int(input('Enter 2nd number:  ')) #second input here for the second number
    ans = num1-num2
    print("The answer is " +str(ans))
    return ans


def divide():
    return
def multiply():
    return
def mod():
    return

while(True):
    print('Option 1 - add two numbers')
    print('Option 2 - sub two numbers')
    print('Option 3 - exit')
    option = int(input('Pick an option 1 - 3: '))
    if option == 1:
        add()
    elif option == 2:
        sub()
    elif option == 3:
        exit()
    else:
        print('Invalid input')
