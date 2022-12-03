from tkinter import *
from PIL import Image, ImageFont, ImageDraw


#--------------Function to add watermark---------------------------------
def add_watermark():
    watermark = watermark_text.get()
    print(watermark)
    img = Image.open(img_entry.get())

    replica_img = img.copy()

    draw = ImageDraw.Draw(replica_img)

    font = ImageFont.truetype("arial.ttf", 35)
    draw.text((230, 230), watermark, (int(r.get("1.0",'end-1c')), int(g.get("1.0",'end-1c')), int(b.get("1.0", 'end-1c'))), font=font)
    replica_img.show()

#-------------------------------UI---------------------------------------
window = Tk()
window.title("Watermark To Image")
window.minsize(500, 500)
window.config(padx=50, pady=50, bg="yellow")

# setting up canvas and logo image
canvas = Canvas(width=300, height=100, bg="yellow", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(155, 40, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2, pady=10)

# Widgets
img_path_label = Label(text="Enter Image Path: ", bg="Yellow", font=("Arial", 12, "bold"), justify=LEFT)
img_path_label.grid(row=1, column=0)
img_entry = Entry(width=40)
img_entry.grid(row=1, column=1, pady=10)

watermark_label = Label(text="Enter watermark to add:", bg="Yellow", font=("Arial", 12, "bold"), justify=LEFT)
watermark_label.grid(row=2, column=0, padx=10)
watermark_text = Entry(width=40)
watermark_text.grid(row=2, column=1, pady=10)

red = Label(text="Enter r value: ", justify=LEFT, bg="Yellow", font=("Arial", 12, "bold"))
red.grid(row=3, column=0)
r = Text(height=1, width=8)
r.grid(row=3, column=1, pady=10)

green = Label(text="Enter g value: ", bg="Yellow", font=("Arial", 12, "bold"), justify=LEFT)
green.grid(row=4, column=0)
g = Text(height=1, width=8)
g.grid(row=4, column=1, pady=10)

blue = Label(text="Enter b value: ", bg="Yellow", font=("Arial", 12, "bold"), justify=LEFT)
blue.grid(row=5, column=0)
b = Text(height=1, width=8)
b.grid(row=5, column=1, pady=10)

# Button
Add_watermark_button = Button(text="Add Watermark", relief=GROOVE, command=add_watermark, font=("Arial", 12, "italic"))
Add_watermark_button.grid(row=6, column=0, columnspan=4, pady=10)

window.mainloop()