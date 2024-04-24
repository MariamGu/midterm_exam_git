accounts = {
    "TB001": {"name": "Mariam", "balance": 100},
    "TB021": {"name": "Someone", "balance": 50}
}


def validate_account(account_number):
    return account_number in accounts


def add_funds(account_number, amount):
    if validate_account(account_number):
        if isinstance(amount, (int, float)) and amount > 0:
            accounts[account_number]['balance'] += amount
            print(f"Balance was filled with {amount} GEL. New balance: {accounts[account_number]['balance']} GEL")
            return True
        else:
            print("Invalid amount entered. Please enter a positive number.")
    else:
        print("Account number does not exist.")
    return False


def initiate_add_funds():
    account_number = input("Enter the account number to add funds: ")
    try:
        amount = float(input("Enter the amount to add: "))
        add_funds(account_number, amount)
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount. ")
