from report import Collector, CSV_format, JSON_format, TSV_format
from vk_api import Api

import os


class App:
    def __init__(self, token='', id='', path='report', format_file=CSV_format):
        self.__token = token
        self.__id = id
        self.__path = path
        self.__format_file = format_file

    def __format(self, id:int) -> bool:
        if id == 1 or id == 4:
            self.__format_file = CSV_format
            return True
        elif id == 2:
            self.__format_file = JSON_format
            return True
        elif id == 3:
            self.__format_file = TSV_format
            return True
        else:
            return False

    def __path_chek(self, path) -> bool:
        if path == '':
            self.__path = 'report'
            return True
        if os.path.exists(path):
            self.__path = path
            return True
        return False

    def app(self):
        check = True
        if self.__token == '' and self.__id == '':
            self.__token = input('Введите токен>')
            self.__id = input('Введите id>')
            while check:
                format_id = int(input("Введите число для выбора нужного формата:\n"
                                      "1 - CSV\n2 - JSON\n3 - TSV\n4 - По умолчанию\n>"))
                check = not self.__format(format_id)

            check = True
            while check:
                path = input('Введите путь до файла или оставьте пустым>')
                check = not self.__path_chek(path)

        api = Api(self.__token, self.__id)

        collector = Collector(self.__format_file(data=api.data, fields=api.fields, id=api.id, path=self.__path))
        collector.make_report()
        print("Данные успешно сохранены")


if __name__ == '__main__':
    
    app = App()
    app.app()
