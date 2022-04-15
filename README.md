### Описание
API-сервис приложения социальной сети **Yatube**.

#### Использованы технологии:
- Python 3.7.0;
- Django 2.2.16;
- Django REST framework 3.12.4;
- Simple JWT 4.7.2.

##### ***Примечание:*** в данной версии реализован механизм отмены действия текущего access-токена в случае получения нового (предусмотрено на случай компрометации текущего токена).

### Данный сервис позволяет через стандартные HTTP запросы выполнять следующие команды:

#### ![Изображение незарегистрированного пользователя](https://cdn2.scratch.mit.edu/get_image/user/60928233_60x60.png) Для незарегистрированных пользователей:
  - Публикации:
    - Просмотр списка публикаций: **GET**-запрос на адрес `http://127.0.0.1:8000/api/v1/posts/`, предусмотрена пагинация (разбиение выводимой информации на страницы) по параметрам запроса (идут в URL после **?**) *limit=число* (количество выводимых на экран публикаций) и *offset=число*(с какой публикации начинать показ).
    - Просмотр конкретной публикации: **GET**-запрос на адрес `http://127.0.0.1:8000/api/v1/posts/{номер_публикации}/`.
  - Комментарии к постам:
    - Просмотр списка комментариев к посту: **GET**-запрос на адрес `http://127.0.0.1:8000/api/v1/posts/{номер_публикации}/comments/`.
    - Просмотр комментария к посту: **GET**-запрос на адрес `http://127.0.0.1:8000/api/v1/posts/{номер_поста}/comments/{номер_комментария}/`.
  - Группы:
    - Просмотр списка сообществ: **GET**-запрос на адрес `http://127.0.0.1:8000/api/v1/groups/`.
    - Просмотр конкретного сообщества: **GET**-запрос на адрес `http://127.0.0.1:8000/api/v1/groups/{номер_сообщества}/`.
    
#### ![Изображение зарегистрированного пользователя](https://yumtrade.ru/35929-33226-medium/modul-verifikacija-lic.jpg) Для зарегистрированных пользователей:
  - Токен:
    - Получение токена: **POST**-запрос на адрес `http://127.0.0.1:8000/api/v1/jwt/create/` с передачей имени зарегистрированного пользователя[^1] по ключу `username` и его пароля[^1] по ключу `password`; ответ будет содержать ***access-токен*** (используется для выполнения запросов, требующих авторизации [помечены далее звзедочкой]) и ***refresh-токен*** (используется для обновления access-токена).
    - Обновление токена: **POST**-запрос на адрес `http://127.0.0.1:8000/api/v1/jwt/refresh/` с передачей в теле запроса ***refresh-токена***[^1] по ключу `"refresh"`.
    - Проверка токена[^2]: **POST**-запрос на адрес `http://127.0.0.1:8000/api/v1/jwt/verify/` с передачей в теле запроса проверяемого ***access-***[^1] либо ***refresh-токена***[^1] по ключу `"token"`.
  - Публикации:
    - Просмотр списка публикаций: **GET**-запрос на адрес `http://127.0.0.1:8000/api/v1/posts/`, предусмотрена пагинация (разбиение выводимой информации на страницы) по параметрам запроса (идут в URL после **?**, указываемого после последнего слэша) *limit=число* (количество выводимых на экран публикаций) и *offset=число*(с какой публикации начинать показ).
    - Просмотр конкретной публикации: **GET**-запрос на адрес `http://127.0.0.1:8000/api/v1/posts/{номер_публикации}/`.
    - Добавление поста[^2] **POST**-запрос на адрес `http://127.0.0.1:8000/api/v1/posts/` с передачей в теле запроса ключей со значениями[^1]:
      - `"text"` - строка символов;
      - `"image"` - строка символов или *null*(ничего) - необязательное поле;
      - `"group"` - идентификационный (*id*) номер сообщества - необязательное поле.
    - Изменение своей публикации[^2]: **PATCH**- (для частичого изменения) или **PUT**-запрос (для полного изменения) на адрес `http://127.0.0.1:8000/api/v1/posts/{номер_публикации}/` с передачей в теле запроса ключей со значениями[^1] изменяемых полей:
      - `"text"` - строка символов;
      - `"image"` - строка символов или *null*(ничего);
      - `"group"` - идентификационный (*id*) номер сообщества.     
    - Удаление своей публикации[^2]: **DELETE**-запрос на адрес `http://127.0.0.1:8000/api/v1/posts/{номер_публикации}/`.
  - Комментарии к публикациям:
    - Просмотр списка комментариев к публикации: **GET**-запрос на адрес `http://127.0.0.1:8000/api/v1/posts/{номер_публикации}/comments/`.
    - Просмотр конкретного комментария к публикации: **GET**-запрос на адрес `http://127.0.0.1:8000/api/v1/posts/{номер_публикации}/comments/{номер_комментария}/`.
    - Написание комментария к публикации[^2]: **POST**-запрос на адрес `http://127.0.0.1:8000/api/v1/posts/{номер_публикации}/comments/` с передачей в теле запроса текста[^1] по ключу `"text"`.
    - Изменение своего комментария к публикации[^2]: **PATCH**- (для частичого изменения) или **PUT**-запрос (для полного изменения) на адрес `http://127.0.0.1:8000/api/v1/posts/{номер_публикации}/comments/{номер_комментария}/` с передачей в теле запроса текста[^1] по ключу `"text"`.
    - Удаление своего комментария к публикации[^2]: **DELETE**-запрос на адрес `http://127.0.0.1:8000/api/v1/posts/{номер_публикации}/comments/{номер_комментария}/`.
  - Подписки на авторов:
    - Заведение подписки на автора[^2]: **POST**-запрос на адрес `http://127.0.0.1:8000/api/v1/follow/` с передачей в теле запроса имени автора[^1] по ключу `"following"`.
    - Получение подписок пользователя, отправляющего запрос: **GET**-запрос на адрес `http://127.0.0.1:8000/api/v1/follow/`; предусмотрен поиск подписок по имени автора, на которого подписан пользователь, передаваемого через параметр запроса (идёт в URL после **?**, указываемого после последнего слэша) *search=искомое_имя_или_его_часть*


  - Группы:
    - Просмотр списка сообществ: **GET**-запрос на адрес `http://127.0.0.1:8000/api/v1/groups/`.
    - Просмотр конкретного сообщества: **GET**-запрос на адрес `http://127.0.0.1:8000/api/v1/groups/{номер_сообщества}/`.

