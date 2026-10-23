class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # public attribute
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

account = BankAccount("123456", 1000)
account.deposit(500)  # Deposited 500. New balance: 1500
print(account.get_balance())  # 1500

print(account.__balance) # This will raise an AttributeError because __balance is private

'''
private attributes are not accessible outside the class. They can only be accessed through methods defined within the class. This is a way to encapsulate data and protect it from being modified directly.
'''