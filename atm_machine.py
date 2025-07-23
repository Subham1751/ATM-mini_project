print("\nHello User!! Welcome to the ATM!!\n")
initial_balance = 100000
pin = 1751
attempt = 0

while attempt < 3:
    entered_pin = int(input("Please Enter Your 4-Digit PIN : "))
    if entered_pin == pin :
        print("PIN Verified.Access Granted\n")

        while True:
            print("\n______ATM MENU_____\n")
            print("1. CHECK BALANCE")
            print("2. WITHDRAW MONEY")
            print("3. DEPOSIT MONEY")
            print("4. EXIT \n")

            entered_choice = int(input("Please Enter Your Choice : "))
            if entered_choice == 1:
                print("Your Balance is",initial_balance)

            elif entered_choice == 2:
                withdraw_amount = int(input("Enter Amount : "))
                if withdraw_amount > initial_balance:
                    print("Insuffecient Balance")

                elif withdraw_amount <= 0:
                    print("Invalid Amount")
            
                else:
                    initial_balance -= withdraw_amount
                    print("Amount Withdrawn. Your New Balance is :", initial_balance)

            elif entered_choice == 3:
                deposit_money = int(input("Enter Amount To Deposit : "))
                if deposit_money <= 0:
                    print("Invalid Amount.Please Enter Valid Amount")
                else:
                    initial_balance += deposit_money
                    print("Amount Deposited. Your New Balance is :", initial_balance)

            elif entered_choice == 4:
                print("Thankyou For Using the ATM. VISIT AGAIN!!")
                break
            else:
                print("INVALID CHOICE. TRY AGAIN.")
            break
    else:
        print("\nINCORECT PIN. PLEASE TRY AGAIN LATER.\n")

    attempt += 1

    if attempt == 3:
        print('''\nToo many incorrect PINs. Your Account is Locked for 24 hours.
          Please Visit Again after 24 Hours \n''')
    

