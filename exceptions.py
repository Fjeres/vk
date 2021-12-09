class GenericException(Exception):

    def __str__(self):
        pass


class ProfileClosed(GenericException):
    def __init__(self):
        self.__code = 30
        self.msg = "Профиль закрыт"

    def __str__(self):
        return f'code:{self.__code} message: {self.msg}'


class FailedToGetUsers(GenericException):
    def __init__(self):
        self.__code = 3
        self.msg = "Ошибка получения друзей"

    def __str__(self):
        return f'code:{self.__code} message: {self.msg}'


class TokenIsNotValid(GenericException):
    def __init__(self):
        self.__code = 4
        self.msg = "Токен не валидный"

    def __str__(self):
        return f'code:{self.__code} message: {self.msg}'


