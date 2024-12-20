import customtkinter
from elements import Top, Display

maxsize=(...)
minsize=(960, 540)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        top_font = customtkinter.CTkFont('Arial', 64)
        default_font = customtkinter.CTkFont('Arial', 16)

        self.title('PyMorse')
        self.geometry('1280x720')
        self.minsize = minsize
        self.grid_columnconfigure((0, 1), weight=1)

        self.top = Top(self, font=top_font, fg_color='transparent')
        self.top.pack(side='top', padx=10, pady=10)

        self.display = Display(self, boxfont=default_font, fg_color='transparent')
        self.display.pack(side='top')

app = App()
app.mainloop()