### Установка
Как запустить проект:
Клонировать репозиторий и запустить его в командной строке:
```
git clone https://github.com/orel333?tab=repositories
```

Зайти в папку с проектом - корневой каталог, находясь в нём, создать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```

Обновить версию pip

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла *requirements.txt*:
```
pip install -r requirements.txt
```

Зайти в папку проекта (которая содержит файл *manage.py*)
Выполнить миграции:
```
python manage.py migrate
```

Запустить проект:
```
python manage.py runserver
```

### Примеры:
Получаем токен:
```
POST http://127.0.0.1:8000/api/v1/jwt/create/
Content-Type: application/json

{
    "username": "Hunk",
    "password": "some0990"
}
```
Ответ:
```
200 OK
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0Mzc5NzM0OSwianRpIjoiZWNiY2RlYmIwMTNjNDA5NWFhNDY2ZjY3YzczN2MwZDMiLCJ1c2VyX2lkIjo1fQ.szixudq4h0xe0hbQDrr-sRfWNxs6qP8_aMlegrqyXK4",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzNzExMjQ5LCJqdGkiOiI2MDU2NjQ4ODM5YTY0NTI4YTBjMDk0OGE0NDk5ODc0MSIsInVzZXJfaWQiOjV9.H5t6o3FevmOkpzpzrrKwfkuq_LdI-k4_soVDB6W1G0g"
}
```

Создаём публикацию:
```
POST http://127.0.0.1:8000/api/v1/posts/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl9k94BlIjoiYWNjZXNzIiwiZXhwIjoxNjQzNzQwODY0LCJqdGkik94iZGE1OTIwZjM5NDI0NzcwOWQxODYzMzExNTU0NTlkZiIsInVzZXJfaWQiOjV9.AxKHmWFC-_V8dGbkKzsnyb28zaA5bizjfNBLPvSI6TE

