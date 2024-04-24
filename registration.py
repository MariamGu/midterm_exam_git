database = {}


def validate_account_number(account_number):
    if len(account_number) == 5 and account_number.startswith('TB') and account_number[2:].isdigit():
        return True
    return False


def register_user(accounts):
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    account_number = input("Enter your account number (Format 'TB' followed by three numbers): ")
    user_info = {f'{account_number}': {'name': f'{first_name}', 'balance': 50}}
    accounts.update(user_info)

    if validate_account_number(account_number):
        if account_number not in database:
            database[account_number] = {'First Name': first_name, 'Last Name': last_name}
            print("You have registered successfully.")
        else:
            print("This account number is already registered. ")
    else:
        print("Invalid account number format. Please try again with format 'TB' followed by three numbers). ")
