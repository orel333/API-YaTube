### ��������
API-������ ���������� ���������� ���� **Yatube**.
������ ������ ��������� ����� ����������� HTTP ������� ��������� ��������� �������:

#### ![����������� ��������������������� ������������](https://cdn2.scratch.mit.edu/get_image/user/60928233_60x60.png) ��� �������������������� �������������:
  - ����������:
    - �������� ������ ����������: **GET**-������ �� ����� `http://127.0.0.1:8000/api/v1/posts/`, ������������� ��������� (��������� ��������� ���������� �� ��������) �� ���������� ������� (���� � URL ����� **?**) *limit=�����* (���������� ��������� �� ����� ����������) � *offset=�����*(� ����� ���������� �������� �����).
    - �������� ���������� ����������: **GET**-������ �� ����� `http://127.0.0.1:8000/api/v1/posts/{�����_����������}/`.
  - ����������� � ������:
    - �������� ������ ������������ � �����: **GET**-������ �� ����� `http://127.0.0.1:8000/api/v1/posts/{�����_����������}/comments/`.
    - �������� ����������� � �����: **GET**-������ �� ����� `http://127.0.0.1:8000/api/v1/posts/{�����_�����}/comments/{�����_�����������}/`.
  - ������:
    - �������� ������ ���������: **GET**-������ �� ����� `http://127.0.0.1:8000/api/v1/groups/`.
    - �������� ����������� ����������: **GET**-������ �� ����� `http://127.0.0.1:8000/api/v1/groups/{�����_����������}/`.
    
#### ![����������� ������������������� ������������](https://yumtrade.ru/35929-33226-medium/modul-verifikacija-lic.jpg) ��� ������������������ �������������:
  - �����:
    - ��������� ������: **POST**-������ �� ����� `http://127.0.0.1:8000/api/v1/jwt/create/` � ��������� ����� ������������������� ������������[^1] �� ����� `username` � ��� ������[^1] �� ����� `password`; ����� ����� ��������� ***access-�����*** (������������ ��� ���������� ��������, ��������� ����������� [�������� ����� ����������]) � ***refresh-�����*** (������������ ��� ���������� access-������).
    - ���������� ������: **POST**-������ �� ����� `http://127.0.0.1:8000/api/v1/jwt/refresh/` � ��������� � ���� ������� ***refresh-������***[^1] �� ����� `"refresh"`.
    - �������� ������[^2]: **POST**-������ �� ����� `http://127.0.0.1:8000/api/v1/jwt/verify/` � ��������� � ���� ������� ������������ ***access-***[^1] ���� ***refresh-������***[^1] �� ����� `"token"`.
  - ����������:
    - �������� ������ ����������: **GET**-������ �� ����� `http://127.0.0.1:8000/api/v1/posts/`, ������������� ��������� (��������� ��������� ���������� �� ��������) �� ���������� ������� (���� � URL ����� **?**, ������������ ����� ���������� �����) *limit=�����* (���������� ��������� �� ����� ����������) � *offset=�����*(� ����� ���������� �������� �����).
    - �������� ���������� ����������: **GET**-������ �� ����� `http://127.0.0.1:8000/api/v1/posts/{�����_����������}/`.
    - ���������� �����[^2] **POST**-������ �� ����� `http://127.0.0.1:8000/api/v1/posts/` � ��������� � ���� ������� ������ �� ����������[^1]:
      - `"text"` - ������ ��������;
      - `"image"` - ������ �������� ��� *null*(������) - �������������� ����;
      - `"group"` - ����������������� (*id*) ����� ���������� - �������������� ����.
    - ��������� ����� ����������[^2]: **PATCH**- (��� ��������� ���������) ��� **PUT**-������ (��� ������� ���������) �� ����� `http://127.0.0.1:8000/api/v1/posts/{�����_����������}/` � ��������� � ���� ������� ������ �� ����������[^1] ���������� �����:
      - `"text"` - ������ ��������;
      - `"image"` - ������ �������� ��� *null*(������);
      - `"group"` - ����������������� (*id*) ����� ����������.     
    - �������� ����� ����������[^2]: **DELETE**-������ �� ����� `http://127.0.0.1:8000/api/v1/posts/{�����_����������}/`.
  - ����������� � �����������:
    - �������� ������ ������������ � ����������: **GET**-������ �� ����� `http://127.0.0.1:8000/api/v1/posts/{�����_����������}/comments/`.
    - �������� ����������� ����������� � ����������: **GET**-������ �� ����� `http://127.0.0.1:8000/api/v1/posts/{�����_����������}/comments/{�����_�����������}/`.
    - ��������� ����������� � ����������[^2]: **POST**-������ �� ����� `http://127.0.0.1:8000/api/v1/posts/{�����_����������}/comments/` � ��������� � ���� ������� ������[^1] �� ����� `"text"`.
    - ��������� ������ ����������� � ����������[^2]: **PATCH**- (��� ��������� ���������) ��� **PUT**-������ (��� ������� ���������) �� ����� `http://127.0.0.1:8000/api/v1/posts/{�����_����������}/comments/{�����_�����������}/` � ��������� � ���� ������� ������[^1] �� ����� `"text"`.
    - �������� ������ ����������� � ����������[^2]: **DELETE**-������ �� ����� `http://127.0.0.1:8000/api/v1/posts/{�����_����������}/comments/{�����_�����������}/`.
  - �������� �� �������:
    - ��������� �������� �� ������[^2]: **POST**-������ �� ����� `http://127.0.0.1:8000/api/v1/follow/` � ��������� � ���� ������� ����� ������[^1] �� ����� `"following"`.
    - ��������� �������� ������������, ������������� ������: **GET**-������ �� ����� `http://127.0.0.1:8000/api/v1/follow/`; ������������ ����� �������� �� ����� ������, �� �������� �������� ������������, ������������� ����� �������� ������� (��� � URL ����� **?**, ������������ ����� ���������� �����) *search=�������_���_���_���_�����*


  - ������:
    - �������� ������ ���������: **GET**-������ �� ����� `http://127.0.0.1:8000/api/v1/groups/`.
    - �������� ����������� ����������: **GET**-������ �� ����� `http://127.0.0.1:8000/api/v1/groups/{�����_����������}/`.

