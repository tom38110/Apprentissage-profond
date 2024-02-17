import os
import tkinter as tk
from PIL import Image, ImageTk

class ImageClassifierApp:
    def __init__(self, master, image_folder):
        self.master = master
        self.image_folder = image_folder
        self.images = os.listdir(image_folder)
        self.current_image_index = 0

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.image_label = self.canvas.create_image(0, 0, anchor=tk.NW)
        self.load_image()

        master.bind("<Left>", lambda event: self.keep_image())
        master.bind("<Right>", lambda event: self.discard_image())

    def load_image(self):
        image_path = os.path.join(self.image_folder, self.images[self.current_image_index])
        image = Image.open(image_path)
        image.thumbnail((400, 400))
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.itemconfig(self.image_label, image=self.tk_image)

    def keep_image(self):
        print("Image gardée :", self.images[self.current_image_index])
        self.next_image()

    def discard_image(self):
        print("Image supprimée :", self.images[self.current_image_index])
        os.remove(os.path.join(self.image_folder, self.images[self.current_image_index]))
        del self.images[self.current_image_index]
        if self.current_image_index >= len(self.images):
            self.current_image_index = 0
        self.load_image()

    def next_image(self):
        self.current_image_index += 1
        if self.current_image_index >= len(self.images):
            self.current_image_index = 0
        self.load_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageClassifierApp(root, "./Cathedrale_Saint_Etienne/")
    root.mainloop()
