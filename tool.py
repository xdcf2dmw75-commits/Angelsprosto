import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type, format_number, PhoneNumberFormat
import requests
import socket


def phone_info():
    num = input("Введите номер (+...): ").strip()

    try:
        parsed = phonenumbers.parse(num)
        zones = timezone.time_zones_for_number(parsed)

        t = number_type(parsed)
        if t == phonenumbers.PhoneNumberType.MOBILE:
            t = "Мобильный"
        elif t == phonenumbers.PhoneNumberType.FIXED_LINE:
            t = "Стационарный"
        else:
            t = "Неизвестно"

        print("\n========== ИНФО НОМЕРА ==========")
        print("Номер:", num)
        print("Регион:", geocoder.description_for_number(parsed, "ru"))
        print("Оператор:", carrier.name_for_number(parsed, "ru"))
        print("Тип:", t)
        print("Часовой пояс:", zones[0] if zones else "Неизвестно")
        print("Валидный:", phonenumbers.is_valid_number(parsed))
        print("Формат международный:", format_number(parsed, PhoneNumberFormat.INTERNATIONAL))
        print("Формат национальный:", format_number(parsed, PhoneNumberFormat.NATIONAL))
        print("================================")

    except Exception as e:
        print("Ошибка номера:", e)

    input("\nНажми Enter...")


def ip_info():
    ip = input("Введите IP: ").strip()

    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = r.json()

        print("\n========== ИНФО IP ==========")

        if data.get("status") != "success":
            print("Ошибка:", data.get("message"))
        else:
            print("IP:", data.get("query"))
            print("Страна:", data.get("country"))
            print("Регион:", data.get("regionName"))
            print("Город:", data.get("city"))
            print("Провайдер:", data.get("isp"))
            print("Организация:", data.get("org"))
            print("Часовой пояс:", data.get("timezone"))
            print("Координаты:", data.get("lat"), data.get("lon"))

        print("================================")

    except requests.exceptions.RequestException:
        print("Ошибка сети")

    except Exception as e:
        print("Ошибка:", e)

    input("\nНажми Enter...")


def site_info():
    site = input("Введите сайт: ").strip()

    try:
        ip = socket.gethostbyname(site)

        print("\n========== ИНФО САЙТА ==========")
        print("Домен:", site)
        print("IP:", ip)

        try:
            socket.create_connection((site, 80), timeout=3)
            print("Порт 80: открыт")
        except:
            print("Порт 80: закрыт")

        print("================================")

    except Exception as e:
        print("Ошибка сайта:", e)

    input("\nНажми Enter...")


while True:

    print("""
================================
        ANGEL KOROL TOOL
================================
1 - Инфо по номеру
2 - Инфо по IP
3 - Инфо по сайту
4 - Выход
================================
""")

    choice = input("Выбери: ").strip()

    if choice == "1":
        phone_info()
    elif choice == "2":
        ip_info()
    elif choice == "3":
        site_info()
    elif choice == "4":
        break
    else:
        print("Неверный выбор!")
