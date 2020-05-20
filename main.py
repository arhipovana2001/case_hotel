''' Case study Hotel
Developers: Arkhipova A.(50%)
            Revtova L.(35%)
            Panyukova E.(50%)
            Kuznetsova K.(20%)
'''
from hotel import Rooms, Guest


with open('booking.txt', encoding='utf8') as b:
    people = b.read().splitlines()
    guests = []
    for guest in people:
        guest = Guest(guest)
        guests.append(guest)

with open('fund.txt', encoding='utf8') as f:
    inf = f.read().splitlines()
    rooms = []
    for room in inf:
        room = Rooms(room)
        rooms.append(room)
    list_rooms_inf = [['1'], ['2'], ['люкс']]
    for room_ in inf:
        if '1' in room_[2:]:
            _rm = room_[2:]
            num_rum = int(room_[:2])
            list_rooms_inf[0].append((str(num_rum) + ',' + _rm[_rm.find('1'):]).split(','))
        elif '2' in room_[2:]:
            _rm = room_[2:]
            num_rum = int(room_[:2])
            list_rooms_inf[1].append((str(num_rum) + ',' + _rm[_rm.find('2'):]).split(','))
        elif 'люкс' in room_[2:]:
            _rm = room_[2:]
            num_rum = int(room_[:2])
            list_rooms_inf[2].append((str(num_rum) + ',' + _rm[_rm.find('люкс'):]).split(','))

    for i, j in zip(guests, rooms):
        print('-' * 86 + '\n')
        print('Поступила заявка на бронирование:\n')
        print(i)
        print()
        print('Найден:\n')
        days = i.check_days()
        print(i.choice(days, list_rooms_inf))
