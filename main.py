MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

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
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
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

def main():
    balance = deposit()
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
main()

