import pathlib
import csv
from my_logger import logger


files_dir = pathlib.Path.cwd() / 'csv_files'
target_file = files_dir / '01.01.2022-12.12.2022.csv'


def print_dict(dict_from_csv: dict):
    sorted_dict = {}
    sorted_keys = sorted(dict_from_csv, key=dict_from_csv.get)

    for i in sorted_keys:
        sorted_dict[i] = dict_from_csv[i]
        print(i, '------', sorted_dict[i])


def cut_str(sting: str, cut: int):
    result = sting.rstrip()
    return result[:cut]


file_name = '01.01.2022-12.12.2022.csv'
csv_file = pathlib.Path.cwd() / 'csv_files' / file_name


class Pars_csv(csv.DictReader):
    def __init__(self, path):

        self.path = path
        x = open(self.path, 'r', encoding='utf8')
        super().__init__(x, delimiter=';')
        logger.warning(f'create parse -- {self}')

    def read_column(self):
        return self.fieldnames

    def count_row(self):
        return self.line_num - 1

    def check_column_val(self, name_column: str):
        result_list = []
        for i in self:
            result_list.append(i[name_column])
        return result_list


csv_dict = Pars_csv(csv_file)

result_dict = {}
for i in csv_dict:
    cash = int(i['Сумма в валюте счета'].split(',')[0])
    if i['Тип операции (пополнение/списание)'] == 'Debit' and \
            i['Категория операции'] == 'cardOperation':
        cutting_str = cut_str(i['Контрагент'], 6)
        if cutting_str not in result_dict.keys():

            result_dict[cutting_str] = cash
        else:
            result_dict[cutting_str] += cash
    summ = sum([i for i in result_dict.values()])


print_dict(result_dict)

a = 'Сумма в валюте счета'
logger.warning(f'object - {csv_dict.__sizeof__()} bite\'s')

print(cut_str(a, 4))
