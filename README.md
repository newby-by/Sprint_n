<img src="./resource/python.svg" width="20" height="20"><img src="./resource/Selenium.png" width="20" height="20"><img src="./resource/images.jfif" width="20" height="20"><img src="./resource/pytest.png" width="20" height="20">  

# The test bicycle for Yandex's Route app

[See here the site](https://qa-routes.education-services.ru/)

We made x-broswer tests with chrome, firefox and etc. 
How to start with Docker or local, see below, though.

## Acknowledgements

The Praktikum team

[Artem Yaroshenko whom power is unlimited.](https://github.com/eroshenkoam)

My Tomcat that got me up early.
Your 4 a.m. song was so cool.(RIP)

## Requirements
    python~=3.13.13
    allure-pytest
    pytest
    selenium==3.141.0

*Note:* For local test run we use `webdriver-manager`: Chrome, Gecko and etc.

*Note:* For remote test run we use `selenoid`.

## How to start local 
1. Create venv
```bash
py -3.13 -m venv venv
```
2. Activate venv
```bash
source venv/Scripts/activate
```
3. Install requirements 
```bash
pip install -r requirements.txt
```
4. Run tests
```bash
pytest
```
*Note:* For more details use key `-vv`.
```bash
pytest -vv
```
*Note:* For creating allure reports add `--alluredir=allure-results`.

*Note:* [How to start allure](https://allurereport.org/docs/how-it-works/)

## Test cases

1. Отрисовка маршрута:
    
    **Проверить:**

    При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда" на карте отображаются две точки начала и конца маршрута

    **DONE** `TestCreateRoute.test_create_route_with_different_addresses`

2. Отрисовка блока с выбором маршрута:

    **Проверить:**

    - При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда" под выбором адресов отображается блок с выбором маршрута
    
    **DONE** `TestChooseRoute.test_show_type_block_with_different_addresses`
    
    - При вводе одинакового адреса в поля "Откуда" и "Куда" под выбором адресов отображается блок с выбором маршрута с текстом "Авто Бесплатно В пути 0 мин."
    
    **DONE** `TestChooseRoute.test_show_type_block_with_different_addresses_and_expected_text`

3. Подготовка к заказу такси. Ввести два разных предустановленных адреса в поля "Откуда" и "Куда"

    **Проверить:**

     - *XFAIL*При переключении между видами маршрута (Оптимальный\Быстрый) происходит смена активного таба и пересчет времени и стоимости маршрута
    
    **DONE**  `TestChooseRoute.test_switch_from_optimal_to_radid_info_is_changed`

    - При переключении на вид маршрута Свой происходит смена активного таба и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)

    **DONE** `TestChooseRoute.test_choose_myself_route_with_different_addresses_types_active`

    - При выборе вида маршрута Быстрый активна кнопка Вызвать такси
    
    **DONE** `TestChooseRoute.test_choose_rapid_route_with_different_addresses`
    
    - При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать

    **DONE** `TestChooseRoute.test_choose_myself_route_with_different_addresses_with_carsharing`

4. Заказ тарифа Такси. Ввести два разных предустановленных адреса в поля "Откуда" и "Куда", выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси

    **Проверить:**

    - Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный
    
    **DONE** `TestOrderTaxi.test_order_form_has_6_tariffs` and `TestOrderTaxi.test_order_form_has_only_1_active`
    
    - При наведении на иконку i в правом верхнем углу каждого тарифа отображается всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ
    
    **DONE** `TestOrderTaxi.test_tariff_has_expected_description`
    
    - Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу.  Кнопка Заказ тарифа Такси.
    
    **DONE** `TestOrderTaxi.test_order_form_has_expected_fields` and `TestOrderTaxi.test_order_form_available`

5. Сценарий. Ввести два разных предустановленных адреса в поля "Откуда" и "Куда", выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси

    **Проверить:**

    Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать 
        
    - Появляется окно ожидания машины (проверить элементы по ТЗ)
    
    **DONE** `TestWaitPage.test_wait_page_after_ordered_is_available`
    
    Дождаться окончания таймера поиска машины 
        
    - Отображается окно совершенного заказа (проверить элементы по ТЗ)

    **DONE** `TestComplitedOrderPage.test_complited_order_has_expected_title`
     `TestComplitedOrderPage.test_complited_order_has_car_number_and_tariff_image`
     `TestComplitedOrderPage.test_complited_order_has_raiting_and_name_and_foto_driver`

    Нажать кнопку Детали в блоке Еще про поездку 
        
    - Указана стоимость, которая была при выборе тарифа
    
    **DONE** `TestComplitedOrderPage.test_complited_order_has_expected_detail`
    
    Нажать кнопку Отмена 
        
    - Окно закрывается
    
    **DONE** `TestComplitedOrderPage.test_complited_order_press_cancel_is_closed`

- ТЗ и интерфейсы 
1. Блок начального экрана: 

        Карта в правой части экрана
        Блок с вводом адресов: Откуда, Куда
2. Блок с выбором маршрута: 

        Виды маршрута: Оптимальный, Быстрый, Свой
        Типы передвижения: Машина, Пешком, Такси, Велосипед, Самокат, Двайв
        Блок информации: Стоимость, Время в пути
        Кнопка Вызвать такси для типа Такси
        Кнопка Забронировать для типа Драйв
3. Блок заказа Такси: 
    
        Тарифы: Рабочий, Сонный, Отпускной, Разговорчивый, Утешительный, Глянцевый
        Поля для заполнения: Телефон, Способ оплаты, Комментарий водителю, Требования к заказу
        Кнопка Ввести номер и заказать
4. Описание тарифов Такси: 
    
        Рабочий - Для деловых особ, которых отвлекают
        Сонный - Для тех, кто не выспался
        Отпускной - Если пришла пора отдохнуть
        Разговорчивый - Если мысли не выходят из головы
        Утешительный - Если хочется свернуться калачиком
        Глянцевый - Если нужно блистать
5. Окно ожидания машины Такси:
    
        Заголовок: Поиск машины
        Таймер обратного отсчета в правом верхнем углу
        Кнопки: Отменить, Детали
6. Окно Детали: 
    
        Адреса: Адрес подачи, Адрес назначения (указаны адреса введенные в поля Откуда и Куда)
        Способ оплаты (указана информация из поля Способ оплаты из формы заказа Такси)
        Блок информации: заголовок Еще про поездку, информация Стоимость
7. Окно совершенного заказа Такси: 
    
        Заголовок: n мин. и приедет >
        Номер автомобиля и картинка тарифа в правом верхнем углу
        Блок с информацией о водителе: Имя, фото, рейтинг в правом верхнем углу фото
        Кнопки: Отменить, Детали
8. Блок заказа Драйв: 
    
        Тарифы: Повседневный, Походный, Роскошный
        Поля для заполнения: Добавить права, Способ оплаты, Требования к заказу
        Кнопка Ввести права и забронировать
9. Описание тарифов Драйв: 
    
        Повседневный - BMW 750 Просто по делам, ничего лишнего
        Походный - KIA RIO Для путешествий
        Роскошный - PORSCHE 911 Блеск, мощь, глянец
10. Окно Добавление прав тарифа Драйв: 
    
        Поля для заполнения: Имя, Фамилия, Дата рождения, Номер
        Кнопки: Добавить, Отмена
11. Окно совершенного заказа Драйв: 
    
        Заголовок: Машина забронирована
        
        Описание: Бесплатное ожидание и таймер в правом верхнем углу
        Изображение картинки выбранного тарифа и название тарифа над ней
        Кнопка Отменить
        
        Блок с информацией: Адрес машины (указан адрес введенный в поле Откуда), Еще про поездку (Стоимость)
