import random, sys

#Number guessing game: let user guess a number randomly made

#first : guess a random number
# Telling the user the number range or hardcoding it



def random_except(start,end, exclude):
    while True:
        num = random.randint(start, end)
        if num != exclude:
            return num
def congratulation(tries):
    print(f"Congratulation. You find it after {tries} {'tries' if tries > 1 else 'trie'}")

def giveHint(secretNumber, userNumber):
    #check if userNumber is halfway of secretNumber
    if secretNumber > userNumber: 
        print('too low')
    else:
        print('too high')

    distance = secretNumber - userNumber
    if distance > 10:
        print(f'Secret Number is {distance/2} away of your number')


def main():
    limit = 100
    userScore = 0
    tries = 0
    print(f"Hi dear, we you are going to guess a number between 0 and {limit}")
    secretNumber = random_except(0,limit,5)

    print('The number is generated, now guess it. Let\'s go')

    keepGoing = True

    while keepGoing:
        userInput = int(input('Guess the number or type 5 to exit : '))

        if userInput == secretNumber :
            congratulation(tries)
            keepGoing = False
            break
        elif userInput == 5:
            print('Good bye')
            sys.exit() 
        else:
            print("Sorry")
            tries +=1
            giveHint(secretNumber, userInput)
            continue


#ask user to enter the number until there are anymore  ok

# congratulate user if there are succcesful

main()