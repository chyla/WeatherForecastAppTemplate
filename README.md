# Weather Forecast App Template

This is the template of Weather Forecast App. You can train your Python 3 developer skills by adding new functionalities. The list of ideas can be found below.

## Screenshots

![alt text](https://github.com/chyla/WeatherForecastAppTemplate/raw/master/screenshots/screenshot1.gif "Main window")

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need:

* Python 3 with Tk
* Pillow library

### Installing

When using PyCharm environment [follow the instructions and install Pillow library](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html).

You can also use pip with virtualenv:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Deployment

Run this app with Python 3:

```bash
python3 main.py
```

## Ideas for future development

- Unittest your app (use TDD with unittest or pytest, mock, tox).
- Use web service to receive list of supported cities and weather data (eg. https://openweathermap.org/).
- Remember to catch errors and notify user about them in a nice way.
- Use local storage to cache the data (eg. text file, database like SQLite).
- Add forecast for next days.
- Add tray icon.
- Notify user about bad weather conditions (eg. via Facebook, Twitter, SMS or simple desktop notification).
- Prepare an installer for your app with Distutils (setup.py).
- Prepare standalone version for Windows users (eg. py2exe, PyInstaller).

## Authors

* **Adam Chyła** - *Initial work* - [chyla.org](https://chyla.org/blog/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [Weather Icons by Alex M.](https://opengameart.org/content/weather-icons) - [License: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

