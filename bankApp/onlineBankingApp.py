import math
print("Welcome to the online banking Application")

def signin():
    global name #username
    global pin #password
    global cb # current balance
    name = str(input("Please create your username :"))
    pin = str(input("Please create your 6 digits pin :"))
    if len(pin) == 6:
        pin = pin
    else:
        print("The pin has to be in 6 digits")
        newpin = str(input("Please create your 6 digits pin :"))
        if len(newpin) != 6:
          print("The pin has to be in 6 digits")
          signin()  
        else:
            pin = newpin
    print("Thanks for creating your bank account")

def forgetpin():
    recoverpin = str(input("Please create your new 6 digits :"))
    if len(recoverpin) != 6:
        print("The pin has to be in 6 digits ")
        forgetpin()
    else:
        print("The new pin has been stored. Please login")
        pin = recoverpin
        login()
def depositInterest(p,r,t):
    # A = Pe^(rt) which is the formula 
    #to calculate compound interest

    p = float(p) #principal capital
    r = float(r) # rate or taux
    t = float(t) # time
    rt = r * t
    e = math.exp(rt)
    #Calculation
    a = p * e #return the value of your investment
    return a
def login():
    # name1 represent username 
    # pin1 represent user's pin
    name1 = str(input("Please enter your username: "))
    pin1 = str(input("Please enter your pin : "))

    #check if the name and pin match the ones stored

    if name1 == name and pin1 == pin:
        print("Welcome to the online banking Application" + " " + name)
        print("Please choose the menu down here")

        listMenu = {"1- Deposit","2-withdraw", "3-Transfer", "4-Check Balance", 
                    "5-Deposit interest rate", "6-calculate compound interest"}
        for b in listMenu:
            print(b)
        choose = int(input("Please enter number of your choice "))
        d = 0 #represent deposit
        w = 0 #represent withdraw
        cb = 0 #represents current balance

        if choose == 1:
            d = int(input("Enter the amount of your deposit "))
            cb += d
            print("Your current balance is" + " " + str(cb))

        elif choose == 2:
            w = int(input("Enter the amount of money you want to withdraw "))
            if w > cb:
                print("Your current balance is not sufficient for this transaction")
                login()
            else:
                cb -= w
                print(str(w) + "has been withdrawn from your account." + " " + "Your current balance is " + str(cb))
        elif choose ==3:
            dest = str(input("Please enter the account number of your destination in 8 digits "))
            if len(dest)== 8:
                amount= int(input("Please enter the amount of money you want to transfer  "))
                if amount > cb:
                    print("Your current balance is not sufficient")
                    login()
                else:
                    cb -= amount
                    print("The transaction of " + " " + str(amount) + " has been transferred to " + str(dest))
                    print("Your current balance is " + " "+ str(cb))

            else:
                print("The transaction has been rejected. The destinatiion account number is invalid")
        elif choose == 4:
                print("Your current balance is " + " " + str(cb))
        elif choose == 5:
            if d > 50000:
                rate = 3
            elif d > 30000:
                rate =2
            else:
                rate = 1.5
            print("Your current deposit interest rate is " + " " + str(rate) + "%")
        elif choose == 6:
            listOption = ["1-Calculate your deposit compound interest based on your cb", "2-Calculate your deposit compound interest based on your deposit input"]
            for n in listOption:
                print(n)
            choice = int(input("Please enter your choice from the options above "))
            if choice == 1:
                timing = str(input("How many years you want to invest your money "))
                if d > 50000:
                    rate = 3/100
                elif d > 30000:
                    rate = 2/100
                else:
                    rate= 1.5/100
                print("Your current balance in "+ " " + timing + " will be ")
                print(depositInterest(cb, rate, timing))
            elif choice ==2:
                timing = str(input("How many years you want to invest your money : "))
                money = str(input("Please enter the amout of money you would like to deposit ? "))
                money = int(money)
                if d > 50000:
                    rate = 3/100
                elif d > 30000:
                    rate = 2/100
                else:
                    rate= 1.5/100
                print("Your current balance in "+ " " + timing + " will be ")
                print(depositInterest(money, rate, timing))
            else:
                print("Option is not available, back to main account")
                login()
        exit()
    else:
        print("Either of your username or pin is wrong, did you create your account ? ")
        list1 = {"1-yes", "2-no"}
        for i in list1:
            print(i)
        inp = int(input("Enter your choice below: "))
        if inp == 1:
            list2 = {"1- Do you want to login again", "2-you forget your password"}
            for i in list2:
                print(i)
                theanswer = str(input("Please enter your choice "))
                theanswer = int(theanswer)
                if theanswer == 1:
                    login()
                elif theanswer == 2:
                    forgetpin()
                    login()
                else:
                    print("Option is not available")
                    login()
        elif inp == 2:
            print("Please create your account  ")
            signin()
    
def mainMenu():
    options = int(input("Choose 1 to sign in and choose 2 to login "))
    if options == 1:
        signin()
    elif options == 2:
        login()
    else:
        print("Option is not available")
        mainMenu()
    exit()

def exit():
    answer = str(input(" Do you still want to conduct transactions ? Yes or No "))
    if answer == "Yes":
        login()
    elif answer == "No":
     print("Thank you for using this app")

    else:
      print("Option is not available")
      mainMenu()     


mainMenu()