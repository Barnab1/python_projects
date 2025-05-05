#The main file of the Basic Calculator App

def addition(numbers):
    return sum(numbers)

substract = lambda num1, num2 : num1 - num2
multiplication = lambda num1, num2: num1 * num2 
 
def division(num1, num2):
    if num2 == 0:
        print('Division by 0 leads to Infinity')
        return
    return num1/num2

def main():
    
    print('Welcome to the Basic Calculator App. Here are the current functions.')

    functions = ['addition', 'soustraction', 'multiplication','division']
    for index, item in enumerate(functions):
        print(f'{index+1}- {item}')
        
main()