import csv
from faker import Faker
import random

fake = Faker('uk_UA')

male_patronymics = [
    'Юрійович', 'Васильович', 'Григорович', 'Олександрович', 'Павлович',
    'Романович', 'Сергійович', 'Миколайович', 'Євгенович', 'Іванович',
    'Федорович', 'Ярославович', 'Дмитрович', 'Віталійович', 'Андрійович',
    'Богданович', 'Вікторович', 'Леонідович', 'Володимирович', 'Петрович'
]

female_patronymics = [
    'Юріївна', 'Василівна', 'Григорівна', 'Олександрівна', 'Павлівна',
    'Романівна', 'Сергіївна', 'Миколаївна', 'Євгенівна', 'Іванівна',
    'Федорівна', 'Ярославівна', 'Дмитрівна', 'Віталіївна', 'Андріївна',
    'Богданівна', 'Вікторівна', 'Леонідівна', 'Володимирівна', 'Петрівна'
]

gender_map = {
    'male': 'Чоловіча',
    'female': 'Жіноча'
}

# Відсоткове співвідношення чоловіків та жінок
male_ratio = 0.6
female_ratio = 0.4
total_entries = 2000

# Генеруємо дані для співробітника
def create_employee():
    gender = random.choices(['male', 'female'], [male_ratio, female_ratio])[0]
    first_name = fake.first_name_male() if gender == 'male' else fake.first_name_female()
    last_name = fake.last_name()
    patronymic = random.choice(male_patronymics if gender == 'male' else female_patronymics)
    birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
    role = fake.job()
    residence_city = fake.city()
    residence_address = fake.address()
    contact_phone = fake.phone_number()
    contact_email = fake.email()

    return [last_name, first_name, patronymic, gender_map[gender], birth_date, role, residence_city, residence_address, contact_phone, contact_email]

# Створення CSV файлу з даними
with open('employees.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([
        'Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 
        'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'
    ])

    for _ in range(total_entries):
        csv_writer.writerow(create_employee())

print("Файл CSV успішно згенеровано!")
