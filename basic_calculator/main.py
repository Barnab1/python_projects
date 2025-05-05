#The main file of the Basic Calculator App

def addition(num1, num2):
    return sum(num1, num2)

substract = lambda num1, num2 : num1 - num2
multiplication = lambda num1, num2: num1 * num2 
 
def division(num1, num2):
    if num2 == 0:
        print('Division by 0 leads to Infinity')
        return
    return num1/num2

def introduceFunction():
    pass

def main():
    
    print('Welcome to the Basic Calculator App. Here are the current functions.')

    functions = ['addition', 'soustraction', 'multiplication','division']
    for index, item in enumerate(functions):
        print(f'{index+1}- {item}')
    userChoice = input('Choose a number from the menu: ')

    try:
        userChoice = int(userChoice)

        if userChoice > len(functions):

            print('Your choice is out of range')
        else:
            introduceFunction()
    except ValueError:
        print('Give only number')  
main()