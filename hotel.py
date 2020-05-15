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

    def __init__(self, data_guest: str):
        """Initialization method"""
        self.date_of_bron, self.first_name, self.middle_name, self.last_name, self.number_of_guests, \
        self.date_of_arrival, self.number_of_days, self.sum_person = [s for s in data_guest.split()]
        #self.room = Guest.check(self.data_guest,)

    def __str__(self):
        """String output method"""
        return f'{self.date_of_bron} {self.first_name} {self.middle_name} {self.last_name} {self.number_of_guests} {self.date_of_arrival} {self.number_of_days} {self.sum_person}'

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
        for i in range (int(self.number_of_days) - 1):
            total += 1
            days.append(total)
        return days
