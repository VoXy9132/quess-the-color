from tkinter import *
from random import choice
def start_time():
    global time_left, health, colour, start
    text_time_left.config(text=f'Осталось {time_left} секунд.')
    time_left -= 1
    if time_left < 0:
        time_left = 30
        text_check.config(text=f'Поздно')
        colour = choice(colours)
        health = 3
        start = False
        text_enter.config(text='Нажмите Enter, чтобы стартовать')
        text_colour.config(text='')
        text_time_left.config(text='')
    else:
        text_time_left.after(1000, start_time)
def Start(num):
    global start, colour, health, time_left
    if not start:
        start = True
        start_time()
        text_enter.config(text='Нажмите Enter, чтобы подтвердить')
        text_colour.config(text=choice(colours), fg=colour)
    else:
        if colour.lower() == variable.get().lower():
            colour = choice(colours)
            text_colour.config(text=choice(colours), fg=colour)
            text_check.config(text='Верно')
            time_left = 30
        else:
            if health < 2:
                colour = choice(colours)
                health = 3
                text_colour.config(text=choice(colours), fg=colour)
                time_left = 30
            else:
                health -= 1
            text_check.config(text=f'Неверно, осталось жизней {health}')
    colour_entry.delete(0, END)
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
start = False
time_left = 30
health = 3
font_default = ("Helvetica", 20)
width, height = 600, 600
colour = choice(colours)
root = Tk()
root.geometry(f"{width}x{height}")
text_enter = Label(root, text='Введите Enter, чтобы начать, жизней всего 3', font=font_default)
variable = StringVar()
colour_entry = Entry(textvariable=variable)
text_colour = Label(root, fg=colour, font=(font_default[0], 30))
text_check = Label(root, font=(font_default[0], 15))
text_time_left = Label(root, font=(font_default[0], 15))
text_enter.pack()
text_colour.pack()
colour_entry.pack()
text_check.pack()
text_time_left.pack()
root.bind('<Return>', Start)

root.mainloop()