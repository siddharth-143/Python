"""
    Python program to convert jpeg image to png
"""

from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()  # Tkinter window initialized
root.title("Convertor")  # Title of the window

canvas = Canvas(root, width=300, height=250, bg="orange", relief="raised")
canvas.pack()

label1 = Label(root, text="File convertor", bg="lightsteelblue2")  # Giving title to the screen
label1.config(font=("helvetica", 20))

canvas.create_window(150, 50, window=label1)

img1 = None  # variable to store path of image

def get_jpeg():
    """Function to get image location and open it with pillow"""
    global img1
    import_file_path = filedialog.askopenfilename()
    img1 = Image.open(import_file_path)


font = ("helvetica", 12, "bold")
bg = "royalblue"
fg = "white"

jpeg = Button(text="Import jpeg image",command=get_jpeg, bg=bg, fg=fg, font=font)
canvas.create_window(150, 100, window=jpeg)

def convert_to_png():
    """ Function to change file extension to png and save it to user's prefered location"""
    global img1
    if img1 is None:
        Message.showerror("Error no file is selected")

    else:
        export_file_path = filedialog.asksaveasfilename(defaultextension=".png")
        img1.save(export_file_path)


save_as_button = Button(text="Convert JPEG to PNG", command=convert_to_png, bg=bg, fg=fg, font=font)  # Convertor button
canvas.create_window(150, 180, window=save_as_button)

root.mainloop()