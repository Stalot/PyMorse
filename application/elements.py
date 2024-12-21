import customtkinter
from translator import encrypt, decrypt

class Top(customtkinter.CTkFrame):
    def __init__(self, *args, font: customtkinter.CTkFont = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure((0, 1), weight=1)

        self.title = customtkinter.CTkLabel(self, text='PyMorse', font=font)
        self.title.grid(row=0, column=0, sticky='ew')

class TextBox(customtkinter.CTkFrame):
    def __init__(self, *args, boxfont: customtkinter.CTkFont = None, command = None, action_button_text: str = '', **kwargs):
        super().__init__(*args, **kwargs)

        buttonFont = customtkinter.CTkFont('Arial', 24)

        self.grid_columnconfigure((0, 1), weight=1)

        self.textBox = customtkinter.CTkTextbox(self, font=boxfont, width=600, height=500)
        self.textBox.pack()

        self.copy = customtkinter.CTkButton(self, width=100, height=40, font=buttonFont, text='Copy', command=self.copy_to_clipboard)
        self.copy.pack(side='left', padx=(0, 10), pady=10)
        self.paste = customtkinter.CTkButton(self, width=100, height=40, font=buttonFont, text='Paste', command=self.paste_from_clipboard)
        self.paste.pack(side='left', padx=(0, 10), pady=10)

        self.action = customtkinter.CTkButton(self, width=100, height=40, font=buttonFont, text=action_button_text, command=command, fg_color='springgreen2', hover_color='springgreen4')
        self.action.pack(side='left', padx=(0, 10))

    def copy_to_clipboard(self):
        text: str = str(self.textBox.get('0.0', 'end')).strip()
        self.copy.clipboard_clear()
        self.copy.clipboard_append(text)

    def paste_from_clipboard(self):
        text: str = str(self.paste.clipboard_get()).strip()
        self.textBox.delete('0.0', 'end')
        self.textBox.insert('0.0', text)

class Display(customtkinter.CTkFrame):
    def __init__(self, *args, boxfont: customtkinter.CTkFont = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure((0, 1), weight=1)

        self.leftBox = TextBox(self, boxfont=boxfont, fg_color = 'transparent', action_button_text='Encrypt', command=self.encrypt_text)
        self.leftBox.grid(row=0, column=0, padx=40)
        #self.encryptButton = customtkinter.CTkButton(self, width=200, text='Encrypt', font=buttonFont, command=self.encrypt_text)
        #self.encryptButton.grid(row=1, column=0, padx=40, pady=20)

        self.rightBox = TextBox(self, boxfont=boxfont, fg_color = 'transparent', action_button_text='Decrypt', command=self.decrypt_text)
        self.rightBox.grid(row=0, column=1, padx=40)
        #self.decryptButton = customtkinter.CTkButton(self, width=200,  text='Decrypt', font=buttonFont, command=self.decrypt_text)
        #self.decryptButton.grid(row=1, column=1, padx=40, pady=20)

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
