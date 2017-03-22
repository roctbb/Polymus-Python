# Polymus-Python

## Занятие 1: Синстаксис Python и работа с Pillow
1. Установка Anaconda (**Python 3.5** + набор библиотек, включая Pillow): https://www.continuum.io/downloads
2. Изучаем Python 3:
  - https://docs.python.org/3/tutorial/ - официальное руководство (на английском)
  - https://pythonworld.ru/samouchitel-python - tutorial на русском
  - Марк Лутц. Изучаем Python, 4-е издание. - полноценный и подробный учебник
  - https://habrahabr.ru/post/150302/ - подборка материалов
3. Работа с библиотекой Pillow (форк PIL - Python Image Library):
  - https://pillow.readthedocs.io/en/4.0.x/handbook/tutorial.html - документация
  - Примеры c занятия - в папке pillow
  - https://habrahabr.ru/post/142818/ - материал со звездочкой, размытие, резкость и тд.

**ДЗ: Фотофильтр на Python. Запрашивает откуда брать фотографию и куда сохранять, алгоритм не должен зависеть от размеров.**

## Занятие 2: Обработка аудиоданных и использование PyAudio
1. Документация по PyAudio - https://people.csail.mit.edu/hubert/pyaudio/
2. Структура и содержимое wav файла (с кодом на СИ) - http://audiocoding.ru/article/2008/05/22/wav-file-structure.html
3. Еще про кодирование звука: [Википедия](https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%B7%D0%B2%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B9_%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%B8)
4. Работа с микрофоном, динамиками, запись и обработка файлов + немного теории - в [примерах с комментариями](https://github.com/roctbb/Polymus-Python/tree/master/audio).

**ДЗ: Дописать софт для "хрюши-повторюши". Программа записывает человека, когда он говорит и как только он замолкает, поднимает частоту записи и воспроизводит. После этого снова пишет по кругу. - 10 баллов. Идеи для доработки: накладывать фоном какой нибудь бит.**

## Занятие 3: Функции, обработка ошибок и танки

1. Функции в Python.
2. Механизм try-except.
3. Написание алгоритма для танка:
  - Документация и примеры: [roctbb.net](http://roctbb.net) и папка tanks
  - Тестирующая система: [roctbb.net:8888](http://roctbb.net:8888)
  - Прямой эфир: [roctbb.net:8888/game](http://roctbb.net:8888/game)
  - Статистика: [roctbb.net:8888/stats](http://roctbb.net:8888/stats)

**ДЗ: Подготовиться к соревнованию танков.**

## Занятие 4: Веб-сервер Tornado

1. Общая схема работы по HTTP - [https://habrahabr.ru/post/215117/](https://habrahabr.ru/post/215117/).
2. Язык разметки HTML:
  - [http://htmlbook.ru/samhtml](самоучитель htmlbook.ru)
  - [https://www.codecademy.com/learn/web](Интерактивный курс на CodeAcademy)
  - [http://getbootstrap.com](HTML фреймфорк Bootstrap)
3. Веб-сервер Tornado:
  - [Документация](http://www.tornadoweb.org/en/stable/)

**ДЗ: Написать сайт, генерирующий случайные истории.**

## Занятие 5: POST запросы в Tornado, загрузка файлов

1. [Загрузка файлов в Tornado](http://stackoverflow.com/questions/11909397/how-to-upload-an-image-with-python-tornado-from-an-html-form)

**ДЗ: Написать сайт с несколькими фотофильтрами.**

## Занятие 6: Хранения данных в формате JSON, авторизация в Tornado

1. [Описание формата JSON](http://www.json.org/json-ru.html)
2. [Работа с файлами в Python](http://pythonicway.com/python-fileio)
3. [Синтаксис шаблонов Tornado](http://www.tornadoweb.org/en/stable/template.html)
4. [Tornado user authentication](http://www.tornadoweb.org/en/stable/guide/security.html)

**ДЗ: Написать блог с панелью администратора, доступной по паролю.**

## Занятие 7: NoSQL базы данных на примере MongoDB

1. [Tutroial по PyMongo](http://api.mongodb.com/python/current/tutorial.html)
2. [MLab - удобный хостинг для MongoDB (500 мб бесплатно)](https://mlab.com/)

**ДЗ: Добавить регистрацию и вход по логину и паролю в чат.**

## Занятие 8: Telegram-бот на Python
1. [Руководство по созданию ботов](https://www.gitbook.com/book/groosha/telegram-bot-lessons/details)

**ДЗ: Написать собственного бота в Telegram.**

## Занятие 8: Взаимодействие в внешними API
1. [Библиотека Requests - GET и POST запросы из Python](http://docs.python-requests.org/en/master/)
2. [microsoft cognitive services](https://www.microsoft.com/cognitive-services/en-us/apis)

**ДЗ: Фотофильтр, который использует распознавание лиц или зависит от настроения человека на фотографии.**
