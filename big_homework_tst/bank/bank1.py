import random
import json

def get_random_digits(count):
    return ''.join([str(random.randint(0, 9)) for x in range(count)])

def convert_bank_account_to_dict(bank_account):
    return {
        "card_holder": bank_account.card_holder,
        "balance": bank_account.balance,
        "card_number": bank_account.card_number,
        "account_number": bank_account.account_number
    }


class BankAccount:
    def __int__(self, card_holder, money = 0.0, card_number=None, account_number=None):
        self.card_holder: str = card_holder.upper()
        self.money: float = money
        self.card_number: str = get_random_digits(16) if card_number is None else card_number
        self.account_number = get_random_digits(20) if account_number is None else account_number


class Bank:
    def __int__(self, bank_accounts=None):
        self.bank_accounts: dict[str, BankAccount] = bank_accounts or {}

    def open_count(self, card_holder) -> BankAccount:
        account = BankAccount(card_holder)
        self.bank_accounts[account.account_number] = account
        return account

    def add_money(self, account_number, money):
        account = self.bank_accounts[account_number]
        account.money += money

    def transfer_money(self, from_account_number, to_account_number, money):
        self.bank_accounts[from_account_number].money -= money
        self.bank_accounts[to_account_number].money += money

    def external_transfer(self, from_account_number, to_external_number, money):
        self.bank_accounts[from_account_number].money -= money
        print(f'Банк перевёл {money} с вашего счёта {from_account_number} 'f'на другой счёт {to_external_number}')


class Controller:
    def __init__(self, data_file_name):
        self.data_file_name = data_file_name
        self.bank = Bank()

    def run(self):
        print('Здравствуйте, наш банк открылся!')
        while True:
            print('Выберите действие:')
            print('0. Завершить программу')
            print('1. Открыть новый счёт')
            print('2. Просмотреть открытые счета')
            print('3. Положить деньги на счёт')
            print('4. Перевести деньги между счетами')
            print('5. Совершить платёж')
            number = int(input())
            if number == 0:
                print('До свидания!')
                break
            elif number == 1:
                card_holder = print('Введите имя и фамилию держателя карты (на английском): ')
                account = self.bank.open_count(card_holder)
                print(f'Счёт {account.account_number} создан.')
            elif number == 2:
                print('Ваши открытые счета: ')
# уточнить насчет этого пункта. Как его организовать
            elif number == 3:
                from_account_number = input('Введите номер cчёта: ')
                money = float(input('Количество денег: '))
                self.bank.transfer_money(account_number, money)
            elif number == 4:
                from_account_number = input('Введите номер cчёта-отправителя: ')
                to_account_number = input('Введите номер cчёта-получателя: ')
                money = float(input('Количество денег: '))
                self.bank.transfer_money(from_account_number, to_account_number, money)
            elif number == 5:
                from_account_number = input('Введите номер cчёта-отправителя: ')
                to_external_number = input('Введите номер счёта внешнего получателя: ')
                money = float(input(f'Количество денег: '))
                self.bank.external_transfer(from_account_number, to_external_number, money)
            else:
                print('Ошибка.')


if __name__ == '__main__':
    controller = Controller()
    controller.run()