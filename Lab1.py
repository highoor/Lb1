import requests  # Для отправки HTTP-запросов к API НБУ
from datetime import datetime, timedelta  # Для работы с датами
import matplotlib.pyplot as plt  # Для построения графиков

# Базовый URL API НБУ для получения курсов валют
BASE_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

# Функция для получения курсов валют за конкретную дату
def get_exchange_rate(date):
   
    formatted_date = date.strftime('%Y%m%d')  # Преобразуем дату в формат YYYYMMDD
    response = requests.get(f"{BASE_URL}?date={formatted_date}&json")  # Отправляем GET-запрос к API
    if response.status_code == 200:  # Если запрос успешен
        return response.json()  # Возвращаем данные в формате JSON
    else:
        print(f"Ошибка получения данных для {formatted_date}: {response.status_code}")
        return None  # Возвращаем None в случае ошибки

# Функция для получения курсов валют за последние 7 дней
def get_last_week_rates():
    
    today = datetime.now()  # Текущая дата
    last_week = [today - timedelta(days=i) for i in range(7)]  # Список дат за последние 7 дней
    rates = {}  # Словарь для хранения курсов валют
    for date in last_week:  # Проходим по каждой дате
        data = get_exchange_rate(date)  # Получаем данные
        if data:  # Если данные получены
            rates[date.strftime('%Y-%m-%d')] = data  # Сохраняем курсы валют по дате
    return rates  # Возвращаем словарь с курсами валют

# Функция для построения графика изменения курса валют
def plot_currency_change(rates, currency_code="USD"):
   
    dates = []  # Список для хранения дат
    currency_rates = []  # Список для хранения значений курса валюты

    for date, data in rates.items():  # Проходим по всем датам и данным из словаря
        dates.append(date)  # Добавляем дату в список
        # Находим курс для указанного кода валюты
        rate = next((item['rate'] for item in data if item['cc'] == currency_code), None)
        if rate:  # Если курс найден
            currency_rates.append(rate)  # Добавляем курс в список

    if not currency_rates:
        print(f"Не удалось найти данные для валюты {currency_code}")
        return

    # Построение графика
    plt.figure(figsize=(10, 5))  # Размер графика
    plt.plot(dates, currency_rates, marker='o', label=currency_code, color='blue')  # Линия графика с маркерами
    plt.title(f"Изменение курса {currency_code} за последние 7 дней", fontsize=14)  # Заголовок графика
    plt.xlabel("Дата", fontsize=12)  # Подпись оси X
    plt.ylabel("Курс", fontsize=12)  # Подпись оси Y
    plt.grid(True)  # Включаем сетку
    plt.legend(fontsize=12)  # Добавляем легенду
    plt.xticks(rotation=45)  # Поворачиваем метки оси X для удобства
    plt.tight_layout()  # Автоматическая подгонка графика
    plt.show()  # Показываем график

# Основной блок кода
if __name__ == "__main__":
    # Получаем данные о курсах валют за последние 7 дней
    rates = get_last_week_rates()

    # Проверяем, удалось ли загрузить данные
    if rates:
        # Строим график для валюты USD (доллар США)
        plot_currency_change(rates, currency_code="USD")
    else:
        print("Не удалось загрузить данные о курсах валют.")
