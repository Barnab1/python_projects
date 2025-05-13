#The main file of the Basic Calculator App
import sys
def addition(num1, num2):
    return sum(num1, num2)

substract = lambda num1, num2 : num1 - num2
multiplication = lambda num1, num2: num1 * num2 
 
def division(num1, num2):
    if num2 == 0:
        print('Division by 0 leads to Infinity')
        return
    return num1/num2


def checkTwoNumbers(num1, num2):
    if isinstance(num1, int) & isinstance(num2,int): 
        return True
    else: 
        return False

def introduceFunction(name):
    if name == "exit":
        print('Good bye dear')
        sys.exit()  
    print(f"Fine, here we will make {name}. But first give two numbers")

    number1 = int(input("First number: "))
    number2 = int(input("Second number: "))
    isValid = checkTwoNumbers(number1, number2)
    if isValid:
        if name == "addition":
            result = addition(number1, number2)
        elif name =="soustraction":
            result = substract(number1,number2)
        elif name == "multiplication":
            result = multiplication(number1, number2)
        elif name == "division":
            result= division(number1, number2)
        print(f"The result is {result}")
    else:
        print('Come back and give only integers')

def main():
    
    print('Welcome to the Basic Calculator App. Here are the current functions.')

    functions = ['addition', 'soustraction', 'multiplication','division','exit']

    for index, item in enumerate(functions):
        print(f'{index+1}- {item}')
        valid = True

    while valid:
        userChoice = input('Choose a number from the menu: ')

        try:
            userChoice = int(userChoice)
        except ValueError:
            valid = False
            print('Give only number')
            
            
        if userChoice > len(functions):
            print('Your choice is out of range')
        else:
            introduceFunction(functions[userChoice-1])
main()