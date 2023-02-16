
# collects the deposit as user input
def deposit():
    while True:
        amount = input("What would like to deposit? $")
        # validate user input - make sure it is a number
        if amount.isdigit():
            amount = int(amount) # convert the user input to an integer
            # check if amount is greater than 0
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0 (zero).")
        else:
            print("Please enter a number!")
    return amount


deposit()