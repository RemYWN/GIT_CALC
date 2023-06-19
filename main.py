import tkinter as tk

root = tk.Tk()
root.title('Kalkulator prosty')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 360
window_height = 360

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(0,0)

input_value = ""

display_text = tk.StringVar()

input_frame = tk.Frame(root, width=350, height=10, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side = tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18,'bold'), textvariable=display_text,width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)



def numberClick(number):
    global input_value
    input_value = input_value+ str(number)
    display_text.set(input_value)

def clearClick():
    global input_value
    input_value = ""
    display_text.set("")

def equalClick():
    global input_value
    result = str(eval(input_value))
    display_text.set(result)
    input_value = ""



jeden = tk.Button(text='1', height=3, width=6, command=lambda: numberClick(1))
jeden.pack()
jeden.place(x=15, y=100)

dwa = tk.Button(text='2', height=3, width=6, command=lambda:numberClick(2))
dwa.pack()
dwa.place(x=70,y=100)

trzy = tk.Button(text='3', height=3, width=6, command=lambda:numberClick(3))
trzy.pack()
trzy.place(x=125, y=100)

cztery = tk.Button(text='4', height=3, width=6, command=lambda:numberClick(4))
cztery.pack()
cztery.place(x=15, y=160)

piec = tk.Button(text='5', height=3, width=6, command=lambda:numberClick(5))
piec.pack()
piec.place(x=70, y=160)

szesc = tk.Button(text='6', height=3, width=6, command=lambda:numberClick(6))
szesc.pack()
szesc.place(x=125, y=160)

siedem = tk.Button(text='7', height=3, width=6, command=lambda:numberClick(7))
siedem.pack()
siedem.place(x=15, y=220)

osiem = tk.Button(text='8', height=3, width=6, command=lambda:numberClick(8))
osiem.pack()
osiem.place(x=70, y=220)

dziewiec = tk.Button(text='9', height=3, width=6, command=lambda:numberClick(9))
dziewiec.pack()
dziewiec.place(x=125, y=220)

zero = tk.Button(text='0', height=3, width=6, command=lambda:numberClick(0))
zero.pack()
zero.place(x=70,y=280)

clear = tk.Button(text='C', height=3, width=6, command=clearClick)
clear.pack()
clear.place(x=15, y=280)

equals = tk.Button(text='=', height=3, width=6, command=equalClick)
equals.pack()
equals.place(x=125, y=280)

plus = tk.Button(text='+', height=3, width=6, command=lambda:numberClick("+"))
plus.pack()
plus.place(x=235, y=100)

minus = tk.Button(text='-', height=3, width=6, command=lambda:numberClick("-"))
minus.pack()
minus.place(x=290, y=100)

divider = tk.Button(text='/', height=3, width=6, command=lambda:numberClick("/"))
divider.pack()
divider.place(x=235, y=160)

multiplier = tk.Button(text='x', height=3, width=6, command=lambda:numberClick("*"))
multiplier.pack()
multiplier.place(x=290, y=160)


root.mainloop()