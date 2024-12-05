import  os
import time

directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}, '
      f'Родительская директория: {parent_dir}')
# Обнаружен файл: test_file.txt, Путь: C:\Users\user\PycharmProjects\pythonProject\Файлы\test_file.txt, 
# Размер: 169 байт, Время изменения: 01.12.2024 20:39, 
# Родительская директория: C:\Users\user\PycharmProjects\pythonProject\Файлы
