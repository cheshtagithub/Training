'''            ​ Encapsulation example:
Made a class payment with account and balance as private:'''

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} is added in the account.")
        else:
            print("Invalid ammount to deposit in account.")
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} is withdrawn from account.")
            
        else:
            print("Insufficient balance in account.")
            
    def get_balance(self):
        return self.__balance


def process_withdrawal(account, amount):
    account.withdraw(amount)


account_number = input("Enter account number: ")
balance = int(input("Enter the balance of account: "))
amount = int(input("Enter the amount to withdraw: "))

s = BankAccount(account_number, balance)

process_withdrawal(s, amount)

print("Remaining Balance: ₹",s.get_balance())

'''
Output:
Enter account number: 554433
Enter the balance of account: 555555
Enter the amount to withdraw: 444444
₹444444 is withdrawn from account.
Remaining Balance: ₹ 111111
'''
