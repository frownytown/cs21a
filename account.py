class Account(object):
    """
        Represent a bank account.

        Argument:
        account_holder (string): account holder's name.

        Attributes:
        holder (string): account holder's name.
        balance (float): account balance in dollars.
        """
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def __str__(self):
        return self.holder + ':$' + str(self.balance)

    def deposit(self, amount):
        """
        deposit the amount to the account.

        :param:
        amount (float): the amount to be deposited in dollars.
        :return:
        the updated account object.
        """
        self.balance += amount
        return self

    def withdraw(self, amount):
        """
        withdraw the amount from the account if possible.

        :param amount:
         amount (float): the amount to be withdrawn in dollars.
        :return:
         boolean: True if the withdrawal is successful
        """
        if self.balance >= amount:
            self.balance = self.balance - amount
            return True
        else:
            return False

        