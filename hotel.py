class Rooms:
    """The class describe The Room"""
    type_room = {'одноместный': 2900.00, 'двухместный': 2300.00, 'полулюкс': 3200.00, 'люкс': 4100.00}
    comfortable = {'стандарт': 1.0, 'стандарт улучшенный': 1.2, 'апартамент': 1.5}
    food = {'без питания': 0.00, 'завтрак': 280.00, 'полупансион': 1000.00}

    def __init__(self, data_room: str):
        """Initialization method"""
        self.room, self.type_, self.max_people, self.degree_comfortable = [s for s in data_room.split()]

    def __str__(self):
        """String output method"""
        return f'{self.room} {self.type_} {self.degree_comfortable} рассчитан на {self.max_people} чел.'


class Guest:
    """The class describe The Guest"""

    #@staticmethod
    #def check(dates, days):


    def __init__(self, data_guest: str):
        """Initialization method"""
        self.date_of_bron, self.first_name, self.middle_name, self.last_name, self.number_of_guests, \
        self.date_of_arrival, self.number_of_days, self.sum_person = [s for s in data_guest.split()]
        #self.room = Guest.check(self.data_guest,)

    def __str__(self):
        """String output method"""
        return f'{self.date_of_bron} {self.first_name} {self.middle_name} {self.last_name} {self.number_of_guests} {self.date_of_arrival} {self.number_of_days} {self.sum_person}'


with open('fund.txt', encoding='utf8') as f:
    inf = f.read().splitlines()
    rooms = []
    for room in inf:
        room = Rooms(room)
        rooms.append(room)
    print(rooms)

with open('booking.txt', encoding='utf8') as b:
    people = b.read().splitlines()
    guests = []
    for guest in people:
        guest = Guest(guest)
        guests.append(guest)

for i, j in zip(guests, rooms):
    print('-' * 86 + '\n')
    print('Поступила заявка на бронирование:\n')
    print(i)
    print()
    print('Найден:\n')
    print(j)