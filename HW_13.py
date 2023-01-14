price = 0
while True:
    try:
        number_ticket = int(input('Введите количество билетов '))
        if type(number_ticket) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(number_ticket):
    i += 1
    while True:
        try:
            member_age = int(input(f'Введите возраст участника №{i}? '))
            if member_age < 18:
                print('Билет бесплатный')
            elif 25 > member_age >= 18:
                price += 990
                print('Цена билета: 990 руб.')
            else:
                price += 1390
                print('Цена билета: 1390 руб.')
            if type(member_age) == int:
                break
        except ValueError:
            print('Введите целое число')
if number_ticket > 5:
    price = price - ((price / 100) * 20)
    print(f'Сумма к оплате {price} руб. с учетом 20%-ой скидки')
else:
    print(f'Сумма к оплате {price} руб.')