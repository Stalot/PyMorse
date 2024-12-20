import customtkinter
from translator import encrypt, decrypt

class Top(customtkinter.CTkFrame):
    def __init__(self, *args, font: customtkinter.CTkFont = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure((0, 1), weight=1)

        self.title = customtkinter.CTkLabel(self, text='PyMorse', font=font)
        self.title.grid(row=0, column=0, sticky='ew')

class TextBox(customtkinter.CTkFrame):
    def __init__(self, *args, font: customtkinter.CTkFont = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure((0, 1), weight=1)

        self.textBox = customtkinter.CTkTextbox(self, font=font, width=600, height=500)
        self.textBox.pack()

class Display(customtkinter.CTkFrame):
    def __init__(self, *args, boxfont: customtkinter.CTkFont = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure((0, 1), weight=1)

        buttonFont = customtkinter.CTkFont('Arial', 24)

        self.leftBox = TextBox(self, font=boxfont)
        self.leftBox.grid(row=0, column=0, padx=40)
        self.encryptButton = customtkinter.CTkButton(self, width=200, text='Encrypt', font=buttonFont, command=self.encrypt_text)
        self.encryptButton.grid(row=1, column=0, padx=40, pady=20)

        self.rightBox = TextBox(self, font=boxfont)
        self.rightBox.grid(row=0, column=1, padx=40)
        self.decryptButton = customtkinter.CTkButton(self, width=200,  text='Decrypt', font=buttonFont, command=self.decrypt_text)
        self.decryptButton.grid(row=1, column=1, padx=40, pady=20)

    def encrypt_text(self):
        message: str = self.leftBox.textBox.get('0.0', 'end').strip()
        result: str = None
        try:
            result = encrypt(message)
        except:
            result = 'Whoops.'
        self.rightBox.textBox.delete('0.0', 'end')
        self.rightBox.textBox.insert('0.0', result)

    def decrypt_text(self):
        message: str = self.rightBox.textBox.get('0.0', 'end').strip()
        result: str = None
        try:
            result = decrypt(message)
        except:
            result = 'Whoops.'
        self.leftBox.textBox.delete('0.0', 'end')
        self.leftBox.textBox.insert('0.0', result)
