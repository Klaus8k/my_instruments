import pathlib

x = pathlib.Path.cwd()
file_name =  '*.csv'
files_dir = pathlib.Path.home() / 'www' / 'my_instruments'
target_file = x / 'csv_files/01.01.2022-12.12.2022.csv'

with open(target_file, 'r') as file:
    count = 0
    for i in file:
        count += 1
        print(count)