# Global constants
MAX_LINES = 3

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


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()