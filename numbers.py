from OperationManager import OperationManager
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
    print('divide two number')
    num1 = int(input('Enter 1st number:  ')) #This line of code will take the first number
    num2 = int(input('Enter 2nd number:  ')) #Thisline of coed will take the second number
    ans = num1/num2
    print("The answer is " +str(ans))
    return ans

def multiply():
    print('multiply two number')
    num1 = int(input('Enter 1st number:  ')) #This line of code will take the first number
    num2 = int(input('Enter 2nd number:  ')) #This line of code will take the second number
    ans = num1*num2
    print("The answer is "  +str(ans))
    return ans

def mod():
    print('modular quotient')
    num1 = int(input('Enter 1st number:  '))
    num2 = int(input('Enter 2nd number:  '))
    ans = num1%num2
    print("The answer is "   +str(ans))
    return
manager = OperationManager()
while(True):
    print('Option 1 - add two numbers')
    print('Option 2 - sub two numbers')
    print('Option 3 - divide two numbers')
    print('Option 4 - multiply two numbers')
    print('Option 5 - modular quotient')
    print('Option 6 - exit')
    option = int(input('Pick an option 1 - 6: '))
    if option == 1:
        add()
    elif option == 2:
        sub()
    elif option == 3:
        divide()
    elif option == 4:
        multiply()
    elif option == 5:
        mod()
    elif option == 6:
        exit()
    else:
        print('Invalid input')
