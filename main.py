import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbol):
    all_symbols = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        # Copy of list(NOT REFERENCE) [:]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        # Empty print() creates space so the next column prints on new line
        print()


def deposit():
    while True:
        # Ask user amount to deposit
        amount = input("What would you like to deposit? $")
        # Checks user's input to see if digit
        if amount.isdigit():
            amount = int(amount)
            # User deposit > 0, deposit successful, break out of while loop
            if amount > 0:
                break
            # If user input < 0
            else:
                print("Amount must be greater than 0.")
        # If user input is not a number
        else:
            print("Please enter a valid number.")
    return amount


def get_number_of_lines():
    while True:
        # Ask user amount of lines to bet on
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        # Checks user's input to see if digit
        if lines.isdigit():
            lines = int(lines)
            # User input lies on or between min & max lines
            if 1 <= lines <= MAX_LINES:
                break
            # If user input < 0
            else:
                print("Enter a valid number of lines.")
        # If user input is not a number
        else:
            print("Please enter a valid number.")
    return lines


def get_bet():
    while True:
        # Ask user amount to bet
        amount = input("What would you like to bet? $")
        # Checks user's input to see if digit
        if amount.isdigit():
            amount = int(amount)
            # Checks if user's bet is between min & max
            if MIN_BET <= amount <= MAX_BET:
                break
            # If user input < 0
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        # If user input is not a number
        else:
            print("Please enter a valid number.")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}"
            )
        else:
            break
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}"
    )
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    # * splat operator unpacks variable
    print(f"You won on:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        res = input("Press enter to play (q to quit).")
        if res == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}.")


main()
