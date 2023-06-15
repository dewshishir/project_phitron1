class Bank:
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.users = []
        self.admins = []
        self.__total_blance = 10000
        self.__loan_amount = 0

    def add_user(self, user):
        if(user.get_account_type() == 'user'):
            self.users.append(user)
        else:
            print(f'user type unknown')


    def add_admin_user(self, admin):
        if(admin.get_account_type() == 'admin'):
            self.admins.append(admin)
        else:
            print(f'admin type unknown')

    def get_bank_blance(self):
        return self.__total_blance

    def loan_from_bank(self, amount, user):
        if(amount < 0):
            print(f'you cannot loan less then 0')
        elif(amount > user.check_available_balance() * 2):
            print(f'your amount is bigger then your twice blance')
        elif(amount > self.__total_blance):
            print(f'your blance is bigger then bank balance')
        else:
            user.set_user_blance(amount)
            self.__total_blance -= amount
            self.__loan_amount += amount

    def get_bank_loan_amount(self):
        return self.__loan_amount
    
class User:
    def __init__(self, unique_id, name, email, password, account_type) -> None:
        self.unique_id = unique_id
        self.name = name
        self.email = email
        self.__password = password
        self.__account_type = account_type
        self.__balance = 0
        self._history = []
    
    def deposit(self, amount):
        if(amount < 0):
            print(f'You are given {0} or nagative value {amount}')
        else:
            self.__balance += amount
            history = previous(self.name, self.check_available_balance(), 0, amount, 0)
            self._history.append(history)

    def create_user_account(self, unique_id, name, email, password, account_type):
        user = User(unique_id, name, email, password, account_type)
        return user

    def withdraw(self, amount):
        if(amount < 0):
            print(f'You can not {0} or nagative value {amount} withdraw')
        elif(amount > self.__balance):
            print(f'You can not {amount} withdraw beacuse {amount} is bigger then {self.__balance}')
        else:
            self.__balance -= amount
            history = previous(self.name, self.check_available_balance(), amount, 0)
            self._history.append(history)

    def check_available_balance(self):
        return self.__balance
    
    def set_user_blance(self, amount):
        self.__balance += amount

    def get_account_type(self):
        return self.__account_type
    
    def transfer_amount(self, amount, from_user, to_user):
        if(amount < 0):
            print(f'{from_user.name} have not enough mony to transfer {to_user.name}!')
        elif(from_user.check_available_balance() < amount):
            print(f'{from_user.name} transfer amount {amount} bigger then self balance {from_user.check_available_balance()}!')
        else:
            to_user.__balance += amount
            from_user.__balance -= amount
            history = previous(self.name, self.check_available_balance(), 0, 0, amount)
            self._history.append(history)

    def transaction_history(self):
        for x in self._history:
            print(f'name: {x.name}, amoutn: {x.amount} withdraw: {x.widthraw} diposit: {x.diposit} transfer: {x.transfer}')

class Admin:
    def __init__(self, unique_id, name, email, password, account_type) -> None:
        self.unique_id = unique_id
        self.name = name
        self.email = email
        self.__account_type = account_type
        self.__password = password
        self.__account_type = account_type

    def create_admin_account(self, unique_id, name, email, password, account_type):
        user = User(unique_id, name, email, password, account_type)
        return user
    
    def available_total_balance(self, bank):
        return bank.get_bank_blance()
    
    def get_account_type(self):
        return self.__account_type
    
    def get_loan_from_bank(self, bank):
        return bank.get_bank_loan_amount()
    
    def off_loan_feature(self):
        print('Off loan feature for all admin and user account')

class previous:
    def __init__(self, name, amount, widthraw = 0, diposit = 0, transfer = 0) -> None:
        self.name = name
        self.amount = amount
        self.widthraw = widthraw
        self.diposit = diposit
        self.transfer = transfer

def Main():
    ific = Bank('IFIC Bank', 'mainific@gmail.com', 'umme, rajshahi')
    print(f'************THIS IS {ific.name} ************')

    user_1 = User('681', 'belal hossain', 'belal@gmail.com', '123456', 'user')
    user_2 = User('682', 'anan jok', ' ananjok@gmail.com', '372730', 'user')
    user_3 = User('683', 'zahidul', ' zahidul@gmail.com', '8493784', 'user')
    user_4 = User('684', 'ronju', ' ronju@gmail.com', '9893784', 'user')

    
    admin_1 = Admin('8923h2w3874', 'belal hossain', 'belal@gmail.com', 'uiweui32u4', 'admin')
    admin_2 = Admin('sahd92839hf', 'anan jok', ' ananjok@gmail.com', 'hbfbh324ruj', 'admin')
    admin_3 = Admin('sdoifj8203h', 'zahidul', ' zahidul@gmail.com', 'hsfg8237g', 'admin')

    user_1.deposit(7000)
    user_2.deposit(4000)
    user_3.deposit(6000)
    user_4.deposit(1000)

    print(user_1.check_available_balance())
    print(user_2.check_available_balance())
    print(user_3.check_available_balance())
    print(user_4.check_available_balance())
    user_1.transfer_amount(1300, user_1, user_2)
    user_2.transfer_amount(8000, user_2, user_1)
    user_3.transfer_amount(500, user_3, user_1)
   

    ific.add_user(user_1)
    ific.add_user(user_2)
    ific.add_user(user_3)
    ific.add_user(user_4)


    ific.add_admin_user(admin_1)
    ific.add_admin_user(admin_2)
    ific.add_admin_user(admin_3)

    print('************HERE IS MY ALL USERS************\n')
    for user in ific.users:
        print(f'name: {user.name} email: {user.email}  type: {user.get_account_type()}')
    print('\n')


    print('************THIS IS MY USER TRANSACTION HISTORY************\n')
    user_1.withdraw(30)
    user_2.withdraw(50)
    user_2.withdraw(700)
    user_3.withdraw(1350)
    user_3.deposit(70)
    user_2.deposit(1700)
    user_2.transaction_history() 
    print('\n')
    user_1.transaction_history()
    print('\n')
    user_3.transaction_history()
    print('\n')


    print('************LOAN FROM BANK TO USER************')
    print(f'before current bank balance: {ific.get_bank_blance()}')
    ific.loan_from_bank(1200, user_1)
    print(f'after current bank balance: {ific.get_bank_blance()}')
    print(f'right now user current blance: {user_1.check_available_balance()} \n')

    print(f'before current bank balance: {ific.get_bank_blance()}')
    ific.loan_from_bank(1400, user_2)
    print(f'after current bank balance: {ific.get_bank_blance()}')
    print(f'right now user current blance: {user_2.check_available_balance()}\n')

    print(f'before current bank balance: {ific.get_bank_blance()}')
    ific.loan_from_bank(1800, user_3)
    print(f'after current bank balance: {ific.get_bank_blance()}')
    print(f'right now user current balance: {user_3.check_available_balance()}\n')
  

    print('************HERE IS MY ALL ADMIN USERS************\n')
    for admin in ific.admins:
        print(f'name: {admin.name} email: {admin.email}  type: {admin.get_account_type()}')
    print('\n')

    print('************HERE BANK LOAN AND TOTAL AMOUNT SHOWING************')
    print(f'bank total available blance: {admin_1.available_total_balance(ific)}')
    print(f'bank loan amount: {admin_1.get_loan_from_bank(ific)}')
    admin_1.off_loan_feature()



if __name__ == '__main__':
    Main()