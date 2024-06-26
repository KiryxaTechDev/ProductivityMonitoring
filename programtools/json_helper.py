import json

from pathlib import Path
from typing import Union, Dict, Any
from logging import getLogger

from programtools.static_meta import StaticMeta


# Создание логгера.
logger = getLogger(__name__)


class JsonHelper(metaclass=StaticMeta):
    """
    Класс, упрощающий работу с JSON.
    """
    def read(fp: Union[str, Path]) -> Dict[str, Any]:
        """
        Читает JSON-файл и возвращает словарь элементов.

        Параметры:
        - fp (Union[str, Path]): Путь до файла.

        Возвращает:
        - Dict[str, Any]: Словарь элементов.
        """
        try:
            logger.debug(f"Reading '{fp}'.")
            with open(fp, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"File {fp} not found. Returning an empty dictionary.")
            return {}

    def write(data: Dict[str, Any], fp: Union[str, Path]) -> None:
        """
        Записывает данные в JSON-файл.

        Параметры:
        - data (Dict[str, Any]): Данные для записи.
        - fp (Union[str, Path]): Путь до файла.
        """
        logger.debug(f"Writing '{fp}'.")
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)