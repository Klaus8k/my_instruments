import pathlib

x = pathlib.Path.cwd()
file_name =  '*.csv'
files_dir = pathlib.Path.home() / 'www' / 'my_instruments'
target_file = x / 'csv_files/01.01.2022-12.12.2022.csv'

i = target_file.read_text()

list_target_file_csv = i.split('\n')

