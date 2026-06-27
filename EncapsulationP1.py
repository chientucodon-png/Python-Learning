#Bài 1

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def show_info(self):
        print(f'Tên: {self.owner}\nSố dư: {self.__balance}')

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            print('Nạp tiền thành công!')
        else:
            print('Số tiền không hợp lệ!')

    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            print('Rút tiền thành công!')
        else:
            print('Số dư không đủ!')

acc_1 = BankAccount('An', 1000)
acc_1.deposit(500)
acc_1.withdraw(300)
acc_1.withdraw(5000)
acc_1.show_info()
                  