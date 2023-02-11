This is an automatic translation, may be incorrect in some places.
# Smooth Servo Library
This library is a collection of deceleration options for my servo libraries.
Since this functionality is not mandatory, I decided to move it to a separate library.

Library features:
- Allows you to create iterators based on: value, time, regrettable slowdown.


Materials used to create the library:
- Material [CSS Transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function), by MDN
- Material [easings.net](https://easings.net/en) by Andrey Sitnik and Ivan Solovev

### Compatibility
- MicroPython 1.19.1
- Raspberry Pi Pico

On the hardware above the library has been tested and works correctly.

### ATTENTION
You use this module at your own risk.
I am new to MicroPython programming. So there may be nuances that I did not take into account.
If you notice an error or have suggestions for improvement, please write to Issues.

## Contents
- [Install](https://github.com/TTitanUA/servo_smooth#install)
- [Initialization](https://github.com/TTitanUA/servo_smooth#init)
- [Documentation](https://github.com/TTitanUA/servo_smooth#doc)
- [Bugs and feedback](https://github.com/TTitanUA/servo_smooth#feedback)

<a id="install"></a>
## Installation
- Install the library via pip (Thonny -> Manage Packages) by name **smooth-servo**
- Or manual installation:
   - [Download library from GitHub](https://github.com/TTitanUA/servo_smooth)
   - take the **smooth_servo** folder from the archive.
   - upload to the root of the microcontroller or to the **lib** folder.

<a id="init"></a>
## Usage
This library is primarily designed to be used with my servo libraries.
But you can also use it in other projects like this:

```python
from smooth_servo import SmoothLinear

# Set parameters
value = 100  # End value the iterator should reach
time_ms = 1000  # Time in milliseconds to reach end value
start_value = 0  # Start value
tick_time_ms = 50  # Time between iterations (used to calculate the number of steps)

# Create an instance of the iterator class
linear = SmoothLinear(value, time_ms, start_value)

# create an iterator with a given time between iterations
iterator = linear.generate(tick_time_ms)

# Use an iterator
for i in iterator:
    print(i)
```

<a id="doc"></a>
## Documentation
### Constructor parameters

| Parameter   | type | default | description                                                |
|-------------|------|---------|------------------------------------------------------------|
| value       | int  | None    | End value                                                  |
| time_ms     | int  | None    | The time in milliseconds it takes to reach the final value |
| start_value | int  | 0       | Initial value                                              |

- `value` - cannot be equal to or less than 0.
- `time_ms` - cannot be equal to or less than 0.
- `start_value` - cannot be greater than `value`.

### Iterator classes

| Class                | Easing type    | Description                                      |
|----------------------|----------------|--------------------------------------------------|
| ServoSmoothBase      | None           | Base class for iterators                         |
| SmoothLinear         | Linear         | Linear dependence of value on time.              |
| SmoothEaseIn         | EaseIn         | [Example](https://easings.net/en#easeInSine)     |
| SmoothEaseOut        | EaseOut        | [Example](https://easings.net/en#easeOutSine)    |
| SmoothEaseInOut      | EaseInOut      | [Example](https://easings.net/en#easeInOutSine)  |
| SmoothEaseInQuad     | EaseInQuad     | [Example](https://easings.net/en#easeInQuad)     |
| SmoothEaseOutQuad    | EaseOutQuad    | [Example](https://easings.net/en#easeOutQuad)    |
| SmoothEaseInOutQuad  | EaseInOutQuad  | [Example](https://easings.net/en#easeInOutQuad)  |
| SmoothEaseInCubic    | EaseInCubic    | [Example](https://easings.net/en#easeInCubic)    |
| SmoothEaseOutCubic   | EaseOutCubic   | [Example](https://easings.net/en#easeOutCubic)   |
| SmoothEaseInOutCubic | EaseInOutCubic | [Example](https://easings.net/en#easeInOutCubic) |
| SmoothEaseInQuart    | EaseInQuart    | [Example](https://easings.net/en#easeInQuart)    |
| SmoothEaseOutQuart   | EaseOutQuart   | [Example](https://easings.net/en#easeOutQuart)   |
| SmoothEaseInOutQuart | EaseInOutQuart | [Example](https://easings.net/en#easeInOutQuart) |
| SmoothEaseInQuint    | EaseInQuint    | [Example](https://easings.net/en#easeInQuint)    |
| SmoothEaseOutQuint   | EaseOutQuint   | [Example](https://easings.net/en#easeOutQuint)   |
| SmoothEaseInOutQuint | EaseInOutQuint | [Example](https://easings.net/en#easeInOutQuint) |
| SmoothEaseInExpo     | EaseInExpo     | [Example](https://easings.net/en#easeInExpo)     |
| SmoothEaseOutExpo    | EaseOutExpo    | [Example](https://easings.net/en#easeOutExpo)    |
| SmoothEaseInOutExpo  | EaseInOutExpo  | [Example](https://easings.net/en#easeInOutExpo)  |
| SmoothEaseInCirc     | EaseInCirc     | [Example](https://easings.net/en#easeInCirc)     |
| SmoothEaseOutCirc    | EaseOutCirc    | [Example](https://easings.net/en#easeOutCirc)    |
| SmoothEaseInOutCirc  | EaseInOutCirc  | [Example](https://easings.net/en#easeInOutCirc)  |
| SmoothEaseInBack     | EaseInBack     | [Example](https://easings.net/en#easeInBack)     |
| SmoothEaseOutBack    | EaseOutBack    | [Example](https://easings.net/en#easeOutBack)    |
| SmoothEaseInOutBack  | EaseInOutBack  | [Example](https://easings.net/en#easeInOutBack)  |

<a id="feedback"></a>
## Bugs and feedback
Create an [issue](https://github.com/TTitanUA/servo_smooth/issues) when you find bugs.
The library is open for revision and your [pull requests](https://github.com/TTitanUA/servo_smooth/pulls).
