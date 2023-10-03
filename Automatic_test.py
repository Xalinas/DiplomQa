# Понкратова Алина, Qa_pl-08-а — Дипломный проект


import requests
def test_order_creation_and_retrieval():


  # Шаг 1: Выполнить запрос на создание заказа
  url_create = f"https://fe78610b-8278-41e6-a55a-8f1a62d7d46b.serverhub.praktikum-services.ru/api/v1/orders"
  order_data = {
     "firstName": "Ivan",
     "lastName": "Ivanov",
     "address": "Lenina 16",
     "metroStation": 12,
     "phone": "+7 911 111 11 11",
     "rentTime": 5,
     "deliveryDate": "2024-06-06"
  }
  response_create = requests.post(url_create, json=order_data)


  # Шаг 2: Сохранить номер трека заказа
  order_track = response_create.json()["track"]


  # Шаг 3: Выполнить запрос на получения заказа по треку заказа
  url_get = f"https://fe78610b-8278-41e6-a55a-8f1a62d7d46b.serverhub.praktikum-services.ru/api/v1/orders/track?t={order_track}"
  response_get = requests.get(url_get)


  # Шаг 4: Проверить, что код ответа равен 200
  assert response_get.status_code == 200
