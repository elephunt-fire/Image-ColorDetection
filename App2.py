# resizable dialog box

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os

root = tk.Tk()
root.title('Color picked from image')
root.geometry('800x470+100+100')
root.config(bg='#e4e8eb')
root.resizable(True, True)

def showImage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select image File',
                                          filetypes=(('Png File', '*.png'),
                                                     ('Jpg File', '*.jpg'),
                                                     ('All File', '*.*')))
    if filename:
        img = Image.open(filename)
        img = img.resize((310, 270), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        label.configure(image=img)
        label.image = img

def FindColor():
    ct = ColorThief(filename)
    palette = ct.get_palette(color_count=11)

    # Convert RGB to Hex
    colors_list = [f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}' for color in palette[:10]]

    # Set colors for the rectangles and labels
    for i in range(5):
        colors.itemconfig(ids[i], fill=colors_list[i])
        colors2.itemconfig(ids2[i], fill=colors_list[i + 5])
        hex_labels[i].config(text=colors_list[i])
        hex_labels2[i].config(text=colors_list[i + 5])

# Main layout using grid
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Main frame that resizes with window
frame = tk.Frame(root, bg='#fff')
frame.grid(sticky="nsew", padx=20, pady=20)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(1, weight=1)

# Logo and title
logo = tk.PhotoImage(file='logo.png')
tk.Label(frame, image=logo, bg='#fff').grid(row=0, column=0, sticky='w', padx=10)
tk.Label(frame, text='Color Finder', font='arial 25 bold', bg='white').grid(row=0, column=1, sticky='w')

# Canvas for colors
colors = tk.Canvas(frame, bg='#fff', bd=0)
colors.grid(row=1, column=0, sticky="nsew", padx=(0, 10))

colors2 = tk.Canvas(frame, bg='#fff', bd=0)
colors2.grid(row=1, column=1, sticky="nsew")

# Set of rectangles for colors
ids = [colors.create_rectangle((10, 10 + i*50, 50, 50 + i*50), fill='#b8255f') for i in range(5)]
ids2 = [colors2.create_rectangle((10, 10 + i*50, 50, 50 + i*50), fill='#7ecc49') for i in range(5)]

# Labels for color hex codes
hex_labels = [tk.Label(colors, text='#b8255f', font='arial 15 bold', bg='white') for _ in range(5)]
hex_labels2 = [tk.Label(colors2, text='#7ecc49', font='arial 15 bold', bg='white') for _ in range(5)]

# Position hex labels
for i, label in enumerate(hex_labels):
    label.place(x=60, y=15 + i*50)
for i, label in enumerate(hex_labels2):
    label.place(x=60, y=15 + i*50)

# Frame for selecting the image
selectimage = tk.Frame(frame, bg='#d6dee5', bd=2)
selectimage.grid(row=1, column=2, sticky="nsew", padx=(10, 0))

# Image frame
f = tk.Frame(selectimage, bd=3, bg='black')
f.pack(expand=True, fill="both", padx=10, pady=10)

label = tk.Label(f, bg='black')
label.pack(expand=True, fill="both")

# Buttons
button_frame = tk.Frame(selectimage, bg='#d6dee5')
button_frame.pack(fill="x", pady=10)
tk.Button(button_frame, text='Select Image', font='arial 14 bold', command=showImage).pack(side='left', padx=10)
tk.Button(button_frame, text='Find Color', font='arial 14 bold', command=FindColor).pack(side='left', padx=10)

root.mainloop()
