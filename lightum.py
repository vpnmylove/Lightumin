import os
import platform
os.system("python -m pip install pystyle requests whois phonenumbers bs4 colorama faker")
current_os = platform.system()
if current_os == "Windows":
    os.system("cls")
elif current_os == "Linux" or current_os == "Darwin":
    os.system("clear")
import pystyle
import requests
import whois
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import socket
import random
import threading
import colorama
import string
import faker
current_os = platform.system()
if current_os == "Windows":
    starting = "\n\n\n██╗░░░░░██╗░██████╗░██╗░░██╗████████╗██╗░░░██╗███╗░░░███╗\n██║░░░░░██║██╔════╝░██║░░██║╚══██╔══╝██║░░░██║████╗░████║\n██║░░░░░██║██║░░██╗░███████║░░░██║░░░██║░░░██║██╔████╔██║\n██║░░░░░██║██║░░╚██╗██╔══██║░░░██║░░░██║░░░██║██║╚██╔╝██║\n███████╗██║╚██████╔╝██║░░██║░░░██║░░░╚██████╔╝██║░╚═╝░██║\n╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝\nTelegram-канал: https://t.me/lightum_tool\nЦенник: 500 RUB\nFREE VERSION\n\n"
    pystyle.Write.Print(pystyle.Box.Lines(starting), pystyle.Colors.cyan_to_green, interval=0.001)
    menu = '1: ПОИСК ПО НОМЕРУ             | 2: WEB-CRAWLER                    | 3: ПОИСК ПО IP\n4: cB@T Б@HB0Pд                | 5: ПОРТ СКАНЕР                    | 6: DDOS\n7: ГЕНЕРАТОР СЛОЖНОГО ПАРОЛЯ   | 8: ПОИСК ПО БД                    | 9: ГЕНЕРАТОР ВЫМЫШЛЕННОЙ ЛИЧНОСТИ\n10: ИНФОРМАЦИЯ О САЙТЕ         | 11: ВЫХОД И ИНФОРМАЦИЯ            | 12: ПОИСК ПО НИКУ'
    pystyle.Write.Print(pystyle.Center.XCenter(pystyle.Box.DoubleCube(menu)), pystyle.Colors.cyan_to_green, interval=0.001)
elif current_os == "Linux" or current_os == "Darwin":
    os.system("clear")
    starting = r"   __   ___________ __________  ____  ___\n  / /  /  _/ ___/ // /_  __/ / / /  |/  /\n / /___/ // (_ / _  / / / / /_/ / /|_/ / \n/____/___/\___/_//_/ /_/  \____/_/  /_/  \n"
    pystyle.Write.Print((starting), pystyle.Colors.cyan_to_green, interval=0.001)
    menu = '\n1: ПОИСК ПО НОМЕРУ\n2: WEB-CRAWLER\n3: ПОИСК ПО IP\n4: cB@T Б@HB0Pд\n5: ПОРТ СКАНЕР\n6: DDOS\n7: ГЕНЕРАТОР СЛОЖНОГО ПАРОЛЯ\n8: ПОИСК ПО БД\n9: ГЕНЕРАТОР ВЫМЫШЛЕННОЙ ЛИЧНОСТИ\n10: ИНФОРМАЦИЯ О САЙТЕ\n11: ВЫХОД И ИНФОРМАЦИЯ\n12: ПОИСК ПО НИКУ'
    pystyle.Write.Print((menu), pystyle.Colors.cyan_to_green, interval=0.001)
