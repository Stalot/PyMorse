import customtkinter
from elements import Top, Display
from file_management import _internal, assets_folder, generate_path

maxsize=(...)
minsize=(960, 540)

assets_folder_path = assets_folder()
if not assets_folder_path:
    _internal_folder = _internal()
    assets_folder_path = generate_path(_internal_folder.as_posix(), 'assets')

print(assets_folder_path)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        top_font = customtkinter.CTkFont('Arial', 80)
        default_font = customtkinter.CTkFont('Arial', 16)
        customtkinter.CTkFont()

        self.title('PyMorse')
        self.iconbitmap(generate_path(assets_folder_path.as_posix(), 'PyMorse.ico'))
        self.geometry('1280x720')
        self.minsize = minsize
        self.grid_columnconfigure((0, 1), weight=1)

        self.top = Top(self, font=top_font, fg_color='transparent')
        self.top.pack(side='top', padx=10, pady=20)

        self.display = Display(self, boxfont=default_font, fg_color='transparent')
        self.display.pack(side='top')

app = App()
app.mainloop()