from tkinter import *
from tkinter import messagebox
import random
import webbrowser
import mysql.connector as sql

# Database Connection

my_db = sql.connect(
    host="localhost",
    user="root",
    passwd="varun"
)
c = my_db.cursor()
c.execute("use sudoku")

# Main Window

root = Tk()
root.title("Sudoku")
root.resizable(False, False)
grid_frame = Frame(root)

# Flag

global flag
c.execute("select gno from start")
s_gno = c.fetchall()
global l_gno
l_gno = []
for x in s_gno:
    l_gno.append(x[0])
flag = random.choice(l_gno)
global str_flag
str_flag = str(flag)

# Predefined Unsolved

global start
start = []

# Predefined Editable

global game
game = start.copy()

# Predefined Solved

global game_solved
game_solved = []


# Populating Arrays

def flag_copy(no):
    global start
    global game
    global game_solved
    c.execute(f"select * from start where gno={no}")
    fetch = list(c.fetchall()[0])
    fetch.pop(0)
    start = fetch.copy()
    game = start.copy()
    c.execute(f"select * from solved where gno={no}")
    s_fetch = list(c.fetchall()[0])
    s_fetch.pop(0)
    game_solved = s_fetch.copy()


flag_copy(flag)

# Variables

global k
k = 0


# Releases

def releases(event):
    global info
    webbrowser.open_new("https://github.com/VarunS2002/Python-Sudoku-MySQL/releases/")
    info.attributes('-topmost', False)


# Sources

def sources(event):
    global info
    webbrowser.open_new("https://github.com/VarunS2002/Python-Sudoku-MySQL/")
    info.attributes('-topmost', False)


# Choose Game Window

def choose_window():
    window = Toplevel()
    window.title("Choose")
    window.resizable(False, False)
    window.geometry('220x200')
    window.attributes('-topmost', True)
    window.grab_set()
    window.focus_force()
    return window


# Choose Game Function

def choose_game():
    window = choose_window()
    listbox = Listbox(window)
    global l_gno
    for x in l_gno:
        listbox.insert(END, x)
    listbox.focus_force()
    button_frame = Frame(window)

    # Ok Button Function

    def do_ok():
        global flag
        flag = listbox.get(ACTIVE)
        global start
        global game
        global game_solved
        flag_copy(flag)
        global str_flag
        str_flag = str(flag)
        new()
        window.destroy()

    # Cancel Button Function

    def do_cancel():
        window.destroy()

    ok = Button(button_frame, command=do_ok, text="Ok")
    ok.pack(side='left', fill='x', expand='1')

    cancel = Button(button_frame, command=do_cancel, text="Cancel")
    cancel.pack(side='right', fill='x', expand='1')

    listbox.pack(side='top', fill='both', expand='1')
    button_frame.pack(side='top', fill='x', expand='1')

    window.mainloop()


# Choose Number Function

def choose(btn_x, btn_y):
    x = 'a' + str(btn_x) + str(btn_y)
    exec('y=' + x + str(['text']), globals())
    global y
    y = (y % 9) + 1
    exec('a' + str(btn_x) + str(btn_y) + f'.config(text = {y} )')
    index = (btn_x * 9) + btn_y
    game[index] = y


# Restart Game Function

def new():
    global game
    game = start.copy()
    global text_colour
    for z in range(9):
        for w in range(9):
            exec('a' + str(z) + str(w) + '.config(text = game[(z*9)+w])')
            if game[(z * 9) + w] == 0:
                exec('a' + str(z) + str(w) + '.config(state = NORMAL)')
                text_colour = "blue"
            else:
                text_colour = "black"
                exec('a' + str(z) + str(w) + '.config(state = DISABLED)')
            exec('a' + str(z) + str(w) + '.config(fg = text_colour)')
    file.entryconfig(file.index(0), label=f"Choose Game: {str_flag}", state=NORMAL)
    file.entryconfig(file.index("Check Result"), state=NORMAL)


# Result Function

def check():
    if game == game_solved:
        messagebox.showinfo("Result", "You won")
    else:
        messagebox.showinfo("Result", "You lost")


# Solution Function

def sol():
    global game
    game = game_solved.copy()
    for z in range(9):
        for w in range(9):
            text = game_solved[(z * 9) + w]
            index = (z * 9) + w
            game[index] = text
            exec('a' + str(z) + str(w) + f'.config(text = {text})')
            exec('a' + str(z) + str(w) + '.config(state = DISABLED)')
            file.entryconfig(file.index("Check Result"), state=DISABLED)


# About Window

def about_window():
    global info
    info = Toplevel()
    info.title("About")
    info.resizable(False, False)
    info.geometry('220x100')
    info.attributes('-topmost', True)
    info.grab_set()
    info.focus_force()
    return info


# About Function

def about():
    info = about_window()
    version = Label(info, text="Version: 1.0")
    version.pack(side='top', fill='x', expand='1')
    release = Label(info, text="Releases", fg="blue", cursor="hand2")
    release.pack(side='top', fill='x', expand='1')
    release.bind("<Button-1>", releases)
    source = Label(info, text="Sources", fg="blue", cursor="hand2")
    source.pack(side='top', fill='x', expand='1')
    source.bind("<Button-1>", sources)
    info.mainloop()


# Quit Function

def close():
    ask_quit = messagebox.askyesno("Quit", "Do you want to quit?")
    if ask_quit:
        quit()
    elif not ask_quit:
        pass


# Grid

for rowindex in range(9):

    for colindex in range(9):

        if rowindex in (0, 1, 2, 6, 7, 8) and colindex in (3, 4, 5):
            bg_colour = "light grey"
        elif rowindex in (3, 4, 5) and colindex in (0, 1, 2, 6, 7, 8):
            bg_colour = "light grey"
        else:
            bg_colour = "white"

        x = start[k]
        k = k + 1
        if x == 0:
            text_colour = "blue"
        else:
            text_colour = "black"
        btn_name = ''
        exec('btn_name = "a" + str(rowindex) + str(colindex)')
        exec(
            btn_name + '= Button(grid_frame, width=8, height=4, bg=bg_colour,fg=text_colour, text=x,command=lambda '
                       'i=rowindex, '
                       'j=colindex : choose(i,j))')
        exec(btn_name + '.grid(row=rowindex, column=colindex, sticky=N+S+E+W)')
        if text_colour == 'black':
            exec('a' + str(rowindex) + str(colindex) + '.config(state = DISABLED)')
        grid_frame.pack()

# Option Menu

menubar = Menu(root)
file = Menu(menubar, tearoff=0)
file.add_command(label=f"Choose Game: {str_flag}", command=choose_game)
file.add_command(label="Restart Game", command=new)
file.add_separator()
file.add_command(label="Check Result", command=check)
file.add_command(label="Show Solution", command=sol)
file.add_separator()
file.add_command(label="About", command=about)
file.add_command(label="Quit", command=close)
menubar.add_cascade(label="Menu", menu=file)
root.config(menu=menubar)
root.protocol('WM_DELETE_WINDOW', close)

root.mainloop()