{
    "text": "This new day and a new post",
    "image": null,
    "group": 2
}
```
Ответ:
```
201 Created
{
  "id": 28,
  "author": "Hunk",
  "text": "This new day and a new post",
  "pub_date": "2022-02-01T18:36:43.952786Z",
  "image": null,
  "group": 2
}
```

Получаем список из 3-х публикаций начиная с 3-го (пропустив 2; в базе 10 публикаций с содержанием **Тестовый пост _номер_**):
```
GET http://127.0.0.1:8000/api/v1/posts/?limit=3&offset=2
```
Ответ:
```
200 OK
{
  "count": 10,
  "next": "http://127.0.0.1:8000/api/v1/posts/?limit=3&offset=5",
  "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=3",
  "results": [
    {
      "id": 38,
      "author": "Hunk",
      "text": "Тестовый пост 3",
      "pub_date": "2022-02-02T11:58:19.174308Z",
      "image": null,
      "group": null
    },
    {
      "id": 39,
      "author": "Hunk",
      "text": "Тестовый пост 4",
      "pub_date": "2022-02-02T11:58:23.939083Z",
      "image": null,
      "group": null
    },
    {
      "id": 40,
      "author": "Hunk",
      "text": "Тестовый пост 5",
      "pub_date": "2022-02-02T11:58:28.173730Z",
      "image": null,
      "group": null
    }
  ]
}
```

Подписываемся на интересного автора:
```
POST http://127.0.0.1:8000/api/v1/follow/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl9k94BlIjoiYWNjZXNzIiwiZXhwIjoxNjQzNzQwODY0LCJqdGkik94iZGE1OTIwZjM5NDI0NzcwOWQxODYzMzExNTU0NTlkZiIsInVzZXJfaWQiOjV9.AxKHmWFC-_V8dGbkKzsnyb28zaA5bizjfNBLPvSI6TE

{
    "following": "Alien"
}
```
Ответ:
```
201 Created
{
  "user": "Hunk",
  "following": "Alien"
}
```

Ищем подписки по части имени автора (есть подписки на авторов: Man, Woman, Batman, Alien):
```
GET http://127.0.0.1:8000/api/v1/follow/?search=man
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl9k94BlIjoiYWNjZXNzIiwiZXhwIjoxNjQzNzQwODY0LCJqdGkik94iZGE1OTIwZjM5NDI0NzcwOWQxODYzMzExNTU0NTlkZiIsInVzZXJfaWQiOjV9.AxKHmWFC-_V8dGbkKzsnyb28zaA5bizjfNBLPvSI6TE
```

Ответ:
```
200 OK
[
  {
    "user": "Hunk",
    "following": "Batman"
  },
  {
    "user": "Hunk",
    "following": "Man"
  },
  {
    "user": "Hunk",
    "following": "Woman"
  }
]
```

Создаём комментарий к публикации:
```
POST http://127.0.0.1:8000/api/v1/posts/28/comments/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBgh8oiYWNlo4NzIiwiZXhwIjoxNjQzNzQxMTM2LCJqdGkiOiI4NTNmNzlkZTlkMzQ0NTZhYTg2YWQ1YmU0OTQ2ZmI4NyIsInVzZXJfaWQiOjR9.MP3DxwhV6-KiJCABLDLRC2VcVOsnC3QWy4_yU70wOO8

{
    "text": "I'm your fan!"
}
```
Ответ:
```
201 Created
{
  "id": 4,
  "author": "Alien",
  "text": "I'm your fan!",
  "created": "2022-02-01T18:40:51.635407Z",
  "post": 28
}
```

Корректируем комментарий к публикации (доступно только автору комментария):
```
PATCH http://127.0.0.1:8000/api/v1/posts/28/comments/4/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBgh8oiYWNlo4NzIiwiZXhwIjoxNjQzNzQxMTM2LCJqdGkiOiI4NTNmNzlkZTlkMzQ0NTZhYTg2YWQ1YmU0OTQ2ZmI4NyIsInVzZXJfaWQiOjR9.MP3DxwhV6-KiJCABLDLRC2VcVOsnC3QWy4_yU70wOO8

{
    "text": "Bo-oring!"
}
```
Ответ:
```
200 OK
{
  "id": 4,
  "author": "Alien",
  "text": "Bo-oring!",
  "created": "2022-02-01T18:40:51.635407Z",
  "post": 28
}
```

Удаляем комментарий к публикации (доступно только автору комментария):
```
DELETE http://127.0.0.1:8000/api/v1/posts/28/comments/4/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBgh8oiYWNlo4NzIiwiZXhwIjoxNjQzNzQxMTM2LCJqdGkiOiI4NTNmNzlkZTlkMzQ0NTZhYTg2YWQ1YmU0OTQ2ZmI4NyIsInVzZXJfaWQiOjR9.MP3DxwhV6-KiJCABLDLRC2VcVOsnC3QWy4_yU70wOO8
```
Ответ (*No content* - подтверждение удаления):
```
204 No Content
```

[^1]: Этот и другие значения ключей тела запроса, отмеченные сноской с цифрой 1, должны передаваться в двойных кавычках.
[^2]: Этот и другие запросы, отмеченные сноской с цифрой 2, должны передаваться со словом Bearer и access-токеном в заголовке запроса после ключа Authorization: (ключ и Bearer с токеном - без двойных кавычек).
