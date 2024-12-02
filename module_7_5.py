import  os
import time

directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory)
        filetime = os.path.getmtime(directory)
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
        file_size = os.path.getsize(directory)
        parent_dir = os.path.dirname(directory)
print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}, '
      f'Родительская директория: {parent_dir}')
# Обнаружен файл: test_file.txt, Путь: C:\Users\user\PycharmProjects\pythonProject\Файлы, Размер: 4096 байт,
# Время изменения: 02.12.2024 23:21, Родительская директория: C:\Users\user\PycharmProjects\pythonProject