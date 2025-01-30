# Бот-Telegram: Получение текущего курса валют

<p align="center">
  <img src="https://img.shields.io/badge/python-3.7%2B-blue" alt="Python version" />
</p>

Этот Telegram бот позволяет пользователям получать текущий курс валют. Бот использует API для получения актуальных данных о курсе валют и предоставляет их в удобном формате.  

## 🚀 Установка и запуск  

**Клонируйте репозиторий:**  
   ```
   git clone https://github.com/coolgromov/currency_telegram.git  
   cd currency_telegram 
   ```

**Установите зависимости:**  
   ```
   pip install python-telegram-bot requests
   ```

**Укажите ваш токен Telegram Bot API:**  
   ```
   updater = Updater('YOUR_TELEGRAM_BOT_TOKEN')
   ```

**Запустите бота:**  
   ```
   python bot_tg.py  
   ```

## 📌 Функциональность  

- Получение текущего курса USD к RUB.  
- Использует API `exchangerate-api.com` для получения курсов валют.  
- Кнопочный интерфейс для удобного взаимодействия.  

## 🛠 Требования  

- Python 3.7+  
- Библиотеки `python-telegram-bot`, `requests`

## 📝 Автор  

**Roman** – [GitHub](https://github.com/coolgromov)
