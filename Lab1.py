# import requests
# from datetime import datetime, timedelta

# # Базовий URL для отримання курсу валют
# BASE_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

# # Функція для отримання курсу валют за конкретну дату
# def get_exchange_rate(date):
#     formatted_date = date.strftime('%Y%m%d')  # Формат YYYYMMDD
#     response = requests.get(f"{BASE_URL}?date={formatted_date}&json")
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error fetching data for {formatted_date}: {response.status_code}")
#         return None

# # Отримання курсу валют за попередній тиждень
# def get_last_week_rates():
#     today = datetime.now()
#     last_week = [today - timedelta(days=i) for i in range(7)]
#     rates = {}
#     for date in last_week:
#         rates[date.strftime('%Y-%m-%d')] = get_exchange_rate(date)
#     return rates

# # Виклик функції та друк результатів
# rates = get_last_week_rates()
# for date, data in rates.items():
#     print(f"Date: {date}, Rates: {data}")

##############################################################################

# # Импорт необходимых библиотек
# import requests  # Для отправки HTTP-запросов к API НБУ
# from datetime import datetime, timedelta  # Для работы с датами
# import matplotlib.pyplot as plt  # Для построения графиков

# # Базовый URL API НБУ для получения курсов валют
# BASE_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

# # Функция для получения курсов валют за конкретную дату
# def get_exchange_rate(date):
#     """
#     Получить курсы валют за указанную дату.

#     :param date: объект datetime, представляющий дату
#     :return: JSON-ответ с курсами валют за указанную дату
#     """
#     formatted_date = date.strftime('%Y%m%d')  # Преобразуем дату в формат YYYYMMDD
#     response = requests.get(f"{BASE_URL}?date={formatted_date}&json")  # Отправляем GET-запрос к API
#     if response.status_code == 200:  # Если запрос успешен
#         return response.json()  # Возвращаем данные в формате JSON
#     else:
#         print(f"Ошибка получения данных для {formatted_date}: {response.status_code}")
#         return None  # Возвращаем None в случае ошибки

# # Функция для получения курсов валют за последние 7 дней
# def get_last_week_rates():
#     """
#     Получить курсы валют за последние 7 дней.

#     :return: словарь с датами и курсами валют
#     """
#     today = datetime.now()  # Текущая дата
#     last_week = [today - timedelta(days=i) for i in range(7)]  # Список дат за последние 7 дней
#     rates = {}  # Словарь для хранения курсов валют
#     for date in last_week:  # Проходим по каждой дате
#         rates[date.strftime('%Y-%m-%d')] = get_exchange_rate(date)  # Сохраняем курсы валют по дате
#     return rates  # Возвращаем словарь с курсами валют

# # Функция для построения графика изменения курса валют
# def plot_currency_change(rates, currency_code="USD"):
#     """
#     Построить график изменения курса валюты.

#     :param rates: словарь с датами и курсами валют
#     :param currency_code: код валюты, для которой строится график (по умолчанию USD)
#     """
#     dates = []  # Список для хранения дат
#     currency_rates = []  # Список для хранения значений курса валюты
    
#     for date, data in rates.items():  # Проходим по всем датам и данным из словаря
#         dates.append(date)  # Добавляем дату в список
#         # Находим курс для указанного кода валюты
#         rate = next((item['rate'] for item in data if item['cc'] == currency_code), None)
#         if rate:  # Если курс найден
#             currency_rates.append(rate)  # Добавляем курс в список

#     # Построение графика
#     plt.figure(figsize=(10, 5))  # Размер графика
#     plt.plot(dates, currency_rates, marker='o', label=currency_code, color='blue')  # Линия графика с маркерами
#     plt.title(f"Зміна курсу {currency_code} за останній тиждень", fontsize=14)  # Заголовок графика
#     plt.xlabel("Дата", fontsize=12)  # Подпись оси X
#     plt.ylabel("Курс", fontsize=12)  # Подпись оси Y
#     plt.grid(True)  # Включаем сетку
#     plt.legend(fontsize=12)  # Добавляем легенду
#     plt.xticks(rotation=45)  # Поворачиваем метки оси X для удобства
#     plt.tight_layout()  # Автоматическая подгонка графика
#     plt.show()  # Показываем график

# # Основной блок кода
# if __name__ == "__main__":
#     # Получаем данные о курсах валют за последние 7 дней
#     rates = get_last_week_rates()

#     # Проверяем, удалось ли загрузить данные
#     if rates:
#         # Строим график для валюты USD (доллар США)
#         plot_currency_change(rates, currency_code="USD")
#     else:
#         print("Не удалось загрузить данные о курсах валют.")

