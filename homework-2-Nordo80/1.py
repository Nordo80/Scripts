import datetime


class Customer:
    """Customer class."""

    def __init__(self, name: str, address: str, dob: str, card_number: int, pin: int):
        """Customer constructor."""
        self.name = name
        self.address = address
        self.dob = dob
        self.card_number = card_number
        self.pin = pin

    def verify_pass(self, password: int):
        """Password verification."""
        pass


class Bank:
    """Bank class."""

    def __init__(self, code: int, address: str):
        """Bank constructor."""
        self.code = code
        self.address = address
        self._revenue = 0

    def __manages(self):
        pass

    def __maintains(self):
        pass

    def _print_revenue(self, is_from, to):
        """Printing the revenue from 1 bank to another."""
        pass


class ATM:
    """ATM class."""

    def __init__(self, location: str, managed_by: str):
        """ATM constructor."""
        self.location = location
        self.managed_by = managed_by

    def identifies(self, customer):
        """Customer identification."""
        pass

    def transaction(self):
        """Transactions."""
        pass


class Account:
    """Account class."""

    def __init__(self, number: int, balance: int):
        """Account constructor."""
        self.number = number
        self._balance = balance

    def _authenticate(self, pin: int):
        """Authentication."""
        pass

    def deposit(self, amount: int):
        """Deposit to account."""
        pass

    def withdraw(self, amount: int):
        """Withdraw from account."""
        pass

    def __create_transaction(self, date):
        """Creating transaction."""
        pass


class CurrentAccount(Account):
    def __init__(self, account_no: str, balance: int, interest_rate: int, number: int):
        super().__init__(number, balance)
        self.account_no = account_no
        self.balance = balance
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        pass

    def apply_interest(self):
        pass


class SavingAccount(Account):
    def __init__(self, num: int, holder: str, credit_range: int, number: int, balance: int):
        super().__init__(number, balance)
        self.num = num
        self.holder = holder
        self._credit_range = credit_range

    def withdraw(self, amount):
        pass


class ATM_Transaction:
    """ATM_Transaction class."""

    def __init__(self, transaction_id: int, date: str, type: str, amount: int, post_balance: int):
        """ATM_ Transaction constructor."""
        self.transaction_id = transaction_id
        self.date = date
        self.type = type
        self.amount = amount
        self.post_balance = post_balance

    def updates(self, account):
        """Update balance on account."""
        pass


if __name__ == '__main__':
    customer1 = Customer("Sasha", "liikuri40", "lala", 232324, 2222)
    print(customer1.return_address())
