import secrets
import string
import win32print
import win32ui
# all modules loaded
# opsec level 67


class PasswortGen:
# define class 
    def __init__(self):
        self.pw = "" # password varible
        self.characters = string.digits + string.ascii_letters + string.punctuation #all characters for the gen
        self.header = "" # header in flie 
        self.site_to_safe = "" # not in use
        self.document = None # define the later document varible 
        self.printer = win32print.GetDefaultPrinter() # get the default printer 
        self.length = 0 # length of the password 

    def set_length(self, length):
        self.length = length # set length for the password 

    def create_document(self):
        # create the temp document 
        self.document = win32ui.CreateDC()
        # create the printer for printing your password
        self.document.CreatePrinterDC(self.printer)

    def start_gen(self, s, username):
        for i in range(self.length):
            self.pw += secrets.choice(self.characters) # randomise the letter

        self.header = f"Password for site: {s}" # the site for the password do you want to use as header
        txt_pw = self.pw # temp var  for pw 
        txt_use = username # temp var for username 
        self.pw = "" # reset 
        username = "" # reset

        self.create_document() # create the document for your Password 
        self.document.StartDoc("Generated Password") # start the document
        self.document.StartPage() # start your writng page
        self.document.TextOut(100, 100, self.header) # write header in the document 
        self.document.TextOut(100, 200, f"Username: {txt_use}") # write the username in the document
        txt_use = "" # reset
        self.document.TextOut(100 , 300, f"Password: {txt_pw}")
        txt_pw = "" # reset 
        self.document.EndPage() # load the end page 
        self.document.EndDoc() # close the document
        self.document.DeleteDC() # delete the document


pw_length = int(input("Type the length of password")) # user input to define the password length

site_object = input("Type site: ") # user input to define site do you want to use your pw
obj_username = input("Type Username or Email: ") # user input to define your username which do you use or email address
app = PasswortGen() # load main programm
app.set_length(pw_length) # set the password length
app.start_gen(site_object, obj_username) # start the gen
