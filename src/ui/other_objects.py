# Авторские права (c) KiryxaTechDev.

from typing import Literal

from customtkinter import CTkFrame

from programtools import Color
from ui import position_constants


class SeparateLine(CTkFrame):
    """
    Класс, представляющий собой разделительную линию.
    """
    def __init__(self, master, length: int, orientation: Literal['vertical', 'horizontal'], 
                 width: int = 2) -> None:
        """
        Инициализирует класс.

        Параметры:
        - length (int): Длина линии.
        - orientation (Literal['Vertical', 'Horizontal']): Ориентация линии.
        - width (int): Ширина линии.
        """
        # Настройки в зависимости от положения.
        if orientation == position_constants.VERTICAL:
            height = width
            widht = length
        elif orientation == position_constants.HORIZONTAL:
            height = length
            widht = width
        else:
            raise ValueError(f"The value cannot be '{orientation}'. Available values: 'Vertical' or 'Horizontal'.")

        super().__init__(master, width, height, fg_color=Color('separate_line'))