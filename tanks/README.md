# Соревнования ботов

## Структура бота

Бот представляет собой программу на языке Python 3.

Файл с кодом должен содержать функцию **make_choice** принимающую ровно три аргумента.

Перед каждым ходом тестирующая система передаст в функцию три параметра - координаты бота на карте (x,y) и матрицу с информацией о других игроках.

В итоге функция должна вернуть в точку вызова строку - решение, что делать боту в **текущем** ходе.

```python
def make_choice(x,y,field):
    #произвольный код
```

## Возвращаемые значения

При каждом запуске функция должна выбрать одно из восьми действий - передвижение на одну клетку в одну из четырех сторон, либо стрельба в одном из четырех направлений.

Для этого функция make_choice должна вернуть одну из следующих строк: **"fire_up", "fire_down", "fire_left", "fire_right", "go_up","go_down","go_left","go_right"**.

Выстрел поражает только одного противника, но на произвольном расстоянии.

```python
def make_choice(x,y,field):
    import random

def make_choice(x,y,field):
    actions = ["fire_up", "fire_down",
               "fire_left", "fire_right", 
               "go_up","go_down",
               "go_left","go_right"]
    return random.choice(actions)
```

## Принимаемые параметры

Функция make_choice принимает три параметра - координаты танка по осям x и y, а также матрицу игры.

Матрица игры содержит информацию о:
  - Расположении игроков на карте.
  - Текущем уровне жизни всех игроков.
  - Истории ходов каждого игрока с начала игры.

Физически матрица представляет собой список списков, в которых содержится либо ноль, либо словарь из двух элементов -  очки здоровья бота ('life') стоящего в этой клетке и история его ходов ('history').

  - **Как узнать, сколько жизни осталось у собственного бота?**
  - field[x][y]['life']

История ходов - список ранее отданных команд, т.е. строк вида "go_right".
  - **Как узнать, какие команды были отданы нашим ботом ранее?**
  - field[x][y]['history']

Первая координата в матрице - это значение по оси X, а вторая по оси Y. Левый верхний угол карты - это точка field[0][0]. Правый нижний угол карты - это точка field[x_size][y_size], где x_size = len(field), y_size = len(field[0]).

## Примеры
 - **go_right_bot.py** - в любой ситуации данная программа будет выдавать команду на движение в право в независимости от каких либо внешних условий.
 - **fire_right_bot.py** - аналогичный пример — всегда стреляем вверх.
 - **random_bot.py** - каждый раз выбирает случайное действие.
 - **right_corner_bot.py** - идем в правый нижний угол и отстреливаемся.
 - **find_target_bot.py** - стреляем, только если видим на линии противника, иначе идем в случайную сторону.
 - **life_check_bot.py** - когда здоровья мало - убегаем.
 - **history_circle_bot.py** - используем историю ходов и стреляем по кругу.
