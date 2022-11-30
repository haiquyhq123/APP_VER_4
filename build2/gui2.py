from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/haiquy/OnlineJudgeDeploy/build2/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1366x768")
window.configure(bg = "#FFFFFF")

 

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1211.0,
    y=0.0,
    width=167.0,
    height=161.0
)

"""canvas.create_rectangle(
    -4.0,
    75.76373291015625,
    1235.0,
    80.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1342.0,
    76.0,
    1440.0,
    80.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    178.0,
    75.0,
    186.0,
    1024.0,
    fill="#000000",
    outline="")

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=0.0,
    y=108.0,
    width=167.0,
    height=106.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=395.0,
    y=406.0,
    width=163.0,
    height=61.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=985.0,
    y=406.0,
    width=163.0,
    height=61.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=0.0,
    y=255.0,
    width=167.0,
    height=106.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=0.0,
    y=397.0,
    width=167.0,
    height=106.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=384.0,
    y=202.0,
    width=188.0,
    height=167.0
)

canvas.create_text(
    202.0,
    104.0,
    anchor="nw",
    text="Nhung Thiet Ke Mau:",
    fill="#000000",
    font=("Inter", 30 * -1)
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=846.0,
    y=213.0,
    width=413.0,
    height=148.0
)

canvas.create_text(
    19.0,
    20.0,
    anchor="nw",
    text="OTESL",
    fill="#000000",
    font=("Inter", 40 * -1)
)

canvas.create_rectangle(
    175.0,
    158.0,
    1440.0,
    162.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    174.0,
    507.0,
    1440.0,
    512.0,
    fill="#000000",
    outline="")

canvas.create_text(
    205.0,
    536.0,
    anchor="nw",
    text="Ca Nhan Hoa (Thiet Ke Nang Cao):",
    fill="#000000",
    font=("Inter", 30 * -1)
)

canvas.create_rectangle(
    177.0,
    589.9233856201172,
    1439.999755859375,
    599.0,
    fill="#000000",
    outline="")

canvas.create_text(
    205.0,
    622.0,
    anchor="nw",
    text="Tinh Nang Nay Dang Trong Giai Doan Phat Trien.\n Xin Loi Quy Khach Vi Su Bat TIen Nay !!!",
    fill="#000000",
    font=("Inter", 25 * -1)
)"""
window.resizable(False, False)
window.mainloop()