### ���������
��� ��������� ������:
����������� ����������� � ��������� ��� � ��������� ������:
```
git clone https://github.com/orel333?tab=repositories
```

����� � ����� � �������� - �������� �������, �������� � ��, ������� � ������������ ����������� ���������:
```
python -m venv venv
source venv/Scripts/activate
```

�������� ������ pip

```
python3 -m pip install --upgrade pip
```

���������� ����������� �� ����� *requirements.txt*:
```
pip install -r requirements.txt
```

����� � ����� ������� (������� �������� ���� *manage.py*)
��������� ��������:
```
python manage.py migrate
```

��������� ������:
```
python manage.py runserver
```

### �������:
�������� �����:
```
POST http://127.0.0.1:8000/api/v1/jwt/create/
Content-Type: application/json

{
    "username": "Hunk",
    "password": "some0990"
}
```
�����:
```
200 OK
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0Mzc5NzM0OSwianRpIjoiZWNiY2RlYmIwMTNjNDA5NWFhNDY2ZjY3YzczN2MwZDMiLCJ1c2VyX2lkIjo1fQ.szixudq4h0xe0hbQDrr-sRfWNxs6qP8_aMlegrqyXK4",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzNzExMjQ5LCJqdGkiOiI2MDU2NjQ4ODM5YTY0NTI4YTBjMDk0OGE0NDk5ODc0MSIsInVzZXJfaWQiOjV9.H5t6o3FevmOkpzpzrrKwfkuq_LdI-k4_soVDB6W1G0g"
}
```

������ ����������:
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
�����:
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

