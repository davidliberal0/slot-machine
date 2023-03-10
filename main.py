#imports
import random

# Global constants
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# important -------------------------
# Difference between row and column
# ROW -------
# Column |||||||||



# function for slot machine outcome
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # append a number of symbols into the list based on their values
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        # makle a copy of the symbols list
        current_symbols = all_symbols[:]
        # loop through the number of values needed to generate
        # which is equal to the number of rows in the slot machine
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# function for displaying the slot machine
def print_slot_machine(columns):
    # transpose the matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end= "")
        print()


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


# function for collecting the betting wager as user input
def get_bet():
    while True:
        wager = input("What would like to bet on each line? $")
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
    while True:
        bet = get_bet()
        # calculate the total bet
        total_bet = bet * lines
        # check if user has enough funds to make the bet
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. You current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()