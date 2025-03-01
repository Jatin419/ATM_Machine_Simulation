import getpass  # Importing getpass module to securely input PIN without displaying it

# Initializing ATM variables
pin = "4521"  # Default PIN
balance = 0 # Initial account balance
transaction_history = []  # List to store transaction history

print("Welcome to the ATM machine!!!")
attempts = 3  # Maximum number of attempts allowed for PIN entry

# PIN Authentication Loop
while attempts > 0:
    entered_pin = getpass.getpass("Enter your PIN: ")  # Secure PIN input
    if entered_pin == pin:
        print("Access granted.")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. {attempts} attempts remaining.")
else:
    print("Too many incorrect attempts. Exiting.")
    exit()  # Exiting the program after 3 incorrect attempts

# Main ATM Menu Loop
while True:
    print("\n ATM menu: ")
    print("1. Balance Inquiry ")
    print("2. Cash Withdrawal ")
    print("3. Cash Deposit ")
    print("4. Change Pin ")
    print("5. View Transaction History ")
    print("6. Exit")
    
    # Taking user input for ATM options
    choice = input("Enter your choice: ")  
    
    if choice == "1":  # Balance Inquiry
        print(f"Your current balance is: ₹{balance}")  
        transaction_history.append("Balance Enquiry")  # Logging transaction
        print("=================================================================")
    elif choice == "2":  # Cash Withdrawal
        amount = float(input("Enter the amount to withdraw: ₹"))
        if amount > balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount. Enter a valid amount.")
        else:
            balance -= amount
            print(f"Withdrawal Successful. ₹{amount} has been debited.")
            transaction_history.append(f"Cash Withdrawal: ₹{amount}")
        print("=================================================================")
            

    elif choice == "3":  # Cash Deposit
        amount = float(input("Enter amount to deposit: ₹"))                      
        if amount <= 0:
            print("Invalid amount. Enter a valid amount.")
        else:
            balance += amount
            print(f"Deposit successful. ₹{amount} has been added to your account and Current balance is ₹{balance}")
            transaction_history.append(f"Cash Deposit: ₹{amount}")
        print("==========================================================================================")
            
            
    elif choice == "4":  # Change PIN
        old_pin = getpass.getpass("Enter old PIN: ")
        if old_pin == pin:
            pin = getpass.getpass("Enter new PIN: ")
            print("PIN changed successfully.")
            transaction_history.append("PIN changed")
        else:
            print("Incorrect old PIN. PIN change failed.")
        print("=================================================================")
            
            
    elif choice == "5":  # View Transaction History
        if not transaction_history:
            print("No transactions found.")
        else:
            print("Transaction History:")
            for transaction in transaction_history:
                print(f"- {transaction}")
        print("=================================================================")
                
                
    elif choice == "6":  # Exit ATM
        print("Thank you for using our ATM service.")
        break  # Exiting the ATM loop
    
    else:
        print("Invalid choice. Select a valid option.")  # Handling invalid menu choices
