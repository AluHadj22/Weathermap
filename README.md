# Проект WeatherMap

## О проекте
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-green)
![Html](https://img.shields.io/badge/html-orange)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-blue)


WeatherMap - это мое тестовое задание для получения работы. Этот проект разработан на языке Python с использованием фреймворка Django, а также HTML и Bootstrap,json. Он позволяет пользователю ввести название своего города и получить данные о погоде, такие как температура, ветер, давление и влажность. Для получения данных о погоде используется API OpenWeatherMap.

## Настройка проекта
1. Установите Python и Django на свой компьютер.
2. Клонируйте репозиторий с проектом с помощью следующей команды:
   ```
   git clone https://github.com/AluHadj22/Weathermap.git
   ```
3. Перейдите в директорию проекта:
   ```
   cd Weathermap
   ```
4. Установите зависимости, указанные в файле `requirements.txt`, с помощью команды:
   ```
   pip install -r requirements.txt
   ```
5. В файле `settings.py` укажите ваш API ключ от OpenWeatherMap в переменной `appid`.
6. Запустите миграции, чтобы создать базу данных:
   ```
   python manage.py migrate
   ```
7. Запустите сервер разработки Django:
   ```
   python manage.py runserver
   ```
8. Откройте веб-браузер и перейдите по адресу `http://127.0.0.1:8000/` - теперь вы можете использовать WeatherMap для получения данных о погоде.

## Используемые технологии
- Python
- Django
- HTML
- Bootstrap

## Контакты
- Автор: Alu
- Email: alu.hadjiev33@yandex.ru
- GitHub: [Your GitHub Profile](https://github.com/AluHadj22)
