
  <h3 align="center"> python-telegram-bot connect API beer_finder</h3>

### О проекте:
Beers Finder Bot (BFB) предназначен для поиска информации о пенных напитках, используемых
в проекте ```https://github.com/bycs/beer_finder```.
Коммуникация реализована по API.

### Используемый стек технологий в проекте:
* python-telegram-bot
* poetry
* pre-commit

### Перед запуском выполните:

* Виртуальное окружение:
  ```sh
  poetry config virtualenvs.in-project true
  poetry install
  ```
* pre-commit:
  ```sh
  pre-commit install
  ```
* В корне проекта создайте ```.env``` и задайте значения переменных:
    ```sh
    URL_API=#Replace 'URL_API' with beer_finder API.
    TOKEN=#Replace 'TOKEN' with your Bot's API token.
    ```
* Для запуска проекта, в корне проекта пропишите```python bot.py``` в терминале.


