# Автоматизация тестов для сайта https://qa-scooter.praktikum-services.ru/

### Для начала работы:
1. Установи webdriver: 
```
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
Мы используем webdriver, который доступен из PATH
```
2. Установи зависимости из requirements.txt
```
pip3 install -r requirements.txt
```
3. Запусти тесты из корневого каталога проекта:
```
pytest tests --alluredir=allure_results
```
4. Посмотри отчет Allure:
```
allure serve allure_results 
```

### Содержимое проекта:
```
README.md - этот файл
requirements.txt - зависимости, основные
./conftest.py - конфигурация тестов
./tests/ - каталог с тестами
./tests/test_order_page.py - тесты для проверки создания заказа и навигации по лого
./tests/test_questions_page.py - тесты для проверки вопросов и ответов
./locators/ - каталог с локаторами
./locators/base_page_locators.py - локаторы на базовой странице
./locators/order_page_locators.py - локаторы для создания заказа
./locators/questions_page_locators.py - локаторы для проверки вопросов и ответов
./pages/ - каталог с классами страниц
./pages/base_page.py - класс для базовой страницы
./pages/order_page.py - класс для страницы оформления заказа
./pages/questions_page.py - класс для страницы с вопросами
./allure_results/ - каталог с Allure отчетом
```

