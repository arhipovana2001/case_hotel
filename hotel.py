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


class Guest(Rooms):
    """The class describe The Guest"""

    def __init__(self, data_guest: str):
        """Initialization method"""
        self.date_of_bron, self.first_name, self.middle_name, self.last_name, self.number_of_guests, \
        self.date_of_arrival, self.number_of_days, self.sum_person = [s for s in data_guest.split()]
        #self.room = Guest.check(self.data_guest,)

        self.busy_rooms = []         # список комнат, которые заняты.

    def check_days(self):
        """The method counts on which days the guest wants to book a room"""
        # преобразует дату в число, какой по счету день в году
        data = self.date_of_arrival
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        months_vis = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total = 0
        day = int(data[:data.find('.')])
        month = int(data[data.find('.') + 1:data.rfind('.')])
        year = int(data[data.rfind('.') + 1:])
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            for i in range(0, month - 1):
                total += months[i]
            total += day
        else:
            for i in range(0, month - 1):
                total += months_vis[i]
            total += day
        # подсчитывает на какие дни гость заезжает (в формате номер дня по счету в году)
        days = [total]
        for i in range(int(self.number_of_days) - 1):
            total += 1
            days.append(total)
        return days

    def choice_of_room(self, days, list_rooms_inf):
        """The method choice of room for guest."""
        # Выбор комнаты для гостя

        comfortable_1 = Rooms.comfortable
        type_room_1 = Rooms.type_room

        room_for_guest = ''
        if int(self.number_of_guests) == 1:
            rooms_like = list_rooms_inf[0]
            if len(rooms_like) != 0:
                for room in rooms_like:
                    comfort = comfortable_1[room[0].split()[-1]]         # как-то нужно словарь перетащить сюда
                    price = type_room_1[self.number_of_guests]
                    result = comfort * price * len(days)
                    if result > self.sum_person:
                        continue
                    elif result <= self.sum_person:
                        room_for_guest = room
                        break
                else:
                    'не нашли комнату здесь'

        elif int(self.number_of_guests) == 2:
            rooms_like = list_rooms_inf[1]
            if len(rooms_like) != 0:
                for room in rooms_like:
                    comfort = comfortable_1[room[0].split()[-1]]  # как-то нужно словарь перетащить сюда
                    price = type_room_1[self.number_of_guests]
                    result = comfort * price * len(days)
                    if result > self.sum_person:
                        continue
                    elif result <= self.sum_person:
                        room_for_guest = room
                        break
                else:
                    'не нашли комнату здесь'

        else:
            rooms_like = list_rooms_inf[2]
            if len(rooms_like) != 0:
                for room in rooms_like:
                    comfort = comfortable_1[room[0].split()[-1]]  # как-то нужно словарь перетащить сюда
                    price = type_room_1[self.number_of_guests]
                    result = comfort * price * len(days)
                    if result > self.sum_person:
                        continue
                    elif result <= self.sum_person:
                        room_for_guest = room
                        break
                else:
                    'не нашли комнату здесь'

        return room_for_guest      # возвращаем спискок с номером комнаты ,вмещаемостью, степенью комфорта
                                   # также можно повторно вызывать этот метод, если комната не нашлась
                                   # типо указывать поочередно сначало вместимость, которую гость назвал
                                   # а если ,к примеру, 1-местный не нашелся ,запустить поиск ,сказав ,что
                                   # вместимость для гостя уже не 1, а 2    .Нужно со словарями как-то доделать!!




    def __str__(self):
        """String output method"""
        return f'{self.date_of_bron} {self.first_name} {self.middle_name} {self.last_name} {self.number_of_guests} {self.date_of_arrival} {self.number_of_days} {self.sum_person}'
