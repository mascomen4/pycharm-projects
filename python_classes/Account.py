#!usr/bin/env python3
# Copyright QTRAC Corp. (c). Wrote by Podmogilniy Ivan
# Study project provided by book "Programming in Python 3". One of realization of OOP 

""" Module provide to manipulate with money opreations"""

import pickle

class SaveError(Exception): pass
class LoadError(Exception): pass


class Account:
    """ The object of class Account contains number of account, his name,
    and list of objects of class Transaction

    >>> import os
    >>> import tempfile
    >>> name = os.path.join(tempfile.gettempdir(), "account01")
    >>> account = Account(name, "Qtrac Ltd.")
    >>> os.path.basename(account.number), account.name,
    ('account01', 'Qtrac Ltd.')
    >>> account.balance, account.all_usd, len(account)
    (0.0, True, 0)
    >>> account.apply(Transaction(100, "2008-11-14"))
    >>> account.apply(Transaction(150, "2008-12-09"))
    >>> account.apply(Transaction(-95, "2009-01-22"))
    >>> account.balance, account.all_usd, len(account)
    (155.0, True, 3)
    >>> account.apply(Transaction(50, "2008-12-09", "EUR", 1.53))
    >>> account.balance, account.all_usd, len(account)
    (231.5, False, 4)
    >>> account.save()
    >>> newaccount = Account(name, "Qtrac Ltd.")
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (0.0, True, 0)
    >>> newaccount.load()
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (231.5, False, 4)
    >>> try:
    ...     os.remove(name + ".acc")
    ... except EnvironmentError:
    ...     pass
    """
    def __init__(self, number, name, transactions):
        if not isinstance(transactions, list):
            transactions = list((transactions,))
        self.__number = number
        self.__name = name
        self.__transactions = transactions

    @property
    def number(self):
        return self.__number

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        assert len(name) > 3, "account name must be at least 4 characters"
        self.__name = name
    
    @property
    def balance(self):
        """ Return the all money in Account converted to usd

        >>> trans1 = Transaction(5000, '01.01.2001')
        >>> alfred_account = Account(12345, 'Alfred', trans1)
        >>> alfred_account.balance
        5000
        """
        amount_all = 0
        for transaction in self.__transactions:
            amount_all += transaction.usd
        return amount_all

    @property
    def all_usd(self):
        """ Returns True if all transactions are in the USD

        >>> trans1 = Transaction(5000, '01.01.2001')
        >>> alfred_account = Account(12345, 'Alfred', trans1)
        >>> alfred_account.all_usd
        True
        """
        for transaction in self.__transactions:
            if transaction.currency not in {'USD', 'usd', 'dollar'}:
                return False
        return True
    
    def __len__(self):
        """ Returns how many transactions are in the Account """
        return len(self.__transactions)

    def apply(self, transaction):
        """ Apply Transaction object to the Account """
        self.__transactions.append(transaction)
    
    def save(self):
        """ Save the Account object in file whose name is number of Account

        >>> trans1 = Transaction(1, '01.01.2006')
        >>> acc1 = Account(12345, "acc1", trans1)
        >>> acc1.save()
        >>> import os
        >>> if "12345.acc" in os.listdir(): print("All OK")
        All OK
        """
        filename = str(self.number)
        filename += ".acc" 
        fh = None
        try:
            data = [self.number, self.name, self.__transactions]
            fh = open(filename, 'wb')
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close

    def load(self, filename):
        """ Load the items from account file and itialize it.

        All previous lost

        >>> trans1 = Transaction(1, '01.01.2006')
        >>> acc1 = Account(12345, "acc1", trans1)
        >>> acc1.save()
        >>> acc1.name = "Freddy"
        >>> acc1.name
        'Freddy'
        >>> acc1.load("12345.acc")
        >>> acc1.name
        'acc1'

        """
        if not filename.endswith(".acc"):
            filename += ".acc"
        fh = None
        try:
            fh = open(filename, "rb")
            data = pickle.load(fh)
            self.__number, self.name, self.__transactions = data
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()

class Transaction:
    """ The objects of this class contains the attributes of transaction
    
    >>> trans1 = Transaction(5000, '01.01.2001', 'RUB', 68, 'Description')
    >>> trans1.date
    '01.01.2001'
    >>> trans1.currency
    'RUB'
    >>> trans1.description
    'Description'
    """

    def __init__(self, amount, date, currency = "USD",
                 usd_conversation_rate = 1, description = None):
        """ Currency used by default: USD, 'usd_coversation_rate' don't changes 
        automatically. You shall do it yourself.
        
        >>> trans1 = Transaction(1, '01.01.2006')
        >>> trans1.currency
        'USD'
        >>> trans1.description
        """
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__usd_conversation_rate = usd_conversation_rate
        self.__description = description
        self.__usd = self.amount * self.usd_conversation_rate

    def __str__(self):
        return ('Transaction({0.amount}, {0.date}, {0.currency}, {0:'
                '.usd_conversation_rate}, {0.description}'.format(self)) 

    @property
    def amount(self):
        assert self.__amount >= 0, "The amount must be non-negative"
        return self.__amount

    @property
    def date(self):
        return self.__date

    @property
    def currency(self):
        return self.__currency  

    @property
    def usd_conversation_rate(self):
        assert self.__usd_conversation_rate >= 0, ("The"
                        "'usd_conversation_rate' must  be non-negative")
        return self.__usd_conversation_rate  

    @property
    def description(self):
        return self.__description

    @property
    def usd(self):
        return self.__usd
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
