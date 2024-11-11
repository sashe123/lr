import pandas as pd
from openpyxl import Workbook
from datetime import datetime
from openpyxl.utils.dataframe import dataframe_to_rows

# Функція для обчислення віку
def get_age(birth_date):
    birth_year = pd.to_datetime(birth_date).year
    current_year = datetime.now().year
    return current_year - birth_year

# Спроба завантажити CSV файл
try:
    employees_df = pd.read_csv('employees.csv')
    print("Ok, файл CSV успішно відкрито!")
except FileNotFoundError:
    print("Помилка: файл CSV не знайдено.")
    exit()

# Додавання колонки "Вік" до DataFrame
employees_df['Вік'] = employees_df['Дата народження'].apply(get_age)

# Створення XLSX файлу
workbook = Workbook()
ws_all_data = workbook.active
ws_all_data.title = "all"

# Запис заголовків у таблицю
ws_all_data.append(['№', 'Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'])

# Запис всіх даних співробітників
for index, row in enumerate(dataframe_to_rows(employees_df, index=False, header=False), start=1):
    ws_all_data.append([index] + row)

# Визначення вікових категорій
age_groups = {
    'younger_18': employees_df[employees_df['Вік'] < 18],
    '18-45': employees_df[(employees_df['Вік'] >= 18) & (employees_df['Вік'] <= 45)],
    '45-70': employees_df[(employees_df['Вік'] > 45) & (employees_df['Вік'] <= 70)],
    'older_70': employees_df[employees_df['Вік'] > 70]
}

# Створення окремих аркушів для кожної вікової категорії
for sheet_name, age_data in age_groups.items():
    worksheet = workbook.create_sheet(title=sheet_name)
    worksheet.append(['№', 'Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік'])
    for index, row in enumerate(dataframe_to_rows(age_data, index=False, header=False), start=1):
        worksheet.append([index] + row[:6])

# Спроба зберегти файл XLSX
try:
    workbook.save('employees.xlsx')
    print("Ok, XLSX файл успішно створено!")
except Exception as error:
    print(f"Неможливо створити XLSX файл. Помилка: {error}")
