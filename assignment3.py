#Assignment 3 : Write a program to implement a Configurable Payment Processing System using the Strategy Pattern.

class netBanking:

    def payment(self):
        print("Payment made using Net Banking")

class UPI:
    def payment(self):
        print("Payment made using UPI")

class credit:
    def payment(self):
        print("Payment made using Credit Card")

class debit:
    def payment(self):
        print("Payment made using Debit Card")

class Transaction:

    def __init__(self, mode):

        self.mode = mode

    def pay(self):

        self.mode.payment()

payment1 = Transaction(netBanking())
payment2 = Transaction(UPI())
payment3 = Transaction(credit())
payment4 = Transaction(debit())

payment1.pay()
payment2.pay()
payment3.pay()
payment4.pay()

