class Rooms:
    """The class describe The Room"""
    type_room = {'одноместный': 2900.00, 'двухместный': 2300.00, 'полулюкс': 3200.00, 'люкс': 4100.00}
    type_room_int = {1: 2900.00, 2: 2300.00, 'полулюкс': 3200.00, 'люкс': 4100.00}
    comfortable = {'стандарт': 1.0, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}
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

        self.busy_rooms = []

    def check_days(self):
        """The method counts on which days the guest wants to book a room"""
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
        days = [total]
        for i in range(int(self.number_of_days) - 1):
            total += 1
            days.append(total)
        return days

    def choice(self, days, list_rooms_inf):
        all_rooms = []
        for i in list_rooms_inf:
            for j in i[1:]:
                all_rooms.append(j)
        for i in range(2):
            if i == 0:
                comfortable_1 = Rooms.comfortable
                type_room_1 = Rooms.type_room_int
                self.number_of_guests = int(self.number_of_guests)
                room_for_guest = ''
                x = 0
                if self.number_of_guests == 1:
                    rooms_like = list_rooms_inf[0][1:]

                    if len(rooms_like) != 0:
                        for room in rooms_like:
                            comfort = comfortable_1[room[1].split()[-1]]
                            price = type_room_1[self.number_of_guests]
                            if x != 0:
                                price = price * 0.3
                            result = comfort * price * len(days)
                            if result > int(self.sum_person):
                                continue
                            elif result <= int(self.sum_person):
                                room_for_guest = room
                                all_rooms.remove(room)
                                return f'номер {room[0]} одноместный {room[1].split()[-1]} рассчитан на 1 чел фактически {self.number_of_guests} чел.\n\nКлиент согласен. Номер забронирован.'
                        else:
                            'не нашли комнату здесь'
                            x += 1
                            self.number_of_guests += 1
                elif self.number_of_guests == 2:
                    rooms_like = list_rooms_inf[1][1:]
                    if len(rooms_like) != 0:
                        for room in rooms_like:
                            comfort = comfortable_1[room[1].split()[-1]]
                            price = type_room_1[self.number_of_guests]
                            if x != 0:
                                price = price * 0.3
                            result = comfort * price * len(days)
                            if result > int(self.sum_person):
                                continue
                            elif result <= int(self.sum_person):
                                room_for_guest = room
                                all_rooms.remove(room)
                                return f'номер {room[0]} двухместный {room[1].split()[-1]} рассчитан на 2 чел фактически {self.number_of_guests} чел.\n\nКлиент согласен. Номер забронирован.'
                        else:
                            'не нашли комнату здесь'
                            x += 1
                            self.number_of_guests += 1
                else:
                    rooms_like = list_rooms_inf[2][1:]
                    if len(rooms_like) != 0:
                        for room in rooms_like:
                            max_people = int(room[1].split()[1])
                            if self.number_of_guests <= max_people:
                                comfort = comfortable_1[room[1].split()[-1]]
                                price = type_room_1[room[1].split()[0]]
                                if x != 0:
                                    price = price * 0.3
                                result = comfort * price * len(days)
                                if result > int(self.sum_person):
                                    continue
                                elif result <= int(self.sum_person):
                                    room_for_guest = room
                                    all_rooms.remove(room)
                                    return f'номер {room[0]} одноместный {room[1].split()[-1]} рассчитан на {max_people} чел фактически {self.number_of_guests} чел.\n\nКлиент согласен. Номер забронирован.'
                            else:
                                continue
                        else:
                            return 'Предложений по данному запросу нет. В бронировании отказано.'

    def __str__(self):
        """String output method"""
        return f'{self.date_of_bron} {self.first_name} {self.middle_name} {self.last_name} {self.number_of_guests} {self.date_of_arrival} {self.number_of_days} {self.sum_person}'
