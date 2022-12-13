import pathlib
import csv
import logging

logger = logging.basicConfig(filename='log_csv.txt', filemode='a')

files_dir = pathlib.Path.cwd() / 'csv_files'
target_file = files_dir / '01.01.2022-12.12.2022.csv'

print(target_file)

def print_dict(dict_from_csv: dict):
    sorted_dict = {}
    sorted_keys = sorted(dict_from_csv, key=dict_from_csv.get)

    suming = 0
    for i in sorted_keys:
        sorted_dict[i] = dict_from_csv[i]
        print(i, '------', sorted_dict[i])
        suming += sorted_dict[i]

    print(suming)





with open(target_file, 'r', encoding='utf8') as file:
    reader = csv.DictReader(file, delimiter=';')

    sum = 0

    result_dict = {}
    for i in reader:
        cash = int(i['Сумма в валюте счета'].split(',')[0])
        if i['Тип операции (пополнение/списание)'] == 'Debit' and \
                            i['Категория операции'] == 'cardOperation':
                                   

            if i['Контрагент'].rstrip() not in result_dict.keys():


                result_dict[i['Контрагент'].rstrip()] = cash
            else:
                result_dict[i['Контрагент'].rstrip()] += cash




    print_dict(result_dict)