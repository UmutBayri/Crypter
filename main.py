import base64

from tkinter import BooleanVar, Tk, Entry, Text, Button, Frame, Label, mainloop
from tkinter.constants import BOTTOM, END, GROOVE, LEFT, RIGHT, SUNKEN, TOP, BOTH, UNDERLINE, X


class Crypter(Tk):
    def __init__(self):
        super().__init__()    
        
        self.title("Crypter")
        self.resizable(False, False)
  
        self.btn_elements = [("Clean", self.clean), ("Decrypt", self.decrypt), ("Ecrypt", self.ecrypt)]
        self.font = ("Courier", 13)
        self.font_underline = ("Courier", 13, UNDERLINE)

        self.frame_left = Frame(self)
        self.frame_right = Frame(self)

        self.create_button()
        self.create_text()
        self.create_lbl()

        self.locate()
        self.mainloop()

    def create_button(self):
        for element in self.btn_elements:
            self.ecrypt_btn = Button(
                self.frame_left,
                text = element[0],
                font = self.font,
                height = 2,
                bd = 1,
                command = element[1]
            )
            self.ecrypt_btn.pack(side = BOTTOM, fill = X)

    def create_text(self):
        self.output_text = Text(
            self.frame_right,
            font = self.font,
            bd = 2, relief = GROOVE,
            width = 40, height =15
        )

        self.entry_text = Text(
            self.frame_left,
            font = self.font,
            bd = 2, relief = GROOVE,
            width = 40, height = 7
        )

    def create_lbl(self):
        self.input_lbl = Label(
            self.frame_left, text = "Input", font = self.font_underline
        )
        self.output_lbl = Label(
            self.frame_right, text = "Output", font = self.font_underline
        )

    def locate(self):
        self.frame_left.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 5)
        self.frame_right.pack(side = RIGHT, fill = BOTH, expand = True, padx = 5, pady = 5)
       
        self.output_lbl.pack(padx = 10, side = TOP, anchor = "w")
        self.output_text.pack(fill = BOTH, expand = True, pady = 5)

        self.input_lbl.pack(padx = 10, side = TOP, anchor = "w")
        self.entry_text.pack(padx = 5, pady = 5)

    def ecrypt(self):
        try :
            self.output_text.delete(1.0, END)
            input = self.entry_text.get(1.0, END)
            input_type_byte = input.encode("UTF-8")
            self.ecrypted_input = base64.b64encode(input_type_byte)
            self.output_text.insert(END, self.ecrypted_input)

        except :
            pass
    
    def decrypt(self):
        try :
            self.output_text.delete(1.0, END)
            input = self.entry_text.get(1.0, END)
            input_type_byte = input.encode("UTF-8")
            self.decrypted_input = base64.b64decode(input_type_byte)
            self.output_text.insert(END, self.decrypted_input)
        
        except :
            pass
        
    def clean(self):
        self.entry_text.delete(1.0, END)
        self.output_text.delete(1.0, END)

    
root = Crypter()