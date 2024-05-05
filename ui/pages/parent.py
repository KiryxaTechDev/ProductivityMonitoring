from customtkinter import CTkFrame, CTkLabel
from customtkinter import CTkFont

class ParentPage(CTkFrame):
    def __init__(self, master, title: str):
        super().__init__(master, fg_color='#323232', corner_radius=0)

        self.font = CTkFont('Segoe UI', 20, 'bold')

        self.title = CTkLabel(self, width=200, height=40, font=self.font, text=title, anchor='w')
        self.title.place(x=10, y=0)

    def auto_place(self):
        self.grid(column=1, row=0, sticky='nsew')