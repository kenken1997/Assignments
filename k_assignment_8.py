def authenticate_user(sys_pin):
    while True:
        user_pin = input('Enter your pin to begin: ')

        if user_pin != sys_pin:
            print('Invalid pin. Try again')
        else:
            print('Login successful. \n')
            return 
        
def get_valid_int(prompt, error_message="Invalid input. Enter a numeric value.\n"):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(error_message)
    
def check_balance(balance, transactions):
    print(f'Your balance is {balance} cedis. \n')
    transactions.append(f"Checked balance: {balance} cedis")
    return balance

def deposit_money(balance, transactions):
    
    deposit = get_valid_int('Enter amount to deposit: ')

    if deposit <= 0:
        print('Please enter a higher amount. Deposit value too low')
        return balance
    balance += deposit
    print(f'Deposit of {deposit} cedis successful.')
    print(f'Your new balance is {balance} cedis. \n')
    transactions.append(f"Deposited: {deposit} cedis, New balance: {balance} cedis")
    return balance

def withdraw_money(balance, transactions):
    while True:
        withdraw = get_valid_int('Enter amount to withdraw: ')
        if withdraw > balance:
            print('Action cannot be performed. Not enough balance')
        elif withdraw <= 0:
            print(f'Cannot withdraw {withdraw} cedis. Invalid input')
        elif withdraw <= balance:
            balance -= withdraw
            print(f'Withdrawal of {withdraw} cedis succesful')
            print(f'Amount of {withdraw} cedis has been deducted from your account. New balance is {balance} cedis. \n')
            transactions.append(f"Withdrew: {withdraw} cedis, New balance: {balance} cedis")
            return balance
        
def transaction_history(transactions):
    if not transactions:
        print("No transactions have been made yet.\n")
        return

    print("\n=== Transaction History ===")
    for transaction in transactions:
        print(transaction)
    print("===========================\n")



def main():

    sys_pin = '1234'
    balance = 1000
    transactions = []

    authenticate_user(sys_pin)

    while True:
        
    
        print('''Enter preferred action:
1. Check balance
2. Deposit money
3. Withdraw money 
4. View transaction history
5. Exit the system
''')
    
        choice = input('Choose (1-5): ').strip()

        if choice == '1':
            balance = check_balance(balance, transactions)
        elif choice == '2':
            balance = deposit_money(balance, transactions)
        elif choice == '3':
            balance = withdraw_money(balance, transactions)
        elif choice == '4':
            transaction_history(transactions)
        elif choice == '5':
            print('Exiting program. \n')
            break
        else:
            print('Invalid input. Enter (1-5). \n')
    


if __name__ == '__main__':
    main()

    
    
    


