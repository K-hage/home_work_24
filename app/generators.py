from typing import Dict, Iterator, Optional


def generator_commands(params: Dict[str, str | int]) -> Iterator:
    """ Генерирует команды из запроса """

    total_commands: int = len([i for i in params.keys() if 'cmd' in i]) + 1  # получаем количество команд из запроса

    for i in range(1, total_commands):

        res: Dict[str, Optional[str | int]] = {
            'cmd': None,
            'value': None
        }

        # поиск запроса и значения с одинаковым префиксом
        for k in params.keys():
            if f'cmd{i}' == k:
                res['cmd'] = params[k]
            if f'value{i}' == k:
                res['value'] = params[k]
            if None not in res.values():
                yield res
                break
