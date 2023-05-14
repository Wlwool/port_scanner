# a = {i: i**2 for i in range(1, 11)}
# print(a)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# Без генератора этот код имел бы следующий вид:
#
# a = {}
# for i in range(1, 11):
#     a[i] = i**2
# print(a)

# a = {word:len(word) for word in ['hi', 'hello', 'www']}
# print(a)  # {'hi': 2, 'hello': 5, 'www': 3}

# data = {
#     'Джефф Безос': '177',
#     'ИлоН МаСк': '126',
#     'бернар АрнО': '150',
#     'БиЛл ГеЙтС': '124',
# }
# new_data = {key.title(): int(value) for key, value in data.items()}
# print(new_data)  # {'Джефф Безос': 177, 'Илон Маск': 126, 'Бернар Арно': 150, 'Билл Гейтс': 124}

# Без генератора мы должны были бы сделать следующим образом:
# new_data = {}
# for key, value in data.items():
#     new_data[key.title()] = int(value)
# print(new_data)

# from pprint import pprint
# users = [
#     [0, 'Bob', 'password'],
#     [1, 'code', 'python'],
#     [2, 'Stack', 'overflow'],
#     [3, 'username', '1234'],
#     [51, 'qwerty', '1234']
# ]
# new_users = {user[0]: user for user in users}
# pprint(new_users)   # {0: [0, 'Bob', 'password'],
#                     # 1: [1, 'code', 'python'],
#                     # 2: [2, 'Stack', 'overflow'],
#                     # 3: [3, 'username', '1234'],
#                     # 51: [51, 'qwerty', '1234']}
# print('*'*15)
# pprint(new_users[3])    # [3, 'username', '1234']
# pprint(new_users[51])   # [51, 'qwerty', '1234']

# user = {
#     "id": 4170,
#     "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
#     "password": "SyUpfo1ljm",
#     "first_name": "Teresa",
#     "last_name": "Wehner",
#     "username": "teresa.wehner",
#     "email": "teresa.wehner@email.com",
#     "gender": "Female",
#     "phone_number": "+674 424.561.2776",
#     "social_insurance_number": "637316241",
#     "date_of_birth": "1993-08-17",
#     "employment": {
#         "title": "Central Hospitality Liaison",
#         "key_skill": "Organisation"
#     },
#     "subscription": {
#         "plan": "Essential",
#         "status": "Idle",
#         "payment_method": "Debit card",
#         "term": "Annual"
#     }
# }
# print({i: user[i] for i in input().split()})

# people = [
#     ['Amy Smith', '694.322.8133x22426'],
#     ['Brian Shaw', '593.662.5217x338'],
#     ['Christian Sharp', '118.197.8810'],
#     ['Sean Schmidt', '9722527521'],
#     ['Thomas Long', '163.814.9938'],
#     ['Joshua Willis', '+1-978-530-6971x601'],
#     ['Jonathan Gilbert', '9577853541']
# ]
#
# # phone_book = {item[1] for item in people}
# phone_book = {i[1]: i[0] for i in people}
# print(phone_book)



