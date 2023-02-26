###Укротитель ссылок

##Установка:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone 
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
Создайте базу данных через команду
```
flask shell
```
```
from opinions_app import db
```
```
db.create_all()
```
Выйдите из интерактивной оболочки shell
```
exit()
```
Запускаем и пользуемся через команду
```
flask run
```

##Работа с API
Доступны два эндпоинта:
api/id/ - POST запрос
Пример POST запроса:
```
{
"url": "string",
"custom_id": "string"
}
```
api/id/short_id/ - GET запрос
Пример ответа на GET запрос:
```
{"url": "string"}
```