�������� ������ �� 3-� ���������� ������� � 3-�� (��������� 2; � ���� 10 ���������� � ����������� **�������� ���� _�����_**):
```
GET http://127.0.0.1:8000/api/v1/posts/?limit=3&offset=2
```
�����:
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
      "text": "�������� ���� 3",
      "pub_date": "2022-02-02T11:58:19.174308Z",
      "image": null,
      "group": null
    },
    {
      "id": 39,
      "author": "Hunk",
      "text": "�������� ���� 4",
      "pub_date": "2022-02-02T11:58:23.939083Z",
      "image": null,
      "group": null
    },
    {
      "id": 40,
      "author": "Hunk",
      "text": "�������� ���� 5",
      "pub_date": "2022-02-02T11:58:28.173730Z",
      "image": null,
      "group": null
    }
  ]
}
```

������������� �� ����������� ������:
```
POST http://127.0.0.1:8000/api/v1/follow/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl9k94BlIjoiYWNjZXNzIiwiZXhwIjoxNjQzNzQwODY0LCJqdGkik94iZGE1OTIwZjM5NDI0NzcwOWQxODYzMzExNTU0NTlkZiIsInVzZXJfaWQiOjV9.AxKHmWFC-_V8dGbkKzsnyb28zaA5bizjfNBLPvSI6TE

{
    "following": "Alien"
}
```
�����:
```
201 Created
{
  "user": "Hunk",
  "following": "Alien"
}
```

���� �������� �� ����� ����� ������ (���� �������� �� �������: Man, Woman, Batman, Alien):
```
GET http://127.0.0.1:8000/api/v1/follow/?search=man
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl9k94BlIjoiYWNjZXNzIiwiZXhwIjoxNjQzNzQwODY0LCJqdGkik94iZGE1OTIwZjM5NDI0NzcwOWQxODYzMzExNTU0NTlkZiIsInVzZXJfaWQiOjV9.AxKHmWFC-_V8dGbkKzsnyb28zaA5bizjfNBLPvSI6TE
```

�����:
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
```

������ ����������� � ����������:
```
POST http://127.0.0.1:8000/api/v1/posts/28/comments/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBgh8oiYWNlo4NzIiwiZXhwIjoxNjQzNzQxMTM2LCJqdGkiOiI4NTNmNzlkZTlkMzQ0NTZhYTg2YWQ1YmU0OTQ2ZmI4NyIsInVzZXJfaWQiOjR9.MP3DxwhV6-KiJCABLDLRC2VcVOsnC3QWy4_yU70wOO8

{
    "text": "I'm your fan!"
}
```
�����:
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

������������ ����������� � ���������� (�������� ������ ������ �����������):
```
PATCH http://127.0.0.1:8000/api/v1/posts/28/comments/4/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBgh8oiYWNlo4NzIiwiZXhwIjoxNjQzNzQxMTM2LCJqdGkiOiI4NTNmNzlkZTlkMzQ0NTZhYTg2YWQ1YmU0OTQ2ZmI4NyIsInVzZXJfaWQiOjR9.MP3DxwhV6-KiJCABLDLRC2VcVOsnC3QWy4_yU70wOO8

{
    "text": "Bo-oring!"
}
```
�����:
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

������� ����������� � ���������� (�������� ������ ������ �����������):
```
DELETE http://127.0.0.1:8000/api/v1/posts/28/comments/4/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBgh8oiYWNlo4NzIiwiZXhwIjoxNjQzNzQxMTM2LCJqdGkiOiI4NTNmNzlkZTlkMzQ0NTZhYTg2YWQ1YmU0OTQ2ZmI4NyIsInVzZXJfaWQiOjR9.MP3DxwhV6-KiJCABLDLRC2VcVOsnC3QWy4_yU70wOO8
```
����� (*No content* - ������������� ��������):
```
204 No Content
```

[^1]: ���� � ������ �������� ������ ���� �������, ���������� ������� � ������ 1, ������ ������������ � ������� ��������.
[^2]: ���� � ������ �������, ���������� ������� � ������ 2, ������ ������������ �� ������ Bearer � access-������� � ��������� ������� ����� ����� Authorization: (���� � Bearer � ������� - ��� ������� �������).