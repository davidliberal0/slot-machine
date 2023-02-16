# Global constants
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

# function to collect the deposit as user input
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


# function to collect the lines to bet on as user input
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        # validate user input - make sure it is a number
        if lines.isdigit():
            lines = int(lines) # convert the user input to an integer
            # check if lines is within range of MAX_LINES
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number!")
    return lines

def get_bet():
    while True:
        wager = input("What would like to bet? $")
        # validate user input - make sure it is a number
        if wager.isdigit():
            wager = int(wager) # convert the user input to an integer
            # check if wager falls within the range of min and max bet
            if MIN_BET <= wager <= MAX_BET:
                break
            else:
                print(f"Wager must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number!")
    return wager




def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    # calculate the total bet
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    print(balance, lines)


main()