# Wildberries Ассистент API

Это API ищет товары по ключевым словам в ассортименте вашего магазина Wildberries.

## Как задеплоить на Render.com

1. Зайдите на https://render.com и создайте аккаунт
2. Нажмите New → Web Service
3. Подключите ваш GitHub и создайте новый репозиторий с файлами из этого архива
4. Выберите:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`
   - Environment: Python 3.11
5. Нажмите Deploy

После публикации ваш API будет доступен по адресу:
```
https://ваш-сабдомен.onrender.com/search?query=иммунитет
```

## Пример запроса:
```
GET /search?query=суставы
```

## Ответ:
JSON с товарами (название, описание, ссылка на Wildberries)