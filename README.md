# Укротитель ссылок

## Установка:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Sharumario/yacut.git
```
```
cd yacut
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```
* Если у вас windows
    ```
    source venv/scripts/activate
    ```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Создаём .env файл
```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```
Примените миграции командой:
```
flask db migrate
```
Запускаем и пользуемся через команду
```
flask run
```

## Работа с API
API проекта доступен всем желающим. Сервис обслуживает только два эндпоинта:  

/api/id/ — POST-запрос на создание новой короткой ссылки;  
/api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому   идентификатору.  

Примеры запросов к API, варианты ответов и ошибок приведены в спецификации openapi.yml
Пример POST - запроса:  
```
{
"url": "string",
"custom_id": "string"
}
```
Пример ответа на GET запрос:  
```
{"url": "string"}
```
