from hotel import Rooms, Guest

with open('fund.txt', encoding='utf8') as f:
    inf = f.read().splitlines()
    rooms = []
    for room in inf:
        room = Rooms(room)
        rooms.append(room)
    #print(rooms)

with open('booking.txt', encoding='utf8') as b:
    people = b.read().splitlines()
    guests = []
    for guest in people:
        guest = Guest(guest)
        guests.append(guest)
    #print(guests)

#for i, j in zip(guests, rooms):
    #print('-' * 86 + '\n')
    #print('Поступила заявка на бронирование:\n')
    #print(i)
    #print()
    #print('Найден:\n')
    #print(j)