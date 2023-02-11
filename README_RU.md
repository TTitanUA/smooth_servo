# Smooth Servo Library
Эта библиотека представляет собой набор вариантов замедлений для моих библиотек сервоприводов.
Так как данный функционал не является обязательным, то я решил вынести его в отдельную библиотеку.

Возможности библиотеки:
- Позволяет создавать итераторы на основании: значения, времени, жалеемого замедления.


Материалы использованные для создания библиотеки:
- Material [CSS Transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function), by MDN
- Material [easings.net](https://easings.net/en) by Andrey Sitnik and Ivan Solovev

### Совместимость
- MicroPython 1.19.1
- Raspberry Pi Pico

On the hardware above the library has been tested and works correctly.

### ВНИМАНИЕ
Вы используете данный модуль на свой страх и риск. 
Я новичок в программировании на MicroPython. Так что могут быть нюансы, которые я не учел.
Если вы заметили ошибку или у вас есть предложения по улучшению, то пишите в Issues.

## Contents
- [Установка](https://github.com/TTitanUA/servo_smooth#install)
- [Использование](https://github.com/TTitanUA/servo_smooth#init)
- [Документация](https://github.com/TTitanUA/servo_smooth#doc)
- [Баги и обратная связь](https://github.com/TTitanUA/servo_smooth#feedback)

<a id="install"></a>
## Установка
- Библиотеку установить через pip (Thonny -> Manage Packages) по названию **smooth-servo** 
- Или ручная установка:
  - [Скачать библиотеку с GitHub](https://github.com/TTitanUA/servo_smooth) 
  - забрать папку **smooth_servo** из архива.
  - загрузить в корень микроконтроллера или в папку **lib**.

<a id="init"></a>
## Использование
Данная библиотека в первую очередь рассчитана на использование на использование вместе с моими библиотеками сервоприводов.
Но вы можете использовать ее и в других проектах следующим образом:

```python
from smooth_servo import SmoothLinear

# Задаем параметры
value = 100  # Конечное значение которое должен достичь итератор
time_ms = 1000  # Время в миллисекундах за которое должен достичь конечного значения
start_value = 0  # Начальное значение
tick_time_ms = 50  # Время между итерациями (служит для расчета количества шагов)

# Создаем экземпляр класса итератора
linear = SmoothLinear(value, time_ms, start_value)

# создаем итератор с заданным временем между итерациями
iterator = linear.generate(tick_time_ms)

# Используем итератор
for i in iterator:
    print(i)
```

<a id="doc"></a>
## Документация
### Параметры конструктора

| Parameter   | Type | Default | Description                                                        |
|-------------|------|---------|--------------------------------------------------------------------|
| value       | int  | None    | Конечное значение                                                  |
| time_ms     | int  | None    | Время в миллисекундах за которое должен достичь конечного значения |
| start_value | int  | 0       | Начальное значение                                                 |

- `value` - не может быть равным или меньше 0.
- `time_ms` - не может быть равным или меньше 0.
- `start_value` - не может быть больше `value`.

### Классы итераторов

| Class                | Easing type    | Description                                     |
|----------------------|----------------|-------------------------------------------------|
| ServoSmoothBase      | None           | Базовый класс для итераторов                    |
| SmoothLinear         | Linear         | Линейная зависимость значения от времени.        |
| SmoothEaseIn         | EaseIn         | [Пример](https://easings.net/en#easeInSine)     |
| SmoothEaseOut        | EaseOut        | [Пример](https://easings.net/en#easeOutSine)    |
| SmoothEaseInOut      | EaseInOut      | [Пример](https://easings.net/en#easeInOutSine)  |
| SmoothEaseInQuad     | EaseInQuad     | [Пример](https://easings.net/en#easeInQuad)     |
| SmoothEaseOutQuad    | EaseOutQuad    | [Пример](https://easings.net/en#easeOutQuad)    |
| SmoothEaseInOutQuad  | EaseInOutQuad  | [Пример](https://easings.net/en#easeInOutQuad)  |
| SmoothEaseInCubic    | EaseInCubic    | [Пример](https://easings.net/en#easeInCubic)    |
| SmoothEaseOutCubic   | EaseOutCubic   | [Пример](https://easings.net/en#easeOutCubic)   |
| SmoothEaseInOutCubic | EaseInOutCubic | [Пример](https://easings.net/en#easeInOutCubic) |
| SmoothEaseInQuart    | EaseInQuart    | [Пример](https://easings.net/en#easeInQuart)    |
| SmoothEaseOutQuart   | EaseOutQuart   | [Пример](https://easings.net/en#easeOutQuart)   |
| SmoothEaseInOutQuart | EaseInOutQuart | [Пример](https://easings.net/en#easeInOutQuart) |
| SmoothEaseInQuint    | EaseInQuint    | [Пример](https://easings.net/en#easeInQuint)    |
| SmoothEaseOutQuint   | EaseOutQuint   | [Пример](https://easings.net/en#easeOutQuint)   |
| SmoothEaseInOutQuint | EaseInOutQuint | [Пример](https://easings.net/en#easeInOutQuint) |
| SmoothEaseInExpo     | EaseInExpo     | [Пример](https://easings.net/en#easeInExpo)     |
| SmoothEaseOutExpo    | EaseOutExpo    | [Пример](https://easings.net/en#easeOutExpo)    |
| SmoothEaseInOutExpo  | EaseInOutExpo  | [Пример](https://easings.net/en#easeInOutExpo)  |
| SmoothEaseInCirc     | EaseInCirc     | [Пример](https://easings.net/en#easeInCirc)     |
| SmoothEaseOutCirc    | EaseOutCirc    | [Пример](https://easings.net/en#easeOutCirc)    |
| SmoothEaseInOutCirc  | EaseInOutCirc  | [Пример](https://easings.net/en#easeInOutCirc)  |
| SmoothEaseInBack     | EaseInBack     | [Пример](https://easings.net/en#easeInBack)     |
| SmoothEaseOutBack    | EaseOutBack    | [Пример](https://easings.net/en#easeOutBack)    |
| SmoothEaseInOutBack  | EaseInOutBack  | [Пример](https://easings.net/en#easeInOutBack)  |

<a id="feedback"></a>
## Баги и обратная связь
При нахождении багов создавайте [issue](https://github.com/TTitanUA/servo_smooth/issues).
Библиотека открыта для доработки и ваших [pull запросов](https://github.com/TTitanUA/servo_smooth/pulls).
