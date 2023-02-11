from math import sin, pi as PI, cos, sqrt 


class ServoSmoothBase:
    """ Base class for servo smooth actions """
    def __init__(self, value: int, time_ms: int, start_value: int = 0):
        self._value = self.__normalize_value(value)
        self._time_ms = self.__normalize_time(time_ms)
        self._start_value = self.__normalize_start_value(value, start_value)

    def generate(self, tick_t_ms: int):
        yield 0

    @staticmethod
    def __normalize_start_value(value, s_v):
        return 0 if s_v < 0 or s_v > value else s_v
    
    @staticmethod
    def __normalize_value(value):
        if value <= 0:
            raise TypeError('Value must be greater than 0')
        return int(value)
    
    @staticmethod
    def __normalize_time(value):
        if value <= 0:
            raise TypeError('Time must be greater than 0')
        return int(value)


class SmoothLinear(ServoSmoothBase):
    """Simple linear smoother"""

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value

        _ss = (_t_ms // tick_t_ms)
        _s = _v / _ss

        for i in range(1, _ss):
            yield int(_s_v + _s * i)
        yield _e_v


class SmoothEaseIn(ServoSmoothBase):
    """ link https://easings.net/#easeInSine """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            yield int(_s_v + (1 - cos((i / _ss) * PI / 2)) * _v)
        yield _e_v


class SmoothEaseOut(ServoSmoothBase):
    """ link: https://easings.net/#easeOutSine """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            yield int(_s_v + sin(((i / _ss) * PI) / 2) * _v)
        yield _e_v


class SmoothEaseInOut(ServoSmoothBase):
    """ link: https://easings.net/#easeInOutSine """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            yield int(_s_v + (-(cos(PI * (i / _ss)) - 1) / 2) * _v)
        yield _e_v


class SmoothEaseInQuad(ServoSmoothBase):
    """ link: https://easings.net/#easeInQuad """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = i / _ss
            yield int(_s_v + (_x * _x) * _v)
        yield _e_v


class SmoothEaseOutQuad(ServoSmoothBase):
    """ link: https://easings.net/en#easeOutQuad """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (1 - i / _ss)
            yield int(_s_v + (1 - _x * _x) * _v)
        yield _e_v


class SmoothEaseInOutQuad(ServoSmoothBase):
    """ link: https://easings.net/en#easeInOutQuad """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (i / _ss)
            yield int(_s_v + (2 * _x * _x if _x < 0.5 else 1 - pow(-2 * _x + 2, 2) / 2) * _v)
        yield _e_v


class SmoothEaseInCubic(ServoSmoothBase):
    """ link: https://easings.net/#easeInCubic """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = i / _ss
            yield int(_s_v + (_x * _x * _x) * _v)
        yield _e_v


class SmoothEaseOutCubic(ServoSmoothBase):
    """ link: https://easings.net/en#easeOutCubic """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (1 - i / _ss)
            yield int(_s_v + (1 - pow(_x, 3)) * _v)
        yield _e_v


class SmoothEaseInOutCubic(ServoSmoothBase):
    """ link: https://easings.net/en#easeInOutCubic """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (i / _ss)
            yield int(_s_v + (4 * _x * _x * _x if _x < 0.5 else 1 - pow(-2 * _x + 2, 3) / 2) * _v)
        yield _e_v


class SmoothEaseInQuart(ServoSmoothBase):
    """ link: https://easings.net/#easeInQuart """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = i / _ss
            yield int(_s_v + (_x * _x * _x * _x) * _v)
        yield _e_v


class SmoothEaseOutQuart(ServoSmoothBase):
    """ link: https://easings.net/en#easeOutQuart """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (1 - i / _ss)
            yield int(_s_v + (1 - pow(_x, 4)) * _v)
        yield _e_v


class SmoothEaseInOutQuart(ServoSmoothBase):
    """ link: https://easings.net/en#easeInOutQuart """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (i / _ss)
            yield int(_s_v + (8 * _x * _x * _x * _x if _x < 0.5 else 1 - pow(-2 * _x + 2, 4) / 2) * _v)
        yield _e_v


class SmoothEaseInQuint(ServoSmoothBase):
    """ link: https://easings.net/#easeInQuint """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = i / _ss
            yield int(_s_v + (_x * _x * _x * _x * _x) * _v)
        yield _e_v


class SmoothEaseOutQuint(ServoSmoothBase):
    """ link: https://easings.net/en#easeOutQuint """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (1 - i / _ss)
            yield int(_s_v + (1 - pow(_x, 5)) * _v)
        yield _e_v


class SmoothEaseInOutQuint(ServoSmoothBase):
    """ link: https://easings.net/en#easeInOutQuint """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (i / _ss)
            yield int(_s_v + (16 * _x * _x * _x * _x * _x if _x < 0.5 else 1 - pow(-2 * _x + 2, 5) / 2) * _v)
        yield _e_v


class SmoothEaseInExpo(ServoSmoothBase):
    """ link: https://easings.net/#easeInExpo """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = i / _ss
            yield int(_s_v + (0 if _x == 0 else pow(2, 10 * _x - 10)) * _v)
        yield _e_v


class SmoothEaseOutExpo(ServoSmoothBase):
    """ link: https://easings.net/en#easeOutExpo """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (i / _ss)
            yield int(_s_v + (1 if _x == 1 else 1 - pow(2, -10 * _x)) * _v)
        yield _e_v


class SmoothEaseInOutExpo(ServoSmoothBase):
    """ link: https://easings.net/en#easeInOutExpo """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (i / _ss)
            if _x == 0:
                yield _s_v
            elif _x == 1:
                yield _e_v
            elif _x < 0.5:
                yield int(_s_v + (pow(2, 20 * _x - 10) / 2) * _v)
            else:
                yield int(_s_v + ((2 - pow(2, -20 * _x + 10)) / 2) * _v)
        yield _e_v


class SmoothEaseInCirc(ServoSmoothBase):
    """ link: https://easings.net/#easeInCirc """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = i / _ss
            yield int(_s_v + (1 - sqrt(1 - pow(_x, 2))) * _v)
        yield _e_v


class SmoothEaseOutCirc(ServoSmoothBase):
    """ link: https://easings.net/en#easeOutCirc """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (i / _ss)
            yield int(_s_v + (sqrt(1 - pow(_x - 1, 2))) * _v)
        yield _e_v


class SmoothEaseInOutCirc(ServoSmoothBase):
    """ link: https://easings.net/en#easeInOutCirc """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (i / _ss)
            if _x < 0.5:
                yield int(_s_v + ((1 - sqrt(1 - pow(2 * _x, 2))) / 2) * _v)
            else:
                yield int(_s_v + ((sqrt(1 - pow(-2 * _x + 2, 2)) + 1) / 2) * _v)
        yield _e_v


class SmoothEaseInBack(ServoSmoothBase):
    """ link: https://easings.net/#easeInBack """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)
        _c1 = 1.70158
        _c3 = _c1 + 1

        for i in range(1, _ss):
            _x = i / _ss
            yield int(_s_v + (_c3 * _x * _x * _x - _c1 * _x * _x) * _v)
        yield _e_v


class SmoothEaseOutBack(ServoSmoothBase):
    """ link: https://easings.net/en#easeOutBack """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)
        _c1 = 1.70158
        _c3 = _c1 + 1

        for i in range(1, _ss):
            _x = (i / _ss)
            yield int(_s_v + (1 + _c3 * pow(_x - 1, 3) + _c1 * pow(_x - 1, 2)) * _v)
        yield _e_v


class SmoothEaseInOutBack(ServoSmoothBase):
    """ link: https://easings.net/en#easeInOutBack """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)
        _c1 = 1.70158
        _c2 = _c1 * 1.525

        for i in range(1, _ss):
            _x = (i / _ss)
            if _x < 0.5:
                yield int(_s_v + ((pow(2 * _x, 2) * ((_c2 + 1) * 2 * _x - _c2)) / 2) * _v)
            else:
                yield int(_s_v + ((pow(2 * _x - 2, 2) * ((_c2 + 1) * (_x * 2 - 2) + _c2) + 2) / 2) * _v)
        yield _e_v
