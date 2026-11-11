# Sauce Demo UI Autotests

UI-автотесты для демо-магазина [Sauce Demo](https://www.saucedemo.com/), написанные на **Python + Selenium + pytest** с использованием паттерна **Page Object Model**.

Проект покрывает основные пользовательские сценарии: авторизацию, работу с каталогом товаров, сортировку, корзину, оформление заказа и футер.

## Стек

| Инструмент | Назначение |
|---|---|
| Python 3.14 | язык проекта |
| Selenium 4.48 | управление браузером |
| pytest 9.1.1 | тестовый раннер |
| pytest-xdist | параллельный запуск тестов |
| pytest-rerunfailures | автоматические рераны упавших тестов |
| python-dotenv | загрузка переменных окружения из `.env` |

Драйвер браузера отдельно устанавливать не нужно — Selenium Manager подтягивает его автоматически. Локально должен быть установлен **Google Chrome**.

## Структура проекта

```
.
├── .github/workflows/          # CI: запуск тестов в GitHub Actions
├── components/                 # переиспользуемые компоненты страниц (header, footer, sidebar)
├── data/                       # тестовые данные и ожидаемые тексты
├── pages/                      # Page Object классы
│   └── checkout_form_pages/    # страницы оформления заказа
├── tests/                      # тесты, сгруппированные по функциональности
├── conftest.py                 # общие фикстуры (driver, auth_inventory_page)
├── pytest.ini                  # конфигурация pytest
└── requirements.txt            # зависимости проекта
```

## Установка

1. Клонировать репозиторий:

   ```bash
   git clone https://github.com/freakeno16/sele-swag-labs-autotests.git
   cd sele-swag-labs-autotests
   ```

2. Создать и активировать виртуальное окружение:

   ```bash
   python -m venv venv

   # macOS / Linux
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Создать в корне проекта файл `.env` (он в `.gitignore` и не попадает в репозиторий):

   ```dotenv
   BASE_URL=https://www.saucedemo.com/

   STANDARD_USER_USERNAME=standard_user
   PASSWORD=secret_sauce

   INVALID_STANDARD_USER_USERNAME=invalid_user
   INVALID_PASSWORD=invalid_password
   ```

   Значения `BASE_URL` и тестовых учётных данных можно взять из описания Sauce Demo на странице логина.

## Запуск тестов

Запустить весь набор (параллельно, с одним рераном и коротким traceback — настройки в `pytest.ini`):

```bash
pytest
```

Отдельные группы:

```bash
pytest tests/login             # авторизация
pytest tests/inventory         # корзина и сортировка
pytest tests/checkout          # оформление заказа
pytest tests/test_footer.py    # футер
```

Один тест по имени:

```bash
pytest tests/inventory/test_sorting_items.py::test_sort_items_by_price_from_low_to_high
```

Без параллельности и реранов (удобно при отладке):

```bash
pytest -n 0 --reruns 0
```

Локально тесты запускаются в **видимом** браузере Chrome. Если задана переменная окружения `CI`, `conftest.py` автоматически переключает браузер в headless-режим — это используется на билд-агенте.

## Покрытие

| Группа тестов | Сценарии |
|---|---|
| `tests/login` | успешный логин, логаут, неверные и пустые креды, тексты ошибок |
| `tests/inventory` | добавление товара в корзину, счётчик на иконке, кнопка «Continue shopping», сортировка по цене и имени |
| `tests/checkout` | итоговая сумма заказа при пустой корзине |
| `tests/test_footer` | отображение футера и корректность копирайта |

## CI

GitHub Actions запускает весь набор тестов при каждом пуше и пулл-реквесте в `main` (workflow — `.github/workflows/tests.yml`). Конфигурация `.env` на раннере генерируется из [секретов репозитория](https://github.com/freakeno16/sele-swag-labs-autotests/settings/secrets/actions):

`BASE_URL`, `STANDARD_USER_USERNAME`, `PASSWORD`, `INVALID_STANDARD_USER_USERNAME`, `INVALID_PASSWORD`

По завершении рана результаты прогона сохраняются как артефакт `pytest-results`. Статус последнего запуска отображается во вкладке **Actions** и рядом с коммитом.