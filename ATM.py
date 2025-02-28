def atm_withdrawal():
    try:
        balance = float(input("Enter your current bank balance: ₹"))
        withdrawal_amount = float(input("Enter the withdrawal amount: ₹"))
        
        # Check if the withdrawal amount is greater than 0
        if withdrawal_amount <= 0:
            print("Error: The withdrawal amount must be greater than ₹0.")
            return
        
        # Check if the withdrawal amount is in multiples of ₹100
        if withdrawal_amount % 100 != 0:
            print("Error: The withdrawal amount must be in multiples of ₹100.")
            return
        
        # Check if the withdrawal amount exceeds the available balance
        if withdrawal_amount > balance:
            print("Error: Insufficient balance.")
            return
        
        # Deduct the amount and display the remaining balance
        balance -= withdrawal_amount
        print(f"Transaction successful! Your remaining balance is ₹{balance:.2f}")
    
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")

# Run the ATM withdrawal function
atm_withdrawal()