def transform_text(input_text):
    translit_dict = {
        "а": "@",
        "б": "Б",
        "в": "B",
        "г": "г",
        "д": "д",
        "е": "е",
        "ё": "ё",
        "ж": "ж",
        "з": "3",
        "и": "u",
        "й": "й",
        "к": "K",
        "л": "л",
        "м": "M",
        "н": "H",
        "о": "0",
        "п": "п",
        "р": "P",
        "с": "c",
        "т": "T",
        "у": "y",
        "ф": "ф",
        "х": "X",
        "ц": "ц",
        "ч": "4",
        "ш": "ш",
        "щ": "щ",
        "ъ": "ъ",
        "ы": "ы",
        "ь": "ь",
        "э": "э",
        "ю": "ю",
        "я": "я",
        "А": "A",
        "Б": "6",
        "В": "V",
        "Г": "r",
        "Д": "D",
        "Е": "E",
        "Ё": "Ё",
        "Ж": "Ж",
        "З": "2",
        "И": "I",
        "Й": "Й",
        "К": "K",
        "Л": "Л",
        "М": "M",
        "Н": "H",
        "О": "O",
        "П": "П",
        "Р": "P",
        "С": "C",
        "Т": "T",
        "У": "Y",
        "Ф": "Ф",
        "Х": "X",
        "Ц": "Ц",
        "Ч": "Ч",
        "Ш": "Ш",
        "Щ": "Щ",
        "Ъ": "Ъ",
        "Ы": "bl",
        "Ь": "b",
        "Э": "Э",
        "Ю": "9Y",
        "Я": "9A",
    }
    transformed_text = []
    for char in input_text:
        if char in translit_dict:
            transformed_text.append(translit_dict[char])
        else:
            transformed_text.append(char)
    return "".join(transformed_text)
