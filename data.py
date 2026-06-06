import pytest


BASE_URL = "https://qa-routes.education-services.ru/"

ADDRESSES = ["улица Хамовнический Вал, 34", "Зубовский бульвар, 37", ]

TYPE_MOVEMENT = {
    "Авто": 1,
    "Пешком": 2,
    "Такси": 3,
    "Велосипед": 4,
    "Самокат": 5,
    "Драйв": 6
}

ONLY_ONE_CARD_ACTIVE = 1
ORDER_TAXI_FORM = {
    "tariffs": ["Рабочий", "Сонный", "Отпускной",
                "Разговорчивый", "Утешительный","Глянцевый"],
    "params": [
        "Рабочий",
        pytest.param(
            "Сонный",
            marks=pytest.mark.xfail(reason="The discription is unexpected")
        ),
        "Отпускной",
        pytest.param(
            "Разговорчивый",
            marks=pytest.mark.xfail(reason="The discription is unexpected")
        ),
        "Утешительный",
        "Глянцевый"
    ],
    "descriptions": [
        "Для деловых особ, которых отвлекают",
        "Для тех, кто не выспался",
        "Если пришла пора отдохнуть",
        "Если мысли не выходят из головы",
        "Если хочется свернуться калачиком",
        "Если нужно блистать"
    ],
    "fields": ["Телефон", "Способ оплаты", "Комментарий водителю", "Требования к заказу"],
}
