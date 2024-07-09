from tkinter import *
from tkinter.constants import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import adachi_generator

class App():
     def __init__(self):
          self.root = Tk()
          self.file_name = None
          self.root.title("Adachi Gen")
          self.root.minsize(300, 100)
          self.bottom_text = StringVar()

          Button(text="Choose an image", command=self.get_file_name).pack(pady=10)
          Label(text="Enter bottom text").pack(pady=10)
          Entry(textvariable=self.bottom_text).pack(pady=10)
          Button(text="Adachify!", command=self.adachify).pack(pady=10)
     
     def get_file_name(self):
          self.file_name = askopenfilename(filetypes=[("PNG", '.png')])
     
     def adachify(self):
          adachi_generator.adachify(self.file_name, self.bottom_text.get())
          

def main():
     app = App()
     app.root.mainloop()

if __name__ == "__main__":
    main()