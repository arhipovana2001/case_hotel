from hotel import Rooms, Guest
"""
Поступила заявка на бронирование:

01.03.2020 Жиренкова Надежда Евдокимовна 1 01.03.2020 3 4400

Найден:

номер 1 одноместный стандарт рассчитан на 1 чел. фактически 1 чел.  полупансион стоимость 3900.00 руб./сутки

Клиент согласен. Номер забронирован.
------------------------------------------------------------------------------------------------------------
Поступила заявка на бронирование:

01.03.2020 Бузинская Альбина Кирилловна 1 03.03.2020 1 2200

Предложений по данному запросу нет. В бронировании отказано.
"""

with open('booking.txt', encoding='utf8') as b:
    people = b.read().splitlines()
    guests = []
    for guest in people:
        guest = Guest(guest)
        guests.append(guest)

    # Подбираем комнату для человека:
    for human in people:
        # print(human)
        # date = str( date-заезда date-выезда )
        # date = (human.split()[0]) + ' ' + (human.split()[5])



with open('fund.txt', encoding='utf8') as f:
    inf = f.read().splitlines()
    rooms = []
    #print(inf)
    #for room in inf:
        #room = Rooms(room)
        #rooms.append(room)
    #print(rooms)

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

    #print(list_rooms_inf)

#for
# Что и как в списке:
# ['1',['номер комнаты','мест категория'],
#  '2',['номер комнаты','мест категория'],
#  'люкс',['номер комнаты','мест категория'] ]
