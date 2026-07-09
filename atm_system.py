class Atm:

    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        1. Press 1 create pin.
        2. Press 2 change pin.
        3. Press 3 check balance
        4. Press 4 withdrawl
        5. Anything else exit
        """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdrawl()
        else:
            exit()

    def create_pin(self):
        user_pin = input('enter your pin ')
        self.pin = user_pin

        user_balance = int(input('enter your balance '))
        self.balance = user_balance

        print('pin created')
        self.menu()

    def change_pin(self):
        old_pin = input('enter old pin')
        if old_pin == self.pin:
            new_pin = input('enter new pin')
            self.pin = new_pin
            print('new pin created')
        else:
            print('wrong pin')
        self.menu()

    def check_balance(self):
        user_pin = input('enter your pin')
        if user_pin == self.pin:
            print('your balance is', self.balance)
        else:
            print('wrong pin')
        self.menu()

    def withdrawl(self):
        user_pin = input('enter your pin')
        if user_pin == self.pin:
            amount = int(input('enter the amount'))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('withdraw successfully')
                print('Remaining balance:', self.balance)
            else:
                print('insufficient balance')
        else:
            print('wrong pin')
        self.menu()

obj = Atm()