# Notes - Сервис по созданию заметок


Сервис позволяет создавать простые заметки, при этом не прощая никаких орфографических ошибок.

## Ключевые возможности сервиса
- Создание заметок
- Регистрация, аутентификация пользователей
- Автоматическая проверка грамматики посредством использования сервиса [Яндекс.Спеллер](https://yandex.ru/dev/speller/)

## Использованные технологии
- Python 3.10
- FastAPI
- Alembic
- Uvicorn
- SQLAlchemy
- pytest
- mixer

## Как установить проект

Клонируйте репозиторий и перейдите в него в терминале:

```
git clone https://github.com/Apicqq/notes
```

```
cd notes
```
### Для запуска проекта локально:
Установите зависимости: 
* Если у вас установлен Poetry:
    ```
    poetry install
    ```
* Либо через стандартный менеджер зависимостей pip:
    
  Создайте виртуальное окружение:

    ```
    python3 -m venv venv
    ```
  Активируйте его:

    * Если у вас Linux/macOS
    
        ```
        source venv/bin/activate
        ```
    
    * Если у вас windows
    
        ```
        source venv/scripts/activate
        ```
    
        ```
        python3 -m pip install --upgrade pip
        ```
  И установите зависимости:
    ```
    pip install -r requirements.txt
    ```

Создайте файл .env:
```
touch .env
```

И наполните его переменными по примеру из файла `.env.example`
<br>
<sup>Переменная TESTING используется для выбора действующей базы данных.<br> При TESTING=True будет использована база данных SQLite, при TESTING=False — Postgres.</sup>
<br>
<br>
Примените миграции:

```
alembic upgrade head
```

Запустите проект:
```
uvicorn app.main:app
```
### Для запуска проекта через Docker:
- Создайте файл .env, наполните его данными по примеру из файла `.env.example`. Переменная `TESTING` должна быть равна `False`.
- Запустите Docker
- В терминале введите команду `docker compose build`
- После сборки образа введите команду `docker compose up -d`

### Тестирование
Для запуска тестов введите команду pytest, находясь в корневой папке проекта.
При первом запуске будет создан тестовый пользователь с данными, указанными в вашем файле `.env`, при помощи его можно протестировать доступные методы API.

### Документация

После запуска сервис будет доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Документация будет доступна по следующим адресам:

Для документации Swagger:

[https://127.0.0.1:8000/swagger](https://127.0.0.1:8000/swagger)


Для документации ReDoc:

[https://127.0.0.1:8000/redoc](https://127.0.0.1:8000/redoc)


Автор проекта: [Никита Смыков](https://github.com/Apicqq)