import json
import os
import random
from func.functions import *
from games.victory import get_5famous
from games.account import to_deposit, open_session_balance, open_session_history


# "чистые функции"
def test_account_to_deposit():
    assert to_deposit(0, 10) == 10
    assert to_deposit(1000, 300) == 1300
    assert isinstance(to_deposit(10., 5.6), float)
    assert isinstance(to_deposit(100, 5), int)
    assert type(to_deposit(100, 5)) != str


def test_get_5famous():
    assert len(get_5famous(list(range(10)), 5)) == 5
    assert len(get_5famous(list(range(100)), 10)) == 10
    test_list = list(range(20))
    for i in get_5famous(test_list, 10):
        assert i in test_list


def test_create_folder():
    # проверка создания рандом папки, после ее удаление
    folder_name = str(random.getrandbits(32))
    if not os.path.exists(folder_name):
        assert create_folder(folder_name) == f'Создана папка {os.path.join(os.getcwd(), folder_name)}'
        assert os.path.exists(folder_name) == True
    os.rmdir(folder_name)


def test_delete_file_folder():
    # проверка удаления папки
    rm_folder_or_file = str(random.getrandbits(32))
    os.mkdir(rm_folder_or_file)
    if os.path.exists(rm_folder_or_file):
        assert delete_file_folder(rm_folder_or_file) == f'Папка с именем {rm_folder_or_file} была удалена'
    assert os.path.exists(rm_folder_or_file) == False
    # проверка удаления файла
    file_txt = str(random.getrandbits(32)) + '.txt'
    rm_file = open(file_txt, 'w+')
    rm_file.close()
    if os.path.exists(file_txt):
        assert delete_file_folder(file_txt) == f'Файл с именем {file_txt} был удален'
    assert os.path.exists(file_txt) == False


def test_look_only_files():
    for file in look_only_files():
        assert os.path.isfile(file)


def test_look_only_folder():
    for folder in look_only_folder():
        assert os.path.isdir(folder)


def test_open_session_account():
    balance = str(random.getrandbits(32))
    with open(balance, 'w') as f:
        f.write('100')
    assert open_session_balance(balance) == 100.0
    os.remove(balance)


def test_open_session_history():
    history = str(random.getrandbits(32))
    check_dict = {'1': random.getrandbits(32),
                  '2': random.getrandbits(32)}
    with open(history, 'w') as f:
        json.dump(check_dict, f)
    assert open_session_history(history) == check_dict
    os.remove(history)


def test_create_list_dir():
    assert create_list_dir()[0] == 'Содержимое рабочей директории сохранено'
    assert os.path.isfile(create_list_dir()[1])
    assert os.path.getsize(create_list_dir()[1]) > 0


def test_check_name_folder_or_file():
    assert check_name_folder_or_file('123') == False
