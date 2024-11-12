#EX1

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    @staticmethod
    def conversion(amount, rate):
        return amount / rate
    
    def balance(self, amount, currency = 'USD'):
        if currency == 'USD':
            pass
        else:
            amount = self.conversion(amount, 3.77)
            self._balance += amount
    
    def __str__(self):
        output = f'{self.currency} + {self.amount}'
        return output
    
    def __repr__(self):
        return f'{self.currency} + {self.amount}'
    
    def __int__(self):
       return self.amount

    # def __iadd__(self, other):
    #     if isinstance(other, Currency):
    #         if self.currency != other.currency:
    #             raise TypeError(f'Cannot add between Ccy type {self.currency} and {other.currency}')
    #     else:
    #         self.amount + other.amount
    




c1 = Currency('USD', 5)
print(str(c1))

# c1 += 10

#EX2
# in files func.py and exercise_one.py


#EX3

import random as rand
import string as str

a = ''.join(rand.choices(str.ascii_letters, k=5))
print(len(a))

#EX4

import datetime as dt

def today ():
    current_date = dt.date.today()
    print(f'Todays date is {current_date}')

today()

#EX5

def time_left():
    start_date = dt.date.today()
    end_date = dt.date(2025,1,1)
    print(end_date - start_date)

time_left()

#EX6

def lived_days(birthdate):
   birthdate = dt.date(1989, 3,30)
   current_time = dt.datetime.now()
   time_lived = current_time - birthdate
   minutes = time_lived * 24*60
   print(minutes)

#EX7
# from faker import Faker

# fake = Faker()

# fake.name()
# fake.address()

