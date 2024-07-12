import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []
balance = 0


def check_multiplicity(amount):
    if amount % MULTIPLICITY == 0:
        return True
    else:
        return print('Сумма должна быть кратной 50 у.е.')


def deposit(amount):
    global balance
    if check_multiplicity(amount):
        balance += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {balance} у.е.')
    return balance


def withdraw(amount):
    global balance
    fee = amount * PERCENT_REMOVAL
    if fee < MIN_REMOVAL:
        fee = MIN_REMOVAL
    elif fee > MAX_REMOVAL:
        fee = MAX_REMOVAL
    limit = amount + fee
    if check_multiplicity(amount):
        if balance >= limit:
            balance = balance - amount - fee
            operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {int(fee)} у.е.. Итого {int(balance)} у.е.')
        else:
            operations.append(f'Недостаточно средств. Сумма с комиссией {int(limit)} у.е. На карте {balance} у.е.')
    else:
        operations.append(f'Недостаточно средств. Сумма с комиссией {limit} у.е. На карте {balance} у.е.')


def exit():
    global balance
    if balance > RICHNESS_SUM:
        total = balance - (balance * RICHNESS_PERCENT)
        d = decimal.Decimal(balance)*RICHNESS_PERCENT
        operations.append(f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {d} у.е. '
                          f'Итого {total} у.е.')
        operations.append(f'Возьмите карту на которой {total} у.е.')
    else:
        operations.append(f'Возьмите карту на которой {balance} у.е.')


deposit(1000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)
