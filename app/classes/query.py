import re
from typing import List, Dict, Any, Iterator, Callable


class Query:
    """ Класс запроса """

    def __init__(self, path: str):
        self.path = path
        self._command: Dict[str, Callable] = {
            'filter': self._filter,
            'sort': self._sort,
            'map': self._map,
            'unique': self._unique,
            'limit': self._limit,
            'regex': self._regex
        }

    def prepared_data(self) -> List[str]:
        """ Подготовка данных из файла """
        with open(self.path) as f:
            return list(map(lambda x: x.strip(), f))

    def get_query(self, params: Iterator) -> List[str]:
        """ Возвращает данные по параметрам из запроса """

        data = self.prepared_data()
        for param in params:
            data = self._command[param['cmd']](param=param['value'], data=data)
        return data

    @staticmethod
    def _filter(param: str, data: List[str]) -> List[str]:
        return list(filter(lambda v: param in v, data))

    @staticmethod
    def _map(param: str, data: List[str]) -> List[str]:
        column_number: int = int(param)

        return list(map(lambda v: v.split()[column_number], data))

    @staticmethod
    def _unique(data: List[str], *args: Any, **kwargs: Any) -> List[str]:
        return list(set(data))

    @staticmethod
    def _sort(param: str, data: List[str]) -> List[str]:
        reverse = False if param == 'asc' else True
        return sorted(data, reverse=reverse)

    @staticmethod
    def _limit(param: str, data: List[str]) -> List[str]:
        limit = int(param)
        return list(data)[:limit]

    @staticmethod
    def _regex(param: str, data: List[str]) -> List[str]:
        pattern = re.compile(param)
        return list(filter(lambda v: re.search(pattern, v), data))
