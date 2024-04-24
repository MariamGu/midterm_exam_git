def validate_account(account_number, accounts):
    if account_number in accounts:
        return True
    else:
        return False


def transfer_funds(from_acc, to_acc, amount, accounts):
    if not validate_account(to_acc, accounts):
        print("Account number does not exist. Please try again. ")
        return False
    if accounts[from_acc]['balance'] < amount:
        print("Insufficient balance. ")
        return False
    else:
        accounts[from_acc]['balance'] -= amount
        accounts[to_acc]['balance'] += amount
        print(f"You have successfully transfered {amount} GEL to {accounts[to_acc]['name']}. ")


def initiate_transfer(accounts):
    from_account = input("Provide account to transfer money from: ")
    if validate_account(from_account, accounts):
        to_account = input("Enter the account number where you want to transfer: ")
        amount = float(input("Enter the amount you want to transfer: "))

        if transfer_funds(from_account, to_account, amount, accounts):
            print(f"New balance for {accounts[from_account][to_account]['name']}: {accounts[from_account]['balance']} GEL ")

    print("The account you are trying to transfer money from does not exits!")

