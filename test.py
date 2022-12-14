import pathlib
import csv

file_name = '01.01.2022-12.12.2022.csv'
csv_file = pathlib.Path.cwd() / 'csv_files' / file_name

class Pars_csv(csv.DictReader):
    def __init__(self, path):
        self.path = path
        x = open(self.path, 'r', encoding='utf8')
        super().__init__(x, delimiter=';')

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

        if i['Контрагент'].rstrip() not in result_dict.keys():

            result_dict[i['Контрагент'].rstrip()] = cash
        else:
            result_dict[i['Контрагент'].rstrip()] += cash


print(result_dict)