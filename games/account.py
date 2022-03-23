"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
from datetime import datetime
import os
import json
import sys

BALANCE = os.path.join(sys.path[1], 'games', 'data', 'balance.txt')
HISTORY = os.path.join(sys.path[1], 'games', 'data', 'history.json')


def open_session_balance(BALANCE):
    """
    function to download balance.
    open at start program
    """
    if os.path.exists(BALANCE):
        with open(BALANCE, 'r') as f:
            return float(f.read())
    else:
        return 0.0


def open_session_history(HISTORY):
    """
    function to download history.
    open at start program
    """
    if os.path.exists(HISTORY):
        with open(HISTORY, 'r') as f:
            return dict(json.load(f))
    else:
        return {}


def to_deposit(total_cash, cash):
    """function to update balance."""
    return total_cash + cash


# main function
def account(total_cash, history):
    while True:
        print(f'Мой банковский счет. Баланс {total_cash}')
        print('-' * 30)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. запросить баланс')
        print('5. выход')
        print()

        choice = input('Выберите пункт меню: ')
        # пополнение счета
        if choice == '1':
            cash = float(input(
                f'На текущий момент на Вашем счете {total_cash} усл.ед. \nНа какую сумму Вы хотите пополнить счет: '))
            total_cash = to_deposit(total_cash, cash)

        # покупка
        elif choice == '2':
            price_bag = float(input('Введите сумму покупки: '))
            if price_bag > total_cash:
                print('К сожалению у Вас недостаточно средств')
                print('-' * 30)
            else:
                bag = input('Введине название покупки: ')
                history[str(datetime.now().time())] = bag, price_bag
                total_cash -= price_bag

        # история покупок
        elif choice == '3':
            if history == {}:
                print('Вы еще не совершали покупок')
            else:
                print()
                print('{} {:>15}    {}'.format('Дата покупки', 'Товар', 'Стоимость'))
                for k, v in history.items():
                    print(f'{k}       {v}')
        # запросить баланс
        elif choice == '4':
            print(f'Баланс: {total_cash}')
        # выход
        elif choice == '5':
            # сохраниене суммы счета
            with open(BALANCE, 'w') as f:
                f.write(str(total_cash))
            # сохраниене истории покупок
            with open(HISTORY, 'w') as f:
                json.dump(history, f)
            # exit()
            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    # При запуске программы проиходит загрузка инф. о балансе счета
    total_cash = open_session_balance(BALANCE)
    # При запуске программы проиходит загрузка инф. об истории покупок ранее
    history = open_session_history(HISTORY)
    # запуск основной программы
    account(total_cash, history)
