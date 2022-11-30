from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/haiquy/OnlineJudgeDeploy/build3/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("350x550")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 550,
    width = 350,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    92.0,
    314.0,
    anchor="nw",
    text="TRÌNH CÀI ĐẶT Sever",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    -2.0,
    28.0,
    349.9998779296875,
    31.044769287109375,
    fill="#000000",
    outline="")

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
    x=129.0,
    y=49.0,
    width=72.0,
    height=33.0
)

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
    x=3.0,
    y=137.0,
    width=108.0,
    height=28.0
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
    x=121.0,
    y=137.0,
    width=103.0,
    height=28.0
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
    x=234.0,
    y=137.0,
    width=112.0,
    height=27.0
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
    x=234.0,
    y=171.0,
    width=112.0,
    height=27.0
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
    x=117.0,
    y=206.0,
    width=120.88888549804688,
    height=27.0
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
    x=117.0,
    y=241.0,
    width=112.0,
    height=27.0
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
    x=6.0,
    y=279.0,
    width=112.0,
    height=27.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=126.0,
    y=279.0,
    width=112.0,
    height=27.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=244.0,
    y=279.0,
    width=92.0,
    height=27.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=124.0,
    y=172.0,
    width=100.3611068725586,
    height=26.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=7.0,
    y=172.0,
    width=104.0,
    height=26.0
)

canvas.create_rectangle(
    -2.0,
    98.0,
    350.0,
    100.0,
    fill="#000000",
    outline="")

canvas.create_text(
    78.0,
    6.0,
    anchor="nw",
    text="TRÌNH CÀI ĐẶT TRANG WEB",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    -2.0,
    128.0,
    350.0,
    130.0,
    fill="#000000",
    outline="")

canvas.create_text(
    111.0,
    108.0,
    anchor="nw",
    text="ROAD MAP CÀI ĐẶT",
    fill="#000000",
    font=("Inter", 11 * -1)
)

canvas.create_rectangle(
    -2.0,
    273.0,
    350.0,
    275.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    -2.0,
    308.0,
    350.0,
    310.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    10.0,
    306.0,
    13.034194946289062,
    549.9998474121094,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    334.0,
    306.0,
    336.0,
    550.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    12.0,
    336.0,
    337.0,
    339.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
