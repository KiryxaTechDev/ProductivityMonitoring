import tkinter as tk

import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkOptionMenu
from customtkinter import CTkFont

from Ui import Colors


class SettingFrame(CTkFrame):
    def __init__(self,
                 master: CTkFrame|tk.Tk|ctk.CTk,
                 title: str,

                 option_menu_values: list|tuple = None):
        
        super().__init__(master=master,
                         fg_color=Colors.BAR,
                         corner_radius=7)

        self.font = CTkFont('Segoe UI', size=20)
        self.title_label = CTkLabel(self,
                                    height=80,
                                    text=title,
                                    anchor='e',
                                    font=self.font)
        
        self.title_label.pack(side=tk.LEFT, padx=5)

        self.option_menu = CTkOptionMenu(
            master=self,
            values=option_menu_values
        )
        self.option_menu.pack(side=tk.RIGHT, padx=5)

    def auto_place(self):
        self.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)