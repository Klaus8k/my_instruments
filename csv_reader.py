import pathlib
import csv
import logging

logger = logging.basicConfig(filename='log_csv.txt', filemode='a')

x = pathlib.Path.cwd()
file_name =  '*.csv'
files_dir = pathlib.Path.home() / 'www' / 'my_instruments'
target_file = x / 'csv_files/01.01.2022-12.12.2022.csv'

with open(target_file, 'r') as file:
    reader = csv.DictReader(file, delimiter=';')
    print(reader.fieldnames)

    sum = 0
    for i in reader:

        if i['Тип операции (пополнение/списание)'] == 'Debit':
            sum += int(i['Сумма в валюте счета'].split(',')[0])
            print(i['Дата транзакции'], str(i['Сумма в валюте счета']))

    print(sum)