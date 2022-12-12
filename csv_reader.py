import pathlib
import csv
import logging

logger = logging.basicConfig(filename='log_csv.txt', filemode='a')

x = pathlib.Path.cwd()
file_name =  '*.csv'
files_dir = pathlib.Path.home() / 'www' / 'my_instruments'
target_file = x / 'csv_files/01.01.2022-12.12.2022.csv'

def print_dict(dict_from_csv: dict):
    for i in dict_from_csv.keys():
        print(i, '---->', dict_from_csv[i])

with open(target_file, 'r') as file:
    reader = csv.DictReader(file, delimiter=';')

    sum = 0

    result_dict = {}
    for i in reader:
        cash = int(i['Сумма в валюте счета'].split(',')[0])
        if i['Тип операции (пополнение/списание)'] == 'Debit' and \
                            i['Категория операции'] == 'cardOperation':

            if i['Контрагент'] not in result_dict.keys():
                result_dict[i['Контрагент']] = cash
            else:
                result_dict[i['Контрагент']] += cash



    print_dict(result_dict)