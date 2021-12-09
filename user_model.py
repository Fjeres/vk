class User():
    def __init__(self, name='Не определено', last_name='Не определено', country='Не определено',
                 city='Не определено', birthday='Не определено', sex=0):
        self._name = name
        self._last_name = last_name
        self._country = country
        self._city = city
        self._birthday = birthday
        self._sex = sex

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):

        self._country = country['title']

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city['title']

    @property
    def birthday(self):
        return self._birthday

    # преобразование в ISO формат. ГОД-МЕСЯЦ-ДЕНЬ или МЕСЯЦ-ДЕНЬ
    @birthday.setter
    def birthday(self, birthday):
        birthday = birthday.replace(".", " ").split()
        if len(birthday[0]) == 1:
            birthday[0] = f'0{birthday[0]}'
        if len(birthday[1]) == 1:
            birthday[1] = f'0{birthday[1]}'
        if len(birthday) == 3:
            birthday = f"{birthday[2]}-{birthday[1]}-{birthday[0]}"
        else:
            birthday = f"{birthday[1]}-{birthday[0]}"
        self._birthday = birthday

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, sex):
        if sex == 1:
            self._sex = "Ж"
        elif sex == 2:
            self._sex = "М"
        else:
            self._sex = "Не определен"

    def data_normalization(self, data: dict):
        for i in data.keys():
            if 'first_name' in i:
                self.name = data['first_name']
            if 'last_name' in i:
                self.last_name = data['last_name']
            if 'bdate' in i:
                self.birthday = data['bdate']
            if 'sex' in i:
                self.sex = data["sex"]
            if 'country' in i:
                self.country = data["country"]
            if 'city' in i:
                self.city = data["city"]

    def sorting(self, user: list):
        return sorted(user, key=lambda x: x.name)

    def __str__(self):
        return f'{self._name} {self._last_name} {self._country} {self._city} {self._birthday} {self._sex}'