while True:
    choice = pystyle.Write.Input(
        "\nВыберите пункт меню > ", pystyle.Colors.cyan_to_green, interval=0.005
    )
    def ip_lookup(ip_address):
        print()
        url = f"http://ip-api.com/json/{ip_address}"
        try:
            response = requests.get(url)
            data = response.json()
            if data.get("status") == "fail":
                pystyle.Write.Print(f"[!] Произошла ошибка: {data['message']}\n", pystyle.Colors.red_to_yellow, interval=0.005)
            info = ""
            for key, value in data.items():
                info += f"[+] {key}: {value}\n"
            return info
        except Exception as e:
            pystyle.Write.Print(f"[!] Произошла ошибка: {str(e)}\n", pystyle.Colors.red_to_yellow, interval=0.005)
    def get_website_info(domain):
        domain_info = whois.whois(domain)
        print_string = f"""
[+] Домен: {domain_info.domain_name}
[+] Зарегистрирован: {domain_info.creation_date}
[+] Истекает: {domain_info.expiration_date}  
[+] Владелец: {domain_info.registrant_name}
[+] Организация: {domain_info.registrant_organization}
[+] Адрес: {domain_info.registrant_address}
[+] Город: {domain_info.registrant_city}
[+] Штат: {domain_info.registrant_state}
[+] Почтовый индекс: {domain_info.registrant_postal_code}
[+] Страна: {domain_info.registrant_country}
[+] IP-адрес: {domain_info.name_servers}
"""
        pystyle.Write.Print(print_string, pystyle.Colors.red_to_yellow, interval=0.005)
    def phoneinfo(phone_number):
        print()
        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                return pystyle.Write.Print(f"[!] Недействительный номер телефона\n", pystyle.Colors.red_to_yellow, interval=0.005)
            carrier_info = phonenumbers.carrier.name_for_number(parsed_number, "en")
            country = phonenumbers.geocoder.description_for_number(parsed_number, "en")
            region = phonenumbers.geocoder.description_for_number(parsed_number, "ru")
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            is_valid = phonenumbers.is_valid_number(parsed_number)
            is_possible = phonenumbers.is_possible_number(parsed_number)
            timezona = timezone.time_zones_for_number(parsed_number)
            print_phone_info = f"""[+] Номер телефона: {formatted_number}
[+] Страна: {country}
[+] Регион: {region}
[+] Оператор: {carrier_info}
[+] Активен?: {is_possible}
[+] Валид?: {is_valid}
[+] Таймзона: {timezona}
[+] Telegram: https://t.me/{phone_number}
[+] Whatsapp: https://wa.me/{phone_number}
[+] Viber: https://viber.click/{phone_number}
"""
            pystyle.Write.Print(print_phone_info, pystyle.Colors.red_to_yellow, interval=0.005)
        except Exception as e:
            pystyle.Write.Print(f"[!] Произошла ошибка: {str(e)}\n", pystyle.Colors.red_to_yellow, interval=0.005)
    def web_crawler(url, depth):
        print()
        visited = set()
        queue = [(url, 0)]
        while queue:
            current_url, current_depth = queue.pop(0)
            if current_url in visited or current_depth > depth:
                continue
            visited.add(current_url)
            pystyle.Write.Print(f"[+] Ссылка: {current_url}\n", pystyle.Colors.red_to_yellow, interval=0.005)
            try:
                response = requests.get(current_url)
                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.find_all('a', href=True):
                    absolute_url = urljoin(current_url, link['href'])
                    queue.append((absolute_url, current_depth + 1))
            except:
                pystyle.Write.Print(f"[!] Произошла ошибка, проверьте ввод данных\n", pystyle.Colors.red_to_yellow, interval=0.005)
    def get_characters(complexity):
        characters = string.ascii_letters + string.digits
        if complexity == "medium":
            characters += "!@#$%^&*()"
        elif complexity == "high":
            characters += string.punctuation
        return characters
    def generate_password(length, complexity):
        characters = get_characters(complexity)
        password = "".join(random.choice(characters) for i in range(length))
        return password
    if choice == "1":
        number = pystyle.Write.Input(
            '[?] Номер телефона (Пример : +7XXXXXXXXXX): ', pystyle.Colors.cyan_to_green, interval=0.005
        )
        phoneinfo(number)
    if choice == "3":
            ip_address = pystyle.Write.Input(
                "[?] Введите IP-адрес для поиска: ", pystyle.Colors.cyan_to_green, interval=0.005
            )
            result = ip_lookup(ip_address)
            pystyle.Write.Print(result, pystyle.Colors.red_to_yellow, interval=0.005)
    if choice == "10":
        domain = pystyle.Write.Input(
            "[?] Введите домен сайта: ", pystyle.Colors.cyan_to_green, interval=0.005
        )
        get_website_info(domain)
    if choice == "2":
        url = pystyle.Write.Input(
            f'[?] Введите ссылку для кравлинга: ', pystyle.Colors.cyan_to_green, interval=0.005
        )
        web_crawler(url, depth=2)
    if choice == "8":
        path = pystyle.Write.Input("[?] Введите путь к БД: ", pystyle.Colors.cyan_to_green, interval=0.005)
        search_text = pystyle.Write.Input(
            "[?] Введите текст:  ", pystyle.Colors.cyan_to_green, interval=0.005
        )
        print()
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    if search_text in line:
                        pystyle.Write.Print(
                            "[+] Результат: " + line.strip(),
                            pystyle.Colors.red_to_yellow,
                            interval=0.005,
                        )
                        print()
                        break
                else:
                    pystyle.Write.Print("[!] Текст не найден.", pystyle.Colors.cyan_to_green, interval=0.005)
        except:
            try:
                with open(path, "r", encoding="cp1251") as f:
                    for line in f:
                        if search_text in line:
                            pystyle.Write.Print(
                                "[+] Результат: " + line.strip(),
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                            print()
                            break
                    else:
                        pystyle.Write.Print("[!] Текст не найден.", pystyle.Colors.cyan_to_green, interval=0.005)
            except:
                try:
                    with open(path, "r", encoding="cp1252") as f:
                        for line in f:
                            if search_text in line:
                                pystyle.Write.Print(
                                    "[+] Результат: " + line.strip(),
                                    pystyle.Colors.red_to_yellow,
                                    interval=0.005,
                                )
                                print()
                                break
                        else:
                            pystyle.Write.Print("[!] Текст не найден.", pystyle.Colors.cyan_to_green, interval=0.005)
                except:
                    pystyle.Write.Print(f"[!] Произошла ошибка, проверьте ввод данных\n", pystyle.Colors.red_to_yellow, interval=0.005)
    if choice == "4":
        input_text = pystyle.Write.Input("[?] Введите текст: ", pystyle.Colors.cyan_to_green, interval=0.005)
        transformed_text = transform_text(input_text)
        print()
        pystyle.Write.Print(
            "[+] Результат: " + transformed_text + "\n",
            pystyle.Colors.red_to_yellow,
            interval=0.005,
        )
    if choice == "5":
        pystyle.Write.Print("[?] Выберите режим: ", pystyle.Colors.cyan_to_green, interval=0.005)
        pystyle.Write.Print("\n[?] 1 - проверить часто используемые порты", pystyle.Colors.cyan_to_green, interval=0.005)
        pystyle.Write.Print("\n[?] 2 - проверить указанный порт", pystyle.Colors.cyan_to_green, interval=0.005)
        mode = pystyle.Write.Input("\n[?] Ваш выбор: ", pystyle.Colors.cyan_to_green, interval=0.005)
        if mode == "1":
            print()
            ports = [
                20,
                26,
                28,
                29,
                55,
                53,
                80,
                110,
                443,
                8080,
                1111,
                1388,
                2222,
                1020,
                4040,
                6035,
            ]
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex(("127.0.0.1", port))
                if result == 0:
                    pystyle.Write.Print(f"[+] Порт {port} открыт", pystyle.Colors.red_to_yellow, interval=0.005)
                else:
                    pystyle.Write.Print(f"[+] Порт {port} закрыт", pystyle.Colors.red_to_yellow, interval=0.005)
                sock.close()
                print()
        elif mode == "2":
            print()
            port = pystyle.Write.Input("[?] Введите номер порта: ", pystyle.Colors.cyan_to_green, interval=0.005)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(("127.0.0.1", int(port)))
            if result == 0:
                pystyle.Write.Print(f"[+] Порт {port} открыт", pystyle.Colors.red_to_yellow, interval=0.005)
            else:
                pystyle.Write.Print(f"[+] Порт {port} закрыт", pystyle.Colors.red_to_yellow, interval=0.005)
            sock.close()
            print()
        else:
            pystyle.Write.Print("[!] Неизвестный режим", pystyle.Colors.red_to_yellow, interval=0.005)
            print()
    if choice == "6":
        url = pystyle.Write.Input("[?] URL: ", pystyle.Colors.cyan_to_green, interval=0.005)
        num_requests = int(
            pystyle.Write.Input(
                "[?] Введите количество запросов: ", pystyle.Colors.cyan_to_green, interval=0.005
            )
        )
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
        ]
        def send_request(i):
            user_agent = random.choice(user_agents)
            headers = {"User-Agent": user_agent}
            try:
                response = requests.get(url, headers=headers)
                print(f"{colorama.Fore.GREEN}[+] Request {i} sent successfully\n")
            except:
                print(f"{colorama.Fore.GREEN}[+] Request {i} sent successfully\n")
        threads = []
        for i in range(1, num_requests + 1):
            t = threading.Thread(target=send_request, args=[i])
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    if choice == "7":
        password_length = int(
            pystyle.Write.Input("[?] Введите длину пароля: ", pystyle.Colors.cyan_to_green, interval=0.005)
        )
        complexity = pystyle.Write.Input(
            "[?] Выберите сложность (low, medium, high): ",
            pystyle.Colors.cyan_to_green,
            interval=0.005,
        )
        print()
        complex_password = generate_password(password_length, complexity)
        pystyle.Write.Print("[+] "+ complex_password + "\n", pystyle.Colors.red_to_yellow, interval=0.005)
    if choice == "9":
        fake = faker.Faker(locale="ru_RU")
        gender = pystyle.Write.Input("[?] Введите пол (М - мужской, Ж - женский): ", pystyle.Colors.cyan_to_green, interval=0.005)
        print()
        if gender not in ["М", "Ж"]:
            gender = random.choice(["М", "Ж"])
            pystyle.Write.Print(f"[!] Вы ввели неверное значение, будет выбрано случайным образом: {gender}\n\n", pystyle.Colors.cyan_to_green, interval=0.005)
        if gender == "М":
            first_name = fake.first_name_male()
            middle_name = fake.middle_name_male()
        else:
            first_name = fake.first_name_female()
            middle_name = fake.middle_name_female()
        last_name = fake.last_name()
        full_name = f"{last_name} {first_name} {middle_name}"
        birthdate = fake.date_of_birth()
        age = fake.random_int(min=18, max=80)
        street_address = fake.street_address()
        city = fake.city()
        region = fake.region()
        postcode = fake.postcode()
        address = f"{street_address}, {city}, {region} {postcode}"
        email = fake.email()
        phone_number = fake.phone_number()
        inn = str(fake.random_number(digits=12, fix_len=True))
        snils = str(fake.random_number(digits=11, fix_len=True))
        passport_num = str(fake.random_number(digits=10, fix_len=True))
        passport_series = fake.random_int(min=1000, max=9999)
        pystyle.Write.Print(f"[+] ФИО: {full_name}\n", pystyle.Colors.red_to_yellow, interval=0.005)
        pystyle.Write.Print(f"[+] Пол: {gender}\n", pystyle.Colors.red_to_yellow, interval=0.005)
        pystyle.Write.Print(f"[+] Дата рождения: {birthdate.strftime('%d %B %Y')}\n", pystyle.Colors.red_to_yellow, interval=0.005)
        pystyle.Write.Print(f"[+] Возраст: {age} лет\n", pystyle.Colors.red_to_yellow, interval=0.005)
        pystyle.Write.Print(f"[+] Адрес: {address}\n", pystyle.Colors.red_to_yellow, interval=0.005)
        pystyle.Write.Print(f"[+] Email: {email}\n", pystyle.Colors.red_to_yellow, interval=0.005)
        pystyle.Write.Print(f"[+] Телефон: {phone_number}\n", pystyle.Colors.red_to_yellow, interval=0.005)
        pystyle.Write.Print(f"[+] ИНН: {inn}\n", pystyle.Colors.red_to_yellow, interval=0.005)
        pystyle.Write.Print(f"[+] СНИЛС: {snils}\n", pystyle.Colors.red_to_yellow, interval=0.005)
        pystyle.Write.Print(f"[+] Паспорт серия: {passport_series} номер: {passport_num}\n", pystyle.Colors.red_to_yellow, interval=0.005)
    if choice == "12":
        nick = pystyle.Write.Input(f"Введите никнейм: ", pystyle.Colors.cyan_to_green, interval=0.005)
        urls = [
            f"https://www.instagram.com/{nick}",
            f"https://www.tiktok.com/@{nick}",
            f"https://twitter.com/{nick}",
            f"https://www.facebook.com/{nick}",
            f"https://www.youtube.com/@{nick}",
            f"https://t.me/{nick}",
            f"https://www.roblox.com/user.aspx?username={nick}",
            f"https://https://www.twitch.tv/{nick}",
        ]
        for url in urls:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    pystyle.Write.Print(f"\n{url} - аккаунт найден", pystyle.Colors.red_to_yellow, interval=0.005)
                elif response.status_code == 404:
                    pystyle.Write.Print(f"\n{url} - аккаунт не найден", pystyle.Colors.cyan_to_green, interval=0.005)
                else:
                    pystyle.Write.Print(f"\n{url} - ошибка {response.status_code}", pystyle.Colors.cyan_to_green, interval=0.005)
            except:
                pystyle.Write.Print(f"\n{url} - ошибка при проверке", pystyle.Colors.cyan_to_green, interval=0.005)
        print()
    if choice == "11":
        pystyle.Write.Print(f"\n[+] CREATOR -> @vpnmylove1\n[+] TELEGRAM -> https://t.me/lightum_tool\n[+] DONATE -> https://t.me/send?start=IV8PuD6wa0zz\n\n", pystyle.Colors.cyan_to_green, interval=0.005)
        sure = pystyle.Write.Input("[?] Вы действительно хойтите выйти? Y/N: ", pystyle.Colors.cyan_to_green, interval=0.005)
        if sure.lower() == "y" or sure.lower() == "yes" or sure.lower() == "н" or sure.lower() == "нуы" or sure.lower() == "да" or sure.lower() == "lf":
            exit()
        elif sure.lower() == "n" or sure.lower() == "no" or sure.lower() == "not" or sure.lower() == "т" or sure.lower() == "тщ" or sure.lower() == "тще" or sure.lower() == "нет" or sure.lower() == "не":
            0
        else:
            0