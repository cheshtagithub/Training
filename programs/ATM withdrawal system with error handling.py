 #           ​ ATM withdrawal system with error handling:
class InsufficientBalanceError(Exception):
    pass

try:
    balance = int(input("Enter the balance present in the account: ₹"))
    if balance < 0:
        print("Sorry but you do not have any money to withdraw.")
    amount = int(input("Enter the amount to withdraw: ₹"))
    
    if amount > balance:
        raise InsufficientBalanceError("Withdrawal not possible")
        
    if amount < 0 :
        raise ValueError("Withdrawal not possible")
    
    print("The balance left in account is: ₹",balance - amount)
except ValueError as e:
    print(e,",Please input valid numbers.")
    
except InsufficientBalanceError as e:
    print(e,",Withdrawal amount is higher than balance of the account.")
    
finally:
    print("Transaction is completed.")

"""
Output:
Without error
Enter the balance present in the account: ₹5000
Enter the amount to withdraw: ₹3000
The balance left in account is: ₹ 2000
Transaction is completed.
With Value error:
Enter the balance present in the account: ₹600
Enter the amount to withdraw: ₹-55
Withdrawal not possible ,Please input valid numbers.
Transaction is completed.

With Insufficient balance error:
Enter the balance present in the account: ₹6000
Enter the amount to withdraw: ₹9000
Withdrawal not possible ,Withdrawal amount is higher than balance of the account.
Transaction is completed.
"""
