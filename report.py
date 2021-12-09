from __future__ import annotations
from abc import ABC, abstractmethod
import csv
import json


class ReportStrategy(ABC):
    @abstractmethod
    def import_data(self, ):
        pass


# При отсутствии года рождения, exel сам ставит год на текущий
# Так же не понял, почему ставит #### вместо даты, но если нажать по полю + enter, то все работает
class CSV_format(ReportStrategy):
    def __init__(self, data: list, fields: list, id: int, path):
        self.__data = data
        self.__path = path
        self.__fields = fields
        self.__id = id

    def import_data(self, ):
        with open(f'{self.__path}/{self.__id}.csv', 'w', newline='',
                  encoding="cp1251", errors='ignore') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                self.__fields
            )
            for item in self.__data:
                writer.writerow([
                    item.name,
                    item.last_name,
                    item.country,
                    item.city,
                    item.birthday,
                    item.sex,
                ])


class JSON_format(ReportStrategy):
    def __init__(self, data: list, fields: list, id: int, path='report'):
        self.__data = data
        self.__path = path
        self.__fields = fields
        self.__id = id

    def import_data(self):
        data_list = []
        for item in self.__data:
            data_list.append(
                {
                    self.__fields[0]: item.name,
                    self.__fields[1]: item.last_name,
                    self.__fields[2]: item.country,
                    self.__fields[3]: item.city,
                    self.__fields[4]: item.birthday,
                    self.__fields[5]: item.sex,
                })

        with open(f'{self.__path}/{self.__id}.json', 'w', encoding='utf-8') as file:
            json.dump(data_list, file, ensure_ascii=False, indent=4)


class TSV_format(ReportStrategy):
    def __init__(self, data: list, fields: list, id: int, path):
        self.__data = data
        self.__path = path
        self.__fields = fields
        self.__id = id

    def import_data(self, ):
        with open(f'{self.__path}/{self.__id}.tsv', 'w', newline='',
                  encoding="cp1251", errors='ignore') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                self.__fields
            )
            for item in self.__data:
                writer.writerow([
                    item.name,
                    item.last_name,
                    item.country,
                    item.city,
                    item.birthday,
                    item.sex,
                ])


class Collector():
    def __init__(self, strategy: ReportStrategy):
        self._strategy = strategy

    @property
    def strategy(self, ) -> ReportStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: ReportStrategy) -> None:
        self._strategy = strategy

    def make_report(self, ) -> str:
        return self._strategy.import_data()
