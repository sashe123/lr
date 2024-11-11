import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def load_data(file_path):
    """Завантаження даних з CSV."""
    try:
        df = pd.read_csv(file_path)
        print("Файл CSV успішно відкрито!")
        return df
    except FileNotFoundError:
        print("Помилка: файл CSV не знайдено.")
        exit()
    except Exception as e:
        print(f"Сталася помилка при відкритті файлу: {e}")
        exit()

def plot_gender_distribution(data):
    """Побудова графіка кількості співробітників за статтю."""
    gender_stats = data['Стать'].value_counts()
    print(f"Кількість чоловіків: {gender_stats.get('Чоловіча', 0)}")
    print(f"Кількість жінок: {gender_stats.get('Жіноча', 0)}")
    gender_stats.plot(kind='bar', color=['skyblue', 'pink'], title='Кількість співробітників за статтю')
    plt.xlabel('Стать')
    plt.ylabel('Кількість')
    plt.show()

def calculate_age(birthdate_str):
    """Розрахунок віку на основі дати народження."""
    birth_year = datetime.strptime(birthdate_str, '%Y-%m-%d').year
    return datetime.now().year - birth_year

def plot_age_categories(data):
    """Графік розподілу співробітників за віковими категоріями."""
    data['Вік'] = data['Дата народження'].apply(calculate_age)
    age_brackets = {
        'менше 18': len(data[data['Вік'] < 18]),
        '18-45': len(data[(data['Вік'] >= 18) & (data['Вік'] <= 45)]),
        '45-70': len(data[(data['Вік'] > 45) & (data['Вік'] <= 70)]),
        'більше 70': len(data[data['Вік'] > 70])
    }
    print("Вікові категорії:", age_brackets)
    plt.bar(age_brackets.keys(), age_brackets.values(), color='lightgreen')
    plt.title('Кількість співробітників за віковими категоріями')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість')
    plt.show()

def plot_age_gender_distribution(data):
    """Побудова графіків кількості співробітників за віковими категоріями та статтю."""
    age_groups = {
        'менше 18': data[data['Вік'] < 18],
        '18-45': data[(data['Вік'] >= 18) & (data['Вік'] <= 45)],
        '45-70': data[(data['Вік'] > 45) & (data['Вік'] <= 70)],
        'більше 70': data[data['Вік'] > 70]
    }
    for group_name, group_data in age_groups.items():
        gender_counts = group_data['Стать'].value_counts()
        gender_counts.plot(kind='bar', title=f'Стать у віковій категорії {group_name}', color=['blue', 'purple'])
        plt.xlabel('Стать')
        plt.ylabel('Кількість')
        plt.show()

# Виконання коду
df = load_data('employees.csv')
plot_gender_distribution(df)
plot_age_categories(df)
plot_age_gender_distribution(df)
