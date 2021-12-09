import requests
from user_model import User
from exceptions import ProfileClosed, FailedToGetUsers, TokenIsNotValid


class Api:
    def __init__(self, token: str, id: str):
        self.__token = token
        self.__id = id
        self.__user_fields = ['first_name', 'last_name', 'country', 'city', 'bdate', 'sex', ]

    def __token_verification(self) -> bool:
        request = requests.get(
            f'https://api.vk.com/method/users.get?access_token={self.__token}&v=5.131')
        if request.text.find("response") == -1:
            return False
        return True

    # Для определения количества друзей, т.к с fields он выдает не больше 5000
    def __api_get_count(self):
        request = requests.get(
            f'https://api.vk.com/method/friends.get?'
            f'user_id={self.__id}'
            f'&access_token={self.__token}'
            f'&v=5.131')
        if 'error' in request.json():
            raise ProfileClosed
        return request.json()["response"]['count']

    def __api_get_data(self, count=5000, offset=0):
        data = {}
        data_users = []

        request = requests.get(
            f'https://api.vk.com/method/friends.get?'
            f'user_id={self.__id}'
            f'&fields=city,country,bdate,sex'
            f'&count={count}'
            f'&offset={offset}'
            f'&access_token={self.__token}'
            f'&v=5.131')

        for item in request.json()["response"]['items']:
            user = User()
            for field in self.__user_fields:
                if field in item:
                    data[field] = item[field]

            user.data_normalization(data)
            data_users.append(user)

        return data_users

    @property
    def fields(self):
        return self.__user_fields

    @property
    def id(self):
        return self.__id

    @property
    def data(self, ):
        if self.__token_verification():
            count = self.__api_get_count()
            data_users = self.__api_get_data()
            if count > 5000:
                data_users += self.__api_get_data(offset=5000)

            if len(data_users) != count:
                raise FailedToGetUsers
            return data_users[0].sorting(data_users)
        else:
            raise TokenIsNotValid
