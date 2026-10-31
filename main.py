import random
import string
import win32print
import win32ui

# opsec level 67


class PasswortGen:

    def __init__(self):
        self.pw = ""
        self.characters = string.digits + string.ascii_letters + string.punctuation
        self.header = ""
        self.site_to_safe = ""
        self.document = None
        self.printer = win32print.GetDefaultPrinter()
        self.length = 0

    def set_length(self, length):
        self.length = length

    def create_document(self):
        self.document = win32ui.CreateDC()
        self.document.CreatePrinterDC(self.printer)

    def start_gen(self, s, username):
        for i in range(self.length):
            self.pw += random.choice(self.characters)

        self.header = f"Password for site: {s}"
        txt_pw =self.pw
        txt_use = username
        self.pw = ""

        self.create_document()
        self.document.StartDoc("Generated Password")
        self.document.StartPage()
        self.document.TextOut(100, 100, self.header)
        self.document.TextOut(100, 200, f"Username: {txt_use}")
        self.document.TextOut(100 , 300, f"Password: {txt_pw}")
        self.document.EndPage()
        self.document.EndDoc()
        self.document.DeleteDC()


pw_length = int(input("Type the length of password"))

site_object = input("Type site: ")
obj_username = input("Type Username or Email: ")
app = PasswortGen()
app.set_length(pw_length)
app.start_gen(site_object, obj_username